import sys
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

#LangChain Expression Language (LCEL)

load_dotenv()
sys.stdout.reconfigure(encoding="utf-8")

prompt = ChatPromptTemplate.from_template("Please tell about subject : {topic}")
llm = ChatOpenAI()
output_parser = StrOutputParser()

chain = prompt | llm | output_parser
# response = chain.invoke({"topic" : "블랙홀 최근 이슈"})
response = chain.invoke({"topic" : "암흑물질 최근 이슈"})

print(response)
