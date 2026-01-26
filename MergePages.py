import streamlit as st

home_page = st.Page(
    page="Second Project/About_Page.py",
    title="Home",
    icon=":material/account_circle:",
    url_path="about",
    default= True
)

chat_page = st.Page(
    page="Second Project/Chat_with_AI.py",
    title="Start Chat",
    icon=":material/smart_toy:",
    url_path="chat"
)

pages = [home_page, chat_page]


pg = st.navigation(pages=pages)
pg.run()