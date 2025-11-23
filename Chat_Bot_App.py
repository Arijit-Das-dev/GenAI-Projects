import streamlit as st

About_page = st.Page(

        page ="Pages/About_Page.py",
        title = "Home",
        icon = ":material/account_circle:",
        default = True
)

Project1_page = st.Page(

        page = "Pages/Chat_with_AI.py",
        title = "Start Chat",
        icon = ":material/smart_toy:"
)

project2_page = st.Page(

        page="Pages/Tools.py",
        title="Tools",
        icon=":material/tools_installation_kit:"
)

Project3_page = st.Page(

        page = "Pages/History.py",
        title= "History",
        icon= ":material/history:"

)

project4_page = st.Page(

        page="Pages/settings.py",
        title="Settings",
        icon=":material/settings:"

)

pg = st.navigation(pages=[About_page, Project1_page, project2_page, Project3_page, project4_page])
pg.run()