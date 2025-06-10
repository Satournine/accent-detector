import os
import uuid
import requests
import ffmpeg
import whisper
import torch
import torchaudio
torchaudio.set_audio_backend("soundfile")
from speechbrain.pretrained import EncoderClassifier
torch.classes.__path__ = []
accent_model = EncoderClassifier.from_hparams(
    source="Jzuluaga/accent-id-commonaccent_ecapa",
    savedir="pretrained_models/accent-id-commonlanguage_ecapa"
)

MAX_DURATION = 20
SAMPLE_RATE = 16000
MAX_SAMPLES = SAMPLE_RATE * MAX_DURATION

def download_video(url: str, save_dir="temp") -> str:
    os.makedirs(save_dir, exist_ok=True)
    filename = f"{uuid.uuid4()}.mp4"
    filepath = os.path.join(save_dir, filename)

    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filepath, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return filepath
    else:
        raise Exception(f"Failed to download video.")
def extract_audio(video_path: str) -> str:
    audio_path = video_path.replace(".mp4", ".wav")
    try:
        probe = ffmpeg.probe(video_path)
        has_audio = any(stream['codec_type'] == 'audio' for stream in probe['streams'])
        if not has_audio:
            raise RuntimeError("No audio stream found in the video.")
        ffmpeg.input(video_path).output(audio_path, ac=1, ar='16000').run(overwrite_output=True, quiet=True)
    except ffmpeg.Error as e:
        raise RuntimeError(f"FFmpeg error: {e.stderr.decode()}")
    return audio_path


def transcribe_audio(audio_path: str, model_size="base"):
    model = whisper.load_model(model_size)
    result = model.transcribe(audio_path, language="en")

    return {
        "transcript": result["text"],
        "language": result.get("language", "en"),
        "segments": result.get("segments", [])
    }


def classify_accent(audio_path: str):
    out_prob, score, index, label = accent_model.classify_file(audio_path)
    return {
        "accent": label,
        "confidence": round(score.item() * 100, 2),
            }
