import streamlit as st
from model import GenaiModel

model = GenaiModel()

st.title("Gemini Chat Bot")
st.write("Hi there ! how can i help you ?")


if "message" not in st.session_state:
    st.session_state.message = []

for i in st.session_state.message:
    with st.chat_message(i["role"]):
        st.markdown(i["msg"])

user_input = st.chat_input("Ask anything....")

if user_input:

    st.session_state.message.append({
        "role":"user",
        "msg":user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):

        with st.spinner("Thinking...."):
            ai_response = model.query_response(query=user_input)

            st.markdown(ai_response)

    st.session_state.message.append({
        "role":"assistant",
        "msg":ai_response
    })