import streamlit as st
import base64

# BACKGROUND PAGE <-
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

# CHOOSE YOUR AI
import streamlit as st

st.markdown("""
<style>
@keyframes gradientAnimation {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.animated-text {
    text-align: center;
    font-size: 40px;
    font-weight: 800;
    background: linear-gradient(90deg, #FFC300, #00FFF7, #FF4D6D);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradientAnimation 3s ease infinite, bounce 1.5s ease infinite;
}

@keyframes bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}
</style>

<h4 class="animated-text"><i>"Choose your AI"</i></h4>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:

    def get_base64_image(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()

    img_base64 = get_base64_image(r"C:/Users/abijit/Downloads/Gemini.jpg")

    # ---------- IMAGE STYLE ----------
    st.markdown("""
    <style>
    .img-container {
        text-align: center;
        margin-top: 10px;
    }

    .animated-img {
        width: 150px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.4);
        transition: transform 0.4s ease, box-shadow 0.4s ease;
        animation: fadeZoom 0.8s ease;
    }

    .animated-img:hover {
        transform: scale(1.05);
        box-shadow: 0 12px 30px rgba(0,0,0,0.55);
    }

    @keyframes fadeZoom {
        0% { opacity: 0; transform: scale(0.85); }
        100% { opacity: 1; transform: scale(1); }
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------- DISPLAY IMAGE ----------
    st.markdown(
        f"""
        <div class="img-container">
            <img src="data:image/jpeg;base64,{img_base64}" class="animated-img">
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:

    def get_base64_image(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()

    img_base64 = get_base64_image(r"C:/Users/abijit/Downloads/llama.jpg")

    # ---------- IMAGE STYLE ----------
    st.markdown("""
    <style>
    .img-container {
        text-align: center;
        margin-top: 10px;
    }

    .animated-img {
        width: 150px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.4);
        transition: transform 0.4s ease, box-shadow 0.4s ease;
        animation: fadeZoom 0.8s ease;
    }

    .animated-img:hover {
        transform: scale(1.05);
        box-shadow: 0 12px 30px rgba(0,0,0,0.55);
    }

    @keyframes fadeZoom {
        0% { opacity: 0; transform: scale(0.85); }
        100% { opacity: 1; transform: scale(1); }
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------- DISPLAY IMAGE ----------
    st.markdown(
        f"""
        <div class="img-container">
            <img src="data:image/jpeg;base64,{img_base64}" class="animated-img">
        </div>
        """,
        unsafe_allow_html=True
    )    

with col3:

    def get_base64_image(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()

    img_base64 = get_base64_image(r"C:/Users/abijit/Downloads/mistral_ai_logo.jpg")

    # ---------- IMAGE STYLE ----------
    st.markdown("""
    <style>
    .img-container {
        text-align: center;
        margin-top: 10px;
    }

    .animated-img {
        width: 150px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.4);
        transition: transform 0.4s ease, box-shadow 0.4s ease;
        animation: fadeZoom 0.8s ease;
    }

    .animated-img:hover {
        transform: scale(1.05);
        box-shadow: 0 12px 30px rgba(0,0,0,0.55);
    }

    @keyframes fadeZoom {
        0% { opacity: 0; transform: scale(0.85); }
        100% { opacity: 1; transform: scale(1); }
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------- DISPLAY IMAGE ----------
    st.markdown(
        f"""
        <div class="img-container">
            <img src="data:image/jpeg;base64,{img_base64}" class="animated-img">
        </div>
        """,
        unsafe_allow_html=True
    )