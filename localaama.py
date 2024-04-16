from langchain_core.prompts import ChatPromptTemplate


from langchain_core.output_parsers import StrOutputParser

"""
In essence, parsing acts as a bridge between the LLM's internal representation and the human-readable world.
 It takes the raw output and transforms it into something easily interpreted and used by other components in the Langchain application.
"""

from langchain_community.llms import ollama

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACKING_V2"] = "true" # for langchain tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY") 

## Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "you are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title("Langchain Demo With Llama2 API")
input_text = st.text_input("Search the topic u want")

# ollama Llama2 LLM

from langchain_community.llms import Ollama

llm = Ollama(model="llama2")

output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))

