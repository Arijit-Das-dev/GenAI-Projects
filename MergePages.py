import streamlit as st

project5_page = st.Page(
    
        page="Second Project/LoginPage.py",
        title="Login/Signup",
        icon=":material/login:",
        default = True

)

About_page = st.Page(

        page ="Second Project/About_Page.py",
        title = "Home",
        icon = ":material/account_circle:",

)

Project1_page = st.Page(

        page = "Second Project/Chat_with_AI.py",
        title = "Start Chat",
        icon = ":material/smart_toy:"
)


pg = st.navigation(pages=[project5_page, About_page, Project1_page])
pg.run()