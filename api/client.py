import requests
import streamlit as st

def get_openai_response(input_text):
    response = requests.post("http://localhost:8000/song/invoke",
                             json={'input':{'topic':input_text}})
    return response.json()['output']['content']


def get_ollama_reponse(input_text):
    response = requests.post("http://localhost:8000/poem/invoke",
                             json={'input':{'topic':input_text}})
    return response.json()['output']

## Streamlit framwrok

st.title("Langchain Demo With Both OpenAI and Llama2")
input_text = st.text_input("Write song on")
input_text1 = st.text_input("Write a poem on")

if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_ollama_reponse(input_text))