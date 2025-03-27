import streamlit as st
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize Streamlit App
st.title("LangChain Chatbot with Streamlit")

# Initialize Memory for Conversation
memory = ConversationBufferMemory()

# Define a Prompt Template
template = PromptTemplate(
    input_variables=["history", "user_input"],
    template="You are a helpful AI. The conversation history is: {history}\nUser: {user_input}\nAI:"

)

# Initialize LLM
llm = OpenAI(temperature=0.7)

# Create LLM Chain
chain = LLMChain(llm=llm, prompt=template, memory=memory)

# User Input
user_input = st.text_input("Type your message here:")

if user_input:
    # Get response from LangChain
    response = chain.run(user_input)

    # Store in session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    st.session_state.chat_history.append(("User", user_input))
    st.session_state.chat_history.append(("AI", response))

    # Display Chat History
    for role, text in st.session_state.chat_history:
        with st.chat_message(role.lower()):
            st.write(text)

