import streamlit as st

def style2_HOME():

    # --- Page Config ---
    st.set_page_config(
        page_title="Jarvis AI - About",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # --- CSS Styling ---
    st.markdown("""
    <style>
    /* App background: deep navy top → lighter navy bottom */
    .stApp {
        background: linear-gradient(180deg, #02061a, #071433, #0c1f4d, #112b66);
        background-size: 400% 400%;
        animation: gradientBG 18s ease infinite;
        color: #e0e0e0;
        font-family: 'Poppins', sans-serif;
        padding: 40px;
    }

    @keyframes gradientBG {
        0% {background-position: 50% 0%;}
        50% {background-position: 50% 100%;}
        100% {background-position: 50% 0%;}
    }


    /* Hero Section */
    .hero {
        text-align: center;
        margin-bottom: 40px;
    }
    .hero h1 {
        font-size: 56px;
        color: #ffffff;
        margin-bottom: 10px;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.7);
    }
    .hero h3 {
        font-size: 24px;
        color: #a0c0ff;
        margin-bottom: 20px;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.6);
    }
    /* About paragraph under hero */
    .hero p {
        font-size: 18px;
        color: #c0c0c0;
        line-height: 1.7;
        max-width: 900px;
        margin: 0 auto 50px auto;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.5);
    }

    /* Section headings */
    h2 {
        font-size: 36px;
        color: #ffffff;
        margin-top: 50px;
        margin-bottom: 15px;
        border-bottom: 2px solid #ffffff30;
        padding-bottom: 8px;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.5);
    }

    /* Feature cards grid */
    .features {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        justify-content: center;
        margin-top: 30px; /* spacing under divider */
    }
    .feature-card {
        background-color: #0d1a40;
        padding: 25px;
        border-radius: 14px;
        width: 300px;
        transition: transform 0.3s, box-shadow 0.3s;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }
    .feature-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 25px rgba(0,0,0,0.5);
    }
    .feature-card h3 {
        margin-top: 0;
        margin-bottom: 15px;
        font-size: 24px;
        color: #a0c0ff;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.5);
    }
    .feature-card p {
        font-size: 16px;
        color: #d0d0d0;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.4);
    }

    /* User guide containers */
    .user-guide {
        display: flex;
        flex-direction: column;
        gap: 25px;
        margin-top: 20px;
    }
    .guide-container {
        background-color: #102240;
        padding: 25px;
        border-radius: 20px;
        border-left: 6px solid #a0c0ff;
        box-shadow: 0 4px 12px rgba(0,0,0,0.5);
        transition: transform 0.2s;
    }
    .guide-container:hover {
        transform: translateY(-3px);
    }
    .guide-container p {
        margin: 0;
        font-size: 18px;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.4);
    }

    /* Social media icons */
    .social-icons {
        text-align: center;
        margin-top: 40px;
    }
    .social-icons img {
        width: 45px;
        margin: 0 15px;
        transition: transform 0.3s;
    }
    .social-icons img:hover {
        transform: scale(1.2);
    }
    </style>
    """, unsafe_allow_html=True)

    # --- Hero Section with descriptive about text ---
    st.markdown("""
    <div class="hero">
    <h1>Jarvis AI</h1>
    <h3><i>"Your Voice-Powered AI Companion"</i></h3>
    <p>Jarvis AI is a next-generation voice-powered assistant powered by large language models (LLMs). 
    It listens to your commands in audio format and responds intelligently in natural audio, 
    making interactions seamless and human-like. Ask anything, anytime, and let Jarvis AI assist you.</p>
    </div>
    """, unsafe_allow_html=True)

    # --- Features Section ---
    st.markdown("<h2>Key Features</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="features">
    <div class="feature-card">
    <h3>🎙️ Audio Command & Response</h3>
    <p>Give commands via your voice, and Jarvis AI will respond naturally in audio format, enabling hands-free interaction.</p>
    </div>

    <div class="feature-card">
    <h3>💡 Ask Anything</h3>
    <p>Ask general knowledge questions, instructions, or seek advice. Jarvis AI provides accurate responses instantly.</p>
    </div>

    <div class="feature-card">
    <h3>⚡ Intelligent Conversation</h3>
    <p>Jarvis AI understands context, handles multi-turn conversations, and provides coherent replies for realistic AI interaction.</p>
    </div>
    </div>
    """, unsafe_allow_html=True)

    # --- User Guide Section ---
    st.markdown("<h2>User Guide</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="user-guide">
    <div class="guide-container">
    <p>1. Just press the Main page button on sidebar, Jarvis will automatically respond to your all commands.</p>
    </div>
    <div class="guide-container">
    <p>2. Jarvis AI processes your audio and responds back in natural voice.</p>
    </div>
    <div class="guide-container">
    <p>3. Ask anything—from general queries to instructions.</p>
    </div>
    <div class="guide-container">
    <p>4. Ensure your microphone works for the best experience.</p>
    </div>
    <div class="guide-container">
    <p>5. Enjoy a seamless, hands-free AI interaction!</p>
    </div>
    </div>
    """, unsafe_allow_html=True)

    # --- Social Media Section ---
    st.markdown("<h2>Connect With Me</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="social-icons">
    <a href="https://www.instagram.com/self.__arijittt" target="_blank">
    <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/instagram.svg"></a>
    <a href="https://www.linkedin.com/in/your-profile" target="_blank">
    <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/linkedin.svg"></a>
    <a href="https://github.com/Arijit-Das-dev" target="_blank">
    <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/github.svg"></a>
    <a href="https://www.facebook.com/your-profile" target="_blank">
    <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/facebook.svg"></a>
    </div>
    """, unsafe_allow_html=True)
