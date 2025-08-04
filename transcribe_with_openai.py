import openai
import tempfile
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
openai.api_type="azure"
openai.api_key=os.getenv("AZURE_OPENAI_KEY",st.secrets.get("AZURE_OPENAI_KEY",None))
openai.api_version=os.getenv("AZURE_OPENAI_API_VERSION",st.secrets.get("AZURE_OPENAI_API_VERSION",None))
openai.api_base=os.getenv("AZURE_OPENAI_ENDPOINT",st.secrets.get("AZURE_OPENAI_ENDPOINT",None))

def transcribe_audio(audio_file):
    """
    Transcribes uploaded audio using Azure OpenAI Whisper model.
    Accepts either file-like object (from st.file_uploader) or string path.
    """
    if isinstance(audio_file, str):
        tmp_path = audio_file  # it's already a path
    else:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(audio_file.read())
            tmp_path = tmp.name

    with open(tmp_path, "rb") as f:
        transcript = openai.audio.transcriptions.create(
            model="whisper",  # replace with your actual deployment name
            file=f
        )

    # Don't delete temp_path if user passed their own path
    if not isinstance(audio_file, str):
        os.remove(tmp_path)

    return transcript.text