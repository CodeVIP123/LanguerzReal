import streamlit as st
from PIL import Image

st.title("What's New?")

takiya = Image.open("C:\\Users\\Dell\\Desktop\\Docs and Compiledlink\\Windows - Languerz\\Docs Website V - 2.3.4.8.0\\pages\\how2.jpg")

st.subheader("Compiler Added!")
st.write("Now, you can write code in a seperate file which's extension must be .lz . \n It will work in the following way-")
st.image(takiya)
st.subheader("All the python functions added in the compiler!")
st.write("You can also use all kinds of modules and functions and functionalities of python , but only in the file not interpreter.")