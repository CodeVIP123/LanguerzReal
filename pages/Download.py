import streamlit as st

st.title("Downloads - Languerz")
with open("C:\\Users\\Dell\\Desktop\\Docs and CompiledLink\\Windows - Languerz\\Docs Website V - 2.3.4.8.0\\Languerz.zip", "rb") as lang:
    st.download_button("Download Languerz.zip for Windows", mime="text/zip", data=lang, file_name="Languerz.zip")