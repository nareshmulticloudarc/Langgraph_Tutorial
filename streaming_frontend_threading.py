import streamlit as st
from langgraph_streaming_backend import chatbot
from langchain_core.messages import HumanMessage

#************************************************ Session Setup *******************************************
if 'message_history' not in st.session_state:
    st.session_state['message_history']=[]

#************************************************ Sidebar UI *******************************************
st.sidebar.title('LangGraph Chatbot')
st.sidebar.button('New Chat')
st.sidebar.header('My Conversation')

#************************************************ Main UI *******************************************
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input = st.chat_input('Type here ....')

if user_input:
    st.session_state['message_history'].append({'role':'user','content':user_input})
    with st.chat_message(message('user')):
        st.text(user_input)

    CONFIG={'configurable':{'thread_id':'thread-1'}}

    with st.chat_message('assistant'):
        ai_message= st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {'message': [HumanMessage(content=user_input)]},
                config={'configurable':{'thread_id':'thread-1'}},
                stream_mode='messages'
            )
        )