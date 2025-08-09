import streamlit as st

st.set_page_config(page_title="Controls Copilot", layout="wide")
st.title("Controls Copilot — Policy→Regulation Gap Finder")

col1, col2 = st.columns(2)
with col1:
    st.file_uploader("Upload Regulation", type=[
                     "pdf", "docx", "txt"], key="reg")
with col2:
    st.file_uploader("Upload Policy", type=["pdf", "docx", "txt"], key="pol")

st.button("Run Analysis", disabled=True)
