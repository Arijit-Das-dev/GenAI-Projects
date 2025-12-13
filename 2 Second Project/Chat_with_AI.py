import streamlit as st

# BACKGROUND COLOUR
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

st.set_page_config(layout="centered")

# --- Chat history ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- CSS for animation ---
st.markdown("""
<style>
@keyframes slideFade {
    0% {
        opacity: 0;
        transform: translateY(20px);
    }
    100% {
        opacity: 1;
        transform: translateY(0px);
    }
}

#welcome-text {
    animation: slideFade 0.8s ease-out forwards;
    font-size: 32px;
    font-weight: 700;
    text-align: center;
    margin-top: 20px;
    color: white;
    text-shadow: 0px 0px 8px rgba(0,0,0,0.35);
}
</style>
""", unsafe_allow_html=True)


# ---------- NEON CSS ----------
st.markdown("""
<style>

:root {
    --neon: #00eaff;
    --neon2: #9c4bff;
}

/* ----------------------------------------------------------
   MODERN STREAMLIT SELECTBOX - UPDATED CLASS (2024+)
---------------------------------------------------------- */
[data-baseweb="select"] > div {
    background-color: #0d0d0d !important;
    border: 1px solid var(--neon) !important;
    border-radius: 10px !important;
    box-shadow: 0px 0px 8px var(--neon) !important;
    transition: 0.3s;
}

[data-baseweb="select"] * {
    color: white !important;
}

[data-baseweb="select"]:hover > div {
    box-shadow: 0px 0px 14px var(--neon), 0px 0px 25px var(--neon2) !important;
    transform: scale(1.03);
}

/* Label for selectbox */
.st-emotion-cache-1lnpu43 {
    color: var(--neon) !important;
    font-weight: 600 !important;
    font-size: 12px !important;
}

/* ----------------------------------------------------------
   NEON BUTTON
---------------------------------------------------------- */
.neon-btn {
    background: linear-gradient(90deg, var(--neon), var(--neon2));
    color: black;
    font-weight: 700;
    padding: 10px 18px;
    border-radius: 10px;
    border: none;
    cursor: pointer;
    width: 100%;
    text-align: center;
    box-shadow: 0px 0px 12px var(--neon);
    transition: 0.25s ease-in-out;
}

.neon-btn:hover {
    box-shadow: 0px 0px 20px var(--neon), 0px 0px 35px var(--neon2);
    transform: scale(1.06);
}

.neon-btn:active {
    transform: scale(0.96);
}

/* Fade animation */
@keyframes fade-slide {
    0% { opacity: 0; transform: translateY(8px); }
    100% { opacity: 1; transform: translateY(0); }
}

.fade-in {
    animation: fade-slide 0.4s ease-out;
}
            
input[type=number] {
    background-color: #0d0d0d !important;
    border: 1px solid var(--neon) !important;
    color: white !important;
    border-radius: 10px !important;
    padding: 6px 10px !important;
    box-shadow: 0px 0px 8px var(--neon) !important;
    transition: 0.3s ease-in-out;
    font-size: 14px !important;
}

input[type=number]:hover {
    box-shadow: 0px 0px 14px var(--neon), 0px 0px 25px var(--neon2) !important;
    transform: scale(1.03);
}

/* ---------- Neon Button ---------- */
.neon-btn {
    background: linear-gradient(90deg, var(--neon), var(--neon2));
    color: white;
    font-weight: 700;
    padding: 10px 18px;
    border-radius: 10px;
    border: none;
    cursor: pointer;
    width: 100%;
    text-align: center;
    box-shadow: 0px 0px 12px var(--neon);
    transition: 0.25s ease-in-out;
}

.neon-btn:hover {
    box-shadow: 0px 0px 20px var(--neon), 0px 0px 35px var(--neon2);
    transform: scale(1.06);
}

.neon-btn:active {
    transform: scale(0.96);
}

</style>
""", unsafe_allow_html=True)


# --- Show welcome text only if no chat yet ---
if len(st.session_state.messages) == 0:
    st.markdown("<div id='welcome-text'>Hey bro 👋<br>Choose your AI model and start chatting!</div>", unsafe_allow_html=True)

st.divider()

# --- Chat interface ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("Type your message...")

if prompt:
    # Add user message
    st.session_state.messages.append(
        {"role": "user", 
         "content": prompt}
    )

    # Rerun to hide welcome text
    st.rerun()

col1, col2, col3 ,col4 = st.columns(4)

with col1:

    model = st.selectbox("Select your model",

    ["Gemini", "LLaMa", "Mistral"],

    index = None

    )

with col2:

    mode = st.selectbox("Select mode",
                 
                  ["Code", "Conversation", "Therapy", "Entertainment"],

                  index = None
                  )

with col3:

    role = st.selectbox("Select Role",
    
    ["Default", "Professional", "Friendly", "Strict", "Teaching mode"],

    index= None

    )

with col4:

    words = st.number_input("Max words: ")

b1, b2, b3, b4, b5 = st.columns(5)

with b3:

    apply = st.markdown("<button class='neon-btn fade-in'>Apply</button>", unsafe_allow_html=True)