import streamlit as st
from streamlit.components.v1 import html

def style3_MAIN():

    # ---------- Page Config ----------
    st.set_page_config(
        page_title="AI Interface",
        layout="wide"
    )

    # ---------- Custom CSS ----------
    st.markdown("""
    <style>
    /* Background */
    .stApp {
        background: radial-gradient(circle at top, #1b2735, #090a0f);
        font-family: 'Segoe UI', sans-serif;
    }

    /* Top container */
    .top-text {
        text-align: center;
        padding-top: 50px;  /* distance from top */
    }

    /* Heading */
    .ai-heading {
        font-size: 3.2rem;
        font-weight: 600;
        color: #eaeaea;
        letter-spacing: 1px;
        text-shadow: 0 0 20px rgba(0, 255, 255, 0.25);
    }

    /* Sub text */
    .ai-sub {
        font-size: 1.2rem;
        color: #a0aec0;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------- UI ----------
    st.markdown("""
    <div class="top-text">
        <div class="ai-heading">
            How can i assist you today ?
        </div>
        <div class="ai-sub">
            Thinking. Listening. Assisting....
        </div>
    </div>
    """, unsafe_allow_html=True)

def animation():

    st.divider()
    st.set_page_config(layout="centered")

    html("""
<!DOCTYPE html>
<html>
<head>
<style>
html, body {
  margin: 0;
  width: 100%;
  height: 100%;
  background: transparent;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* WRAPPER */
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
}

/* MAIN CIRCLE */
.voice-orb {
  width: 220px;
  height: 220px;
  border-radius: 50%;
  position: relative;
  overflow: hidden;
  background: radial-gradient(circle at 30% 30%,
    #0e1b2e,
    #08121f
  );
  border: 1.5px solid rgba(0, 220, 255, 0.7);
  box-shadow:
    0 0 18px rgba(0, 220, 255, 0.6),
    inset 0 0 30px rgba(0, 220, 255, 0.15);
}

/* PARTICLE WAVES */
.wave {
  position: absolute;
  width: 300%;
  height: 100%;
  top: 45%;
  left: -100%;
  background:
    radial-gradient(circle, rgba(0,255,255,0.8) 1px, transparent 2px),
    radial-gradient(circle, rgba(255,0,200,0.6) 1px, transparent 2px);
  background-size: 12px 12px;
  animation: moveWave 6s linear infinite;
  filter: blur(0.3px);
  opacity: 0.9;
}

.wave.second {
  top: 52%;
  animation-duration: 9s;
  opacity: 0.6;
}

/* CORE */
.core {
  position: absolute;
  inset: 40px;
  border-radius: 50%;
  background: radial-gradient(circle,
    rgba(0,220,255,0.25),
    transparent 70%
  );
}

/* LISTENING TEXT */
.listening {
  font-family: system-ui, sans-serif;
  font-size: 15px;
  letter-spacing: 1px;
  color: rgba(0, 220, 255, 0.9);
  animation: pulseText 2.2s infinite ease-in-out;
}

/* ANIMATIONS */
@keyframes moveWave {
  0% { transform: translateX(0); }
  100% { transform: translateX(33.3%); }
}

@keyframes pulseText {
  0%   { opacity: 1; filter: blur(0px); }
  50%  { opacity: 0.4; filter: blur(2px); }
  100% { opacity: 1; filter: blur(0px); }
}
</style>
</head>

<body>
  <div class="container">
    <div class="voice-orb">
      <div class="wave"></div>
      <div class="wave second"></div>
      <div class="core"></div>
    </div>

    <div class="listening">🎙️ Listening...</div>
  </div>
</body>
</html>
""", height=420)