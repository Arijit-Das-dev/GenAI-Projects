import streamlit as st
import textwrap

def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* FULL BACKGROUND WITH ANIMATED GRADIENT */
    .stApp {
        background: linear-gradient(135deg, #0a0118 0%, #1a0b2e 25%, #2d1b4e 50%, #1a0b2e 75%, #0a0118 100%);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        color: white;
        font-family: 'Inter', sans-serif;
    }
    
    @keyframes gradientShift {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    /* FLOATING PARTICLES EFFECT */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(circle at 20% 30%, rgba(138, 43, 226, 0.15) 0%, transparent 50%),
            radial-gradient(circle at 80% 70%, rgba(75, 0, 130, 0.15) 0%, transparent 50%),
            radial-gradient(circle at 50% 50%, rgba(147, 51, 234, 0.1) 0%, transparent 50%);
        pointer-events: none;
        z-index: 0;
    }

    /* MAIN GLASS CONTAINER */
    .glass-wrapper {
        position: relative;
        background: linear-gradient(135deg, rgba(20, 20, 40, 0.85) 0%, rgba(10, 10, 25, 0.9) 100%);
        border-radius: 32px;
        padding: 60px 70px;
        max-width: 1300px;
        margin: 60px auto;
        border: 1px solid rgba(147, 51, 234, 0.3);
        box-shadow:
            0 8px 32px rgba(138, 43, 226, 0.4),
            0 0 100px rgba(147, 51, 234, 0.2),
            inset 0 0 80px rgba(147, 51, 234, 0.05);
        backdrop-filter: blur(20px);
        transition: all 0.4s ease;
        overflow: hidden;
    }
    
    .glass-wrapper::before {
        content: '';
        position: absolute;
        top: -2px;
        left: -2px;
        right: -2px;
        bottom: -2px;
        background: linear-gradient(45deg, #8b5cf6, #d946ef, #8b5cf6);
        border-radius: 32px;
        z-index: -1;
        opacity: 0;
        transition: opacity 0.4s ease;
        animation: borderGlow 3s ease infinite;
    }
    
    .glass-wrapper:hover::before {
        opacity: 0.6;
    }
    
    @keyframes borderGlow {
        0%, 100% { filter: hue-rotate(0deg); }
        50% { filter: hue-rotate(30deg); }
    }

    /* TITLE WITH GRADIENT */
    .hero-title {
        font-size: 68px;
        font-weight: 700;
        line-height: 1.1;
        margin-bottom: 24px;
        background: linear-gradient(135deg, #ffffff 0%, #e0d4ff 50%, #c4b5fd 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -0.02em;
        animation: titleFloat 3s ease-in-out infinite;
    }
    
    @keyframes titleFloat {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-5px); }
    }
    
    .hero-title .accent {
        background: linear-gradient(135deg, #a78bfa 0%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    /* SUBTEXT */
    .hero-sub {
        font-size: 17px;
        color: #d4d4ff;
        max-width: 600px;
        line-height: 1.8;
        margin-bottom: 45px;
        font-weight: 400;
        opacity: 0.95;
        animation: fadeInUp 1s ease;
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 0.95;
            transform: translateY(0);
        }
    }

    /* FEATURE BADGES */
    .feature-badge {
        display: inline-block;
        background: rgba(167, 139, 250, 0.15);
        border: 1px solid rgba(167, 139, 250, 0.3);
        border-radius: 20px;
        padding: 8px 18px;
        margin: 6px 8px 6px 0;
        font-size: 13px;
        color: #c4b5fd;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .feature-badge:hover {
        background: rgba(167, 139, 250, 0.25);
        border-color: rgba(167, 139, 250, 0.5);
        transform: translateY(-2px);
    }

    /* NEON BUTTON */
    .stButton > button {
        background: linear-gradient(135deg, #8b5cf6 0%, #d946ef 100%);
        color: white;
        border: none;
        border-radius: 16px;
        padding: 16px 40px;
        font-size: 16px;
        font-weight: 600;
        box-shadow: 
            0 0 30px rgba(139, 92, 246, 0.6),
            0 4px 20px rgba(217, 70, 239, 0.4);
        transition: all 0.3s ease;
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        transition: left 0.5s ease;
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }

    .stButton > button:hover {
        box-shadow: 
            0 0 50px rgba(139, 92, 246, 0.9),
            0 8px 30px rgba(217, 70, 239, 0.6);
        transform: translateY(-3px);
    }
    
    .stButton > button:active {
        transform: translateY(-1px);
    }

    /* INPUT FIELDS */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background: rgba(30, 20, 50, 0.6);
        color: white;
        border-radius: 16px;
        border: 1.5px solid rgba(167, 139, 250, 0.3);
        padding: 16px 20px;
        font-size: 15px;
        transition: all 0.3s ease;
        box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.3);
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: rgba(167, 139, 250, 0.7);
        box-shadow: 
            inset 0 2px 8px rgba(0, 0, 0, 0.3),
            0 0 20px rgba(167, 139, 250, 0.4);
        outline: none;
    }
    
    .stTextArea > div > div > textarea {
        min-height: 150px !important;
    }

    /* DECORATIVE ORBS */
    .orb {
        position: absolute;
        border-radius: 50%;
        filter: blur(60px);
        opacity: 0.4;
        pointer-events: none;
        animation: float 8s ease-in-out infinite;
    }
    
    .orb-1 {
        width: 300px;
        height: 300px;
        background: radial-gradient(circle, #8b5cf6, transparent);
        top: -100px;
        right: -100px;
    }
    
    .orb-2 {
        width: 250px;
        height: 250px;
        background: radial-gradient(circle, #d946ef, transparent);
        bottom: -80px;
        left: -80px;
        animation-delay: -4s;
    }
    
    @keyframes float {
        0%, 100% { transform: translate(0, 0) scale(1); }
        33% { transform: translate(30px, -30px) scale(1.1); }
        66% { transform: translate(-20px, 20px) scale(0.9); }
    }

    /* SECTION HEADERS */
    .section-header {
        font-size: 28px;
        font-weight: 600;
        margin: 50px 0 25px 0;
        color: #e0d4ff;
        position: relative;
        padding-left: 20px;
    }
    
    .section-header::before {
        content: '';
        position: absolute;
        left: 0;
        top: 50%;
        transform: translateY(-50%);
        width: 5px;
        height: 30px;
        background: linear-gradient(180deg, #8b5cf6, #d946ef);
        border-radius: 3px;
    }

    /* STATS GRID */
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 20px;
        margin: 30px 0;
    }
    
    .stat-card {
        background: rgba(139, 92, 246, 0.1);
        border: 1px solid rgba(167, 139, 250, 0.3);
        border-radius: 16px;
        padding: 24px;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .stat-card:hover {
        background: rgba(139, 92, 246, 0.15);
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(139, 92, 246, 0.3);
    }
    
    .stat-number {
        font-size: 32px;
        font-weight: 700;
        background: linear-gradient(135deg, #a78bfa, #ec4899);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .stat-label {
        font-size: 14px;
        color: #d4d4ff;
        margin-top: 8px;
    }

    /* SCROLLBAR */
    ::-webkit-scrollbar {
        width: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(10, 10, 25, 0.5);
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #8b5cf6, #d946ef);
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #a78bfa, #ec4899);
    }
    </style>
    """, unsafe_allow_html=True)

def landing_section():
    html = textwrap.dedent("""
<div class="glass-wrapper">
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>   
    <div style="display:flex; justify-content:space-between; align-items:center; position: relative; z-index: 1;">
        <div style="flex: 1;">
            <div class="hero-title">
                Welcome to<br><span class="accent">Jarvis Lab</span>
            </div>                
            <div class="hero-sub">
                Turn your ideas into stunning visuals using AI. Describe your imagination in words 
                and let Jarvis bring it to life. Built for creativity, experimentation, and visual 
                exploration.
            </div>    
            <div style="margin: 35px 0;">
                <span class="feature-badge">🎨 Unlimited Generations</span>
                <span class="feature-badge">⚡ Lightning Fast</span>
                <span class="feature-badge">🔓 No Sign-up Required</span>
                <span class="feature-badge">🎭 Any Style You Imagine</span>
            </div>        
            <div class="stats-grid" style="max-width: 550px; margin-top: 40px;">
                <div class="stat-card">
                    <div class="stat-number">∞</div>
                    <div class="stat-label">Free Generations</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">100%</div>
                    <div class="stat-label">AI Powered</div>
                </div>
            </div>
        </div>
        <div style="width:50px;"></div>
    </div>
</div>
""")

    st.markdown(html, unsafe_allow_html=True)
    return st.button("🚀 Get Started")


def prompt_section():
    st.markdown('<div class="section-header">✨ Create Your Masterpiece</div>', unsafe_allow_html=True)
    
    prompt = st.text_area(
        "Describe your vision",
        placeholder="e.g., A futuristic city at sunset with flying cars, neon lights, and holographic billboards...",
        height=200,
        label_visibility="collapsed"
    )

    generate = st.button("🎨 Generate Image")
    return prompt, generate