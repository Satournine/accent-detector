

# 🧠 English Accent Classifier

A simple, functional tool that detects English-speaking accents from video or audio using AI.

## 🔍 What It Does

- Accepts a **video URL (MP4)** or **file upload (MP4 or WAV)**
- Extracts audio from the video
- Transcribes the speech to verify spoken English
- Classifies the speaker’s **English accent** (e.g. American, Indian, British)
- Displays a **confidence score** and the predicted accent

## ✅ Features

- Handles both file upload and direct links
- Uses Whisper for transcription
- Uses SpeechBrain's pretrained ECAPA model for accent classification
- Displays real-time status and feedback
- Streamlit UI for simplicity

## 🧪 Installation

```bash
git clone https://github.com/Satournine/accent-detector
cd accent-detector
pip install -r requirements.txt
```

## 🚀 Usage

```bash
streamlit run app.py
```

- Paste a video URL or upload a `.mp4` / `.wav` file
- Click "Analyze"
- View transcription, predicted accent, and confidence score

## 🗂️ Requirements

See `requirements.txt` for dependencies.

## 📝 Notes
- Only supports English-language audio
---