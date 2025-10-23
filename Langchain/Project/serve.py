from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
import uvicorn
from dotenv import load_dotenv
from langserve import add_routes
load_dotenv()


groq_api_key = os.getenv("GROQ_API_KEY")
model=ChatGroq(model="openai/gpt-oss-120b",groq_api_key=groq_api_key)


from langchain_core.prompts import ChatPromptTemplate

system_template = "Translate the following into {language}"
prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("user", "{text}")
])

parser=StrOutputParser()

#create chain
chain=prompt_template|model|parser

#App definition
app=FastAPI(title="Langchain",
            version="1.0",
            description="A simple langchain application")
            
add_routes(
    app,
    chain,
    path="/chain"
)

if __name__=="__main__": ##So this is how we start the fastapi application
    uvicorn.run(app,host="0.0.0.0",port=8000) ##running the fastapi application on the port 8000