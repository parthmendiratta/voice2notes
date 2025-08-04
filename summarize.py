import os
import streamlit as st
from openai import AzureOpenAI
from dotenv import load_dotenv
load_dotenv()

api_key=os.getenv("AZURE_OPENAI_KEY",st.secrets.get("AZURE_OPENAI_KEY",None))
api_endpont=os.getenv("AZURE_OPENAI_ENDPOINT",st.secrets.get("AZURE_OPENAI_ENDPOINT",None))
api_deployement=os.getenv("AZURE_OPENAI_DEPLOYMENT",st.secrets.get("AZURE_OPENAI_DEPLOYMENT",None))
api_version=os.getenv("AZURE_OPENAI_API_VERSION",st.secrets.get("AZURE_OPENAI_API_VERSION",None))

llm=AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY",st.secrets.get("AZURE_OPENAI_KEY",None)),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION",st.secrets.get("AZURE_OPENAI_API_VERSION",None)),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT",st.secrets.get("AZURE_OPENAI_ENDPOINT",None)),
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT",st.secrets.get("AZURE_OPENAI_DEPLOYMENT",None))
)

def summarize_text(text):
    response=llm.chat.completions.create(
        model=api_deployement,
        messages=[
            {"role":"system","content":"You are a helpful assistant that summarizes audio transcripts into clean bullet-point notes."},
            {"role":"user","content":f"Summarize this transcript:\n\n{text}"}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content