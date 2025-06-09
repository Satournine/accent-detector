from accent_utils import download_video, extract_audio, transcribe_audio, classify_accent

# Example: Use a direct .mp4 link from the web
video_url = "https://ia800508.us.archive.org/18/items/ClaytonCameron_2013Y/ClaytonCameron_2013Y.mp4"

print("Downloading...")
video_path = download_video(video_url)

print("Extracting audio...")
audio_path = extract_audio(video_path)

print("Audio saved to:", audio_path)

print("Transcribing...")
result = transcribe_audio(audio_path)

print("Transcript:\n", result["transcript"])

accent_info = classify_accent(audio_path)
print(accent_info)