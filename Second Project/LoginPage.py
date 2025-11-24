import streamlit as st


#BACKGROUND COLOUR
st.markdown(
    """
    <style>
    .stApp {
    background: linear-gradient(145deg, #000000, #0e1e36, #192a51, #2e4272);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# WELCOME MESSAGE
st.markdown("""
<style>
@keyframes slideUp {
    0% {
        transform: translateY(40px);
        opacity: 0;
    }
    100% {
        transform: translateY(0px);
        opacity: 1;
    }
}
</style>

<div style="
    display: flex;
    justify-content: center;
    align-items: center;
    animation: slideUp 1.1s ease-out;
">
    <h1 style="
        font-family: 'Poppins', sans-serif;
        font-size: 52px;
        font-weight: 900;
        color:#00FFF7;
        padding: 15px 35px;
        background: rgba(0, 180, 255, 0.15);
        box-shadow: 0px 0px 25px rgba(0, 180, 255, 0.45);
        border-radius: 18px;
        letter-spacing: 1px;
        text-align: center;
        margin: 0;
    ">
        SmartChat.ai
    </h1>
</div>
""", unsafe_allow_html=True)

st.divider()

# Login/ signup
st.markdown("""
<div style="
    backdrop-filter: blur(10px);
    background: rgba(255,255,255,0.1);
    border-radius: 12px;
    padding: 10px 20px;
    text-align: center;
    color: #00eaff;
    font-size: 28px;
    font-weight: bold;
    box-shadow: 0 0 20px rgba(0, 238, 255, 0.3);
">
🔐 Login Portal 🔐
            
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
    text-align: center;
    color: #b3eaff;
    font-size: 18px;
    margin-top: 10px;
    text-shadow: 0 0 10px rgba(0, 238, 255, 0.5);
">
<h4 style="margin: 0;">Login / Signup</h4>
</div>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    /* Style all input boxes */
    input {
        background-color: #1f1f2e !important; /* Change this color */
        color: white !important;              /* Text color */
        border: 2px solid #4b9cd3 !important; /* Border color */
        border-radius: 8px !important;        /* Rounded corners */
        padding: 10px !important;
    }

    /* Style placeholder text */
    input::placeholder {
        color: #b3b3b3 !important;            /* Placeholder color */
    }
    </style>
""", unsafe_allow_html=True)


# NEON INPUTS BOXES
st.markdown("""
<style>

/* Remove the duplicate eye icon */
[data-testid="stPasswordInput"] button {
    display: none;
}

/* Neon blue modern input box */
input[type="text"], input[type="password"] {
    background: #001a33 !important;
    color: cyan !important;
    border: 2px solid cyan !important;
    border-radius: 10px !important;
    padding: 10px !important;
    font-size: 16px !important;
}

/* Placeholder color */
input::placeholder {
    color: #66d9ff !important;
}

</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    username = st.text_input("Enter username")

with col2:

    email = st.text_input("Enter email address")

col3, col4 = st.columns(2)

with col3:

    password = st.text_input("Enter password", type="password")

with col4:

    confirm_pass = st.text_input("Enter confirm password", type="password")


# CREATE ACCOUNT BUTTON STYLE
st.markdown("""
<style>

/* Modern neon button */
.stButton>button {
    background: linear-gradient(90deg, #00c6ff, #0072ff) !important;
    color: white !important;
    padding: 10px 20px !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
    font-size: 16px !important;
    width: 100% !important;
    box-shadow: 0 0 15px rgba(0, 162, 255, 0.5) !important;
    transition: 0.2s ease-in-out !important;
}

/* Hover effect */
.stButton>button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 0 22px rgba(0, 200, 255, 0.85) !important;
}
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col2:
    
    st.markdown("<div style='margin-top: 50px; margin-left: 20px;'>", unsafe_allow_html=True)
    st.button("Create Account")
    st.markdown("</div>", unsafe_allow_html=True)


st.divider()

st.markdown("""
<div style='text-align:center; margin-top:25px;'>
   <u><h4 style='
        color:white; 
        font-weight:700; 
        font-size:20px;
        text-shadow:0 0 10px rgba(255,255,255,0.5);
    '>
        Contact Us
    </h4></u>
</div>
""", unsafe_allow_html=True)

# SOCIAL MEDIA PLATFORM ICONS
st.markdown("""
<div style='text-align:center; margin-top:25px;'>

<style>
.social-icon {
    display: inline-block;
    margin: 0 30px; /* bigger gap between icons */
    transition: all 0.3s ease-in-out;
    border-radius: 50%; /* circle shape */
    overflow: hidden;
    width: 40px;
    height: 40px;
    box-shadow: 0 0 3px rgba(0,0,0,0.4); /* subtle default shadow */
}

.social-icon img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: all 0.3s ease-in-out;
    border-radius: 50%; /* circle image inside container */
}

/* Hover effect: stronger glow + slight scale */
.social-icon:hover img {
    transform: scale(1.2);
    filter: drop-shadow(0 0 12px #00f0ff)
            drop-shadow(0 0 10px #00f0ff)
            drop-shadow(0 0 8px #00f0ff);
}
</style>

<a href='https://instagram.com/self.__arijittt' target='_blank' class='social-icon'>
    <img src='https://cdn-icons-png.flaticon.com/512/2111/2111463.png'>
</a>

<a href='https://facebook.com/YOUR_USERNAME' target='_blank' class='social-icon'>
    <img src='https://cdn-icons-png.flaticon.com/512/124/124010.png'>
</a>

<a href='https://x.com/YOUR_USERNAME' target='_blank' class='social-icon'>
    <img src='https://cdn-icons-png.flaticon.com/512/5968/5968933.png'>
</a>

<a href='https://linkedin.com/in/YOUR_USERNAME' target='_blank' class='social-icon'>
    <img src='https://cdn-icons-png.flaticon.com/512/174/174857.png'>
</a>

</div>
""", unsafe_allow_html=True)