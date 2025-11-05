import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# with st.chat_message('user'):
#     st.text('Hi')

# with st.chat_message('assistant'):
#     st.text('How can i help you?')

# with st.chat_message('user'):
#     st.text('My name is Naresh')

# user_input = st.chat_input("Type here...")

# if user_input:
#     st.text(user_input)

OpenAI.api_key= os.getenv('OPENAI_API_KEY')
# if not OpenAI.api_key:
#     st.error("Error: OpenAI API key is missing!")
# else:
#     st.success("API key loaded successfully.")

CONFIG = {'configurable': {'thread_id':'thread-1'}}

if 'message_history' not in st.session_state:
    st.session_state['message_history']=[]

message_history=[]

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

#{'role': 'user','content':'Hi'}
user_input = st.chat_input("Type here ...")

if user_input:
    st.session_state['message_history'].append({'role':'user','content':user_input})
    with st.chat_message('user'):
        st.text(user_input)
    
    response = chatbot.invoke({'messages':[HumanMessage(content=user_input)]}, config=CONFIG)
    ai_message= response['messages'][-1].content

    st.session_state['message_history'].append({'role':'assistant','content':ai_message})
    with st.chat_message('assistant'):
        st.text(ai_message)