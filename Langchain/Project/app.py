import os 
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")


##Prompt Template
prompt=ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistant that can answer questions about the context provided."),
    ("user","Question:{question}")

])


##streamlit Framework
st.title('Langchain Application Based on Context Retrieval')
input_text=st.text_input("What do you have in your mind today?")

llm=ChatOpenAI(model="gpt-4o-mini")

output_parser=StrOutputParser()

#Creating a chain
chain=prompt|llm|output_parser


if input_text:
    response=chain.invoke({"question":input_text})
    st.write(response)