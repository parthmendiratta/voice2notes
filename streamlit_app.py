import streamlit as st
from summarize import summarize_text
from transcribe_with_openai import transcribe_audio
import os
import tempfile
import io

st.set_page_config(page_title="Voice2Notes",layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Josefin+Sans&display=swap');

    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Josefin Sans', sans-serif;
        background-image: linear-gradient(to top, #d299c2 0%, #fef9d7 100%) !important;
        background-attachment: fixed;
        background-size: cover;
    }

    [data-testid="stHeader"] {
        background-color: rgba(255, 255, 255, 0.0);
    }

    [data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎙️ Voice2Notes - Audio Transcriber & Summarizer")
st.markdown("Upload your audio file (.mp3 or .wav), and I’ll transcribe and summarize it using AI.")

uploaded_file=st.file_uploader("Upload audio",type=['wav','mp3'])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False,suffix=".wav") as temp_audio:
        temp_audio.write(uploaded_file.read())
        temp_audio_path=temp_audio.name

    st.audio(temp_audio_path,format="audio/wav")

    with st.spinner("🔍 Transcribing..."):
        transcript=transcribe_audio(temp_audio_path)

    with st.spinner("🧠 Summarizing..."):
        summary=summarize_text(transcript)

    st.success("✅ Done!")

    col1,col2=st.columns(2)

    with col1:
        st.subheader("📝 Transcript")
        st.text_area("Full transcript",transcript, height=300)
    
    with col2:
        st.subheader("📌 Summary")
        st.text_area("Concise notes",summary,height=300)

        download_btn=st.download_button(
            label='📥 Download Summary as .txt',
            data=summary,
            file_name="summary.txt",
            mime="text/plain"
        )
    os.remove(temp_audio_path)