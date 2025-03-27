import sys

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChanin
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding="utf-8")

load_dotenv()
llm = ChatOpenAI()

prompt = PromptTemplate(
    input_variables = ["topic"],
    template = "Write a short summary about {topic}"
)

#create chain
chain = LLMChanin(llm = llm, prompt = prompt)

#run chain
response = chain.run("Artificial Intelligence")
print(f"Generated Response \n{response}")

