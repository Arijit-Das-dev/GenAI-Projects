import streamlit as st

def style1():

    st.markdown("""
    <style>
    /* Sidebar background with gradient */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f2027, #203a43, #2c5364); /* AI-style gradient */
        color: #ffffff;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Sidebar navigation title with divider */
    [data-testid="stSidebarNav"]::before {
        content: "🤖 JARVIS AI";
        font-size: 22px;
        font-weight: 700;
        display: block;
        padding: 16px 14px;
        border-bottom: 2px solid #ffffff70; /* semi-transparent divider */
        margin-bottom: 12px;
        letter-spacing: 1px;
    }

    /* Sidebar links hover effect */
    [data-testid="stSidebarNav"] div[role="button"]:hover {
        background-color: #ffffff20; /* subtle hover */
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)