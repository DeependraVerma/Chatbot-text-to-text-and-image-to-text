from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input, image):
    if input != "":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
       
    return response.text

st.set_page_config(page_title="Gemini Image Describer")

st.header("Gemini Application")

input=st.text_input("Input Prompt: ",key="input")

upload_file = st.file_uploader("Choose an image....", type = ["jpg", "jpeg", "png"])
image = ""
if upload_file is not None:
   image = Image.open(upload_file)
   st.image(image, caption = "Upload Image Here", use_column_width = True)


submit = st.button("tell me about the image")

if submit:
   response = get_gemini_response(input,image)
   st.subheader("The response is:")
   st.write(response)