import os
from fastapi import FastAPI
from fastapi import Request
from langchain_core.output_parsers import StrOutputParser
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

open_ai_key = os.getenv("OPENAI")
os.environ["OPENAI_API_KEY"] = open_ai_key

llm = OpenAI()
app = FastAPI()
output_parser = StrOutputParser()

prompt_template = PromptTemplate(
    input_variables=["query"],
    template="Given the following question, provide a logical reasoning-based answer: {query}"
)

chain = LLMChain(llm =llm ,prompt = prompt_template,output_parser = output_parser)

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/ask")
async def ask_question(query: str):
    result = chain.invoke({"query": query})
    return {"response": result['text']}

