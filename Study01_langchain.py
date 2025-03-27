from dotenv import load_dotenv
load_dotenv() # load api key info
import sys
from langchain_openai import OpenAI

# print(f"API KEY : {os.environ['OPENAI_API_KEY']}")
sys.stdout.reconfigure(encoding="utf-8")

llm = OpenAI()
#Question to OpenAI
result = llm.invoke("")

#Answer from OpenAI
print(result)
