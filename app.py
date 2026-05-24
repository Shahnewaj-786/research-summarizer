import streamlit as st
from pypdf import PdfReader
import ollama

st.set_page_config(page_title="Academic Summarizer", page_icon="📚")

st.title("📚 Research Paper Summarizer")
st.markdown("Upload a PDF to get a structured summary using local AI.")

uploaded_file = st.file_uploader("Choose a Research Paper (PDF)", type="pdf")

if uploaded_file is not None:
    # 1. Extract Text
    with st.spinner("Reading PDF..."):
        reader = PdfReader(uploaded_file)
        full_text = ""
        for page in reader.pages:
            full_text += page.extract_text()

    # 2. Setup the Prompt
    # We ask for a structured summary to make it 'Medium' level
    prompt = f"""
    You are an expert research assistant. Summarize the following research paper.
    Provide the summary in this format:
    - Main Objective:
    - Methodology:
    - Key Findings:
    - Conclusion/Future Work:

    Paper Content:
    {full_text[:4000]} # Limit text to fit context window
    """

    # 3. Generate Summary
    if st.button("Generate Summary"):
        with st.spinner("Analyzing with Llama 3..."):
            response = ollama.generate(model='llama3', prompt=prompt)
            st.subheader("Summary Result")
            st.write(response['response'])