import os
os.environ["STREAMLIT_WATCHER_TYPE"] = "none"
import asyncio

try:
    asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

        
import streamlit as st
from accent_utils import download_video, extract_audio, transcribe_audio, classify_accent

st.set_page_config(page_title="English Accent Classifier", layout="centered")
st.title("🎙️ English Accent Classifier")
status_placeholder = st.empty()

video_url = st.text_input("Enter a public video URL (MP4 or direct link):")
uploaded_file = st.file_uploader("Or upload an MP4/WAV file:", type=["mp4", "wav"])
button_placeholder = st.empty()
start_button = button_placeholder.button("🔍 Click to Analyze", type="primary")

ACCENT_MAP = {
    "african": "African English",
    "australia": "Australian English",
    "bermuda": "Bermudian English",
    "canada": "Canadian English",
    "england": "British English",
    "hongkong": "Hong Kong English",
    "indian": "Indian English",
    "ireland": "Irish English",
    "malaysia": "Malaysian English",
    "newzealand": "New Zealand English",
    "philippines": "Philippine English",
    "scotland": "Scottish English",
    "singapore": "Singapore English",
    "southatlandtic": "South Atlantic English",
    "us": "American English",
    "wales": "Welsh English",
}

if start_button and (video_url or uploaded_file):
    button_placeholder.button("⏳ Analyzing...", disabled=True)
    status_placeholder.markdown("⏳ **Processing... Please wait...**")
    if uploaded_file:
        with st.spinner("Saving uploaded file..."):
            file_extension = uploaded_file.name.split('.')[-1]
            uploaded_file_path = f"temp/uploaded_input.{file_extension}"
            with open(uploaded_file_path, "wb") as f:
                f.write(uploaded_file.read())
            if file_extension == "mp4":
                video_path = uploaded_file_path
                audio_path = extract_audio(video_path)
            else:
                audio_path = uploaded_file_path
            st.audio(audio_path)
    else:
        with st.spinner("Downloading and extracting audio..."):
            video_path = download_video(video_url)
            audio_path = extract_audio(video_path)
            st.audio(audio_path)

    with st.spinner("Transcribing audio..."):
        transcript = transcribe_audio(audio_path)
        st.success("Transcription complete!")

    with st.spinner("Classifying accent..."):
        result = classify_accent(audio_path)
        st.success("Classification complete!")
        st.subheader("🧠 Accent Classification Result")
        accent_label = result['accent']
        if isinstance(accent_label, list):
            accent_label = accent_label[0]
        accent_code = str(accent_label).lower()
        accent_name = ACCENT_MAP.get(accent_code, accent_code.capitalize())
        st.markdown(f"**Predicted Accent:** {accent_name}")
        st.markdown(f"**Confidence Score:** {result['confidence']}%")
    status_placeholder.empty()