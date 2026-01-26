import streamlit as st
from Frontend_All import style1

style1()
# -------------------------------
# NAVIGATION
# -------------------------------
account_page = st.Page("account.py", title="Account", icon=":material/account_circle:")
home_page = st.Page("home.py", title="About", icon=":material/home:", default=True)
main_page = st.Page("main.py", title="Main", icon=":material/smart_toy:")
code_page = st.Page("CodeEditor.py", title="Code", icon=":material/code:")
image_page = st.Page("Image.py", title="Lab", icon=":material/image:")
data_analysis_page = st.Page("Analysis.py", title="Analyst", icon=":material/bar_chart:")
pages = [account_page,home_page, main_page, code_page, image_page, data_analysis_page]

app = st.navigation(pages)
app.run()