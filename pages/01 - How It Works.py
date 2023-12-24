import streamlit as st

st.title("How Languerz works? Not like other interpreters!")
st.subheader("Then, how it works?")
st.markdown("The Languerz interpreter needs a software to run called 'CompiledLink' which comes with it's installer zip. There will be two folders in the zip.\n")
st.markdown("* Windows - Source Code - Languerz\n")
st.markdown("* Languerz\n")
st.markdown("In the Languerz folder, there will be a file called 'CompiledLink.py' or 'CompiledLink.exe'. If it's .py or even .exe you must have python 3.11.5 installed, only then it can run (There will be python 3.11.5 installer in the zip).\n")
st.markdown("CompiledLink basically reads the source code and dumps it into a file called 'Interpreter.py' (It will be created after you run CompiledLink.py file) and you have to run the Interpreter.py file to get the interpreter of Languerz")
st.markdown("The CompiledLink.py code is-")

st.code("""
with open("C:\\Windows - Source Code - Languerzx\\Languerzx.fls", "r") as f:
    code = f.read()

with open("Interpreter.py", "a") as fb:
    fb.write(code)
    """, language="python")
st.warning("Make sure you should cut Source code folder and paste it in the C: drive")
