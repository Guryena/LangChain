from dotenv import load_dotenv
import sys
import streamlit as st
from langchain_openai import OpenAI

from Study01_langchain import result

load_dotenv()
sys.stdout.reconfigure(encoding="utf-8")

llm = OpenAI()

st.title("ISSUE")

content = st.text_input("최근 이슈", "주제")
st.write(content,"에 대한 최근 이슈입니다.")

if st.button("검색"):
    with st.spinner("Wait for it"):
        result = llm.invoke(content + "사전적 정의를 간단하게 설명해주고, 최신 연구 논문의 결과를 알려줘")
        st.write(result)