import streamlit as st
import base64


st.set_page_config(layout="wide")

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

<h4 class="animated-text"><i>"Explore Your AI Companion"</i></h4>
""", unsafe_allow_html=True)

# EFFECT
st.markdown("""
<style>

.hover-box {
    position: relative;
    display: inline-block;
    text-align: center;
}
            
.hover-container {
    display: flex;
    justify-content: center;
}


/* IMAGE STYLE */
.hover-box img {
    width: 150px;
    border-radius: 20px;
    transition: 0.35s ease;
    box-shadow: 0 0 12px rgba(0,255,255,0.15);
}

/* LIGHT NEON ON HOVER */
.hover-box:hover img {
    transform: scale(1.07);
    box-shadow: 0 0 18px #00eaff, 0 0 28px rgba(0,234,255,0.6);
}

/* HIDDEN DESCRIPTION */
.hover-info {
    visibility: hidden;
    opacity: 0;
    margin-top: 10px;
    width: 180px;
    background: rgba(0, 255, 250, 0.18);
    color: #00FFF7;
    text-align: center;
    padding: 10px 12px;
    border-radius: 12px;
    transition: opacity 0.35s ease;
    font-size: 13px;
    font-family: 'Poppins', sans-serif;
    border: 1px solid rgba(0, 255, 255, 0.28);
    box-shadow: 0 0 10px rgba(0,255,255,0.25);
}

/* SHOW DESCRIPTION ON HOVER */
.hover-box:hover .hover-info {
    visibility: visible;
    opacity: 1;
}

</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

# ------------------ GEMINI ------------------
with col1:

    def get_base64_image(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()

    img_base64 = get_base64_image(r"C:/Users/abijit/Downloads/Gemini.jpg")

    st.markdown(
    f"""
    <div class="hover-container">
        <div class="hover-box">
            <img src="data:image/jpeg;base64,{img_base64}">
            <div class="hover-info">
            "Gemini is Google's most advanced multimodal AI designed for deep reasoning,
            high-accuracy problem solving, image understanding, and powerful text generation."
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
    )


# ------------------ LLAMA ------------------
with col2:

    def get_base64_image(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()

    img_base64 = get_base64_image(r"C:/Users/abijit/Downloads/llama.jpg")

    st.markdown(
    f"""
    <div class="hover-container">
        <div class="hover-box">
            <img src="data:image/jpeg;base64,{img_base64}">
            <div class="hover-info">
            "LLaMA is Meta’s cutting-edge open-source AI focused on high-speed inference,
            flexibility, and efficient real-time conversational intelligence."
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
    )


# ------------------ MISTRAL ------------------
with col3:

    def get_base64_image(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()

    img_base64 = get_base64_image(r"C:/Users/abijit/Downloads/mistral_ai_logo.jpg")

    st.markdown(
    f"""
    <div class="hover-container">
        <div class="hover-box">
            <img src="data:image/jpeg;base64,{img_base64}">
            <div class="hover-info">
            "Mistral AI delivers extremely fast generation, smart reasoning ability,
            and lightweight performance while maintaining top-tier output quality."
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
    )

st.divider()

st.markdown("""
<style>
.stApp {
    background: linear-gradient(145deg, #000000, #0e1e36, #192a51, #2e4272);
    color: #00FFF7;
}
.about-container {
    backdrop-filter: blur(8px);
    background: rgba(0,0,0,0.25);
    border-radius: 15px;
    padding: 30px 40px;
    margin: 30px auto;
    max-width: 900px;
    box-shadow: 0 0 25px rgba(0, 255, 255, 0.3);
}
.about-title {
    text-align: center;
    font-family: 'Poppins', sans-serif;
    font-size: 48px;
    font-weight: 900;
    color: #00FFF7;
    margin-bottom: 20px;
    text-shadow: 0 0 12px rgba(0,255,255,0.7);
}
.about-text {
    text-align: center;
    font-family: 'Poppins', sans-serif;
    font-size: 18px;
    line-height: 1.8;
    color: #b3eaff;
}
</style>
""", unsafe_allow_html=True)

# About Section
st.markdown("""
<div class="about-container">
    <div class="about-title">What is SmartChat.ai?</div>
    <div class="about-text">
        SmartChat.ai connects you to the next generation of intelligent AIs — 
        <strong>Gemini, LLaMA, and Mistral</strong> — enabling powerful text understanding, 
        image reasoning, and creative solutions at your fingertips. 
        Whether you're brainstorming ideas, solving problems, or exploring AI's capabilities, 
        SmartChat.ai makes interaction intuitive, fast, and futuristic.
    </div>
</div>
""", unsafe_allow_html=True)

# Optional: Features Section
st.markdown("""
<div class="about-container">
    <div class="about-title">Key Features</div>
    <div class="about-text">
        <ul style="list-style-type: disc; padding-left: 20px; text-align: left;">
            <li>Multi-AI selection for diverse responses</li>
            <li>Real-time intelligent conversation</li>
            <li>Advanced reasoning and problem-solving</li>
            <li>Interactive & visually modern interface</li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()

# CREATOR SECTION

st.markdown("""
<div style='text-align:center; margin-top:25px;'>
   <u><h4 style='
        color:white; 
        font-weight:700; 
        font-size:20px;
        text-shadow:0 0 10px rgba(255,255,255,0.5);
    '>
        About creator
    </h4></u>
</div>
""", unsafe_allow_html=True)

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

img_base64 = get_base64_image(r"C:/Users/abijit/OneDrive/Documents/creator.jpg")

st.markdown(f"""
<style>
.creator-container {{
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 80px;
    height: 200px; /* FIXED HEIGHT prevents jumping */
    position: relative;
}}

.creator-circle {{
    width: 150px;
    height: 150px;
    border-radius: 50%;
    overflow: hidden;
    cursor: pointer;
    transition: all 0.7s ease;
    box-shadow: 0 0 10px #00f0ff33;
    flex-shrink: 0;
}}

.creator-circle img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 50%;
    transition: all 0.5s ease;
}}

.creator-circle:hover {{
    box-shadow: 0 0 40px #00f0ff, 0 0 60px #00f0ffaa, 0 0 80px #00f0ff88;
    transform: scale(1.2);
}}

.creator-info-box {{
    width: 0;
    padding: 0;
    margin-left: 50px;
    opacity: 0;
    visibility: hidden;
    background: rgba(0,255,255,0.1);
    border: 1px solid #00f0ff44;
    border-radius: 15px;
    backdrop-filter: blur(8px);
    color: #00fff7;
    font-family: 'Poppins', sans-serif;
    position: absolute; /* prevents pushing the circle */
    left: 180px; /* space after circle */
    top: 0;
    height: 100%; /* aligns vertically */
    transition: all 0.7s ease;
}}

.creator-container:hover .creator-info-box {{
    width: 400px;
    padding: 20px;
    opacity: 1;
    visibility: visible;
}}

.creator-info-box h4 {{
    margin: 0 0 10px 0;
    font-size: 18px;
    font-weight: 700;
}}

.creator-info-box p {{
    font-size: 14px;
    line-height: 1.5;
}}

.social-icons {{
    display: flex;
    justify-content: flex-start;
    gap: 15px;
    margin-top: 15px;
}}

.social-icons img {{
    width: 30px;
    height: 30px;
    border-radius: 50%;
    transition: all 0.3s ease;
}}

.social-icons img:hover {{
    transform: scale(1.3);
    filter: drop-shadow(0 0 12px #00f0ff);
}}
</style>

<div class="creator-container">
    <div class="creator-circle">
        <img src="data:image/jpeg;base64,{img_base64}">
    </div>
    <div class="creator-info-box">
        <h4>Arijit Das</h4>
        <p>
        "BCA student & AI enthusiast. Passionate about Python, AI, backend development, and creating modern web apps.
        Skilled in building interactive UI/UX experiences and integrating multiple AI models for intelligent solutions."
        </p>
        <p>Key Highlights:</p>
        <ul>
            <li>Python & AI integration</li>
            <li>Streamlit modern UI</li>
            <li>Interactive & neon effects</li>
            <li>Backend & API integration</li>
            <li>Multi-AI handling</li>
            <li>3D visuals & animations</li>
            <li>Real-time AI responses</li>
            <li>Social media outreach</li>
            <li>Responsive & mobile-friendly</li>
            <li>Continuous improvement mindset</li>
        </ul>
        <div class="social-icons">
            <a href="https://instagram.com/self.__arijittt" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png">
            </a>
            <a href="https://facebook.com/YOUR_USERNAME" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/124/124010.png">
            </a>
            <a href="https://x.com/YOUR_USERNAME" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/5968/5968933.png">
            </a>
            <a href="https://linkedin.com/in/YOUR_USERNAME" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png">
            </a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
