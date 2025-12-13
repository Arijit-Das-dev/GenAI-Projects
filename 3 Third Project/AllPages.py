import streamlit as st
from Frontend_All import style1

style1()

home_page = st.Page(
    page="home.py",
    title="🏡 About",
    default=True
)

main_page = st.Page(
    page="main.py",
    title="🔰 Main",
)

pages = [home_page, main_page]

app = st.navigation(pages)
app.run()
