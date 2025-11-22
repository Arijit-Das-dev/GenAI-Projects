import streamlit as st
import google.generativeai as genai
import fitz
import pymupdf as ppdf
import os
import re


# UI -> STREAMLIT

st.markdown("""
<style>
.header-row {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 25px;
    margin-top: -20px;
}
.app-title {
    font-size: 46px;
    font-weight: 800;
    color: white;
}
.score-circle {
    width: 75px;
    height: 75px;
    border-radius: 50%;
    background: radial-gradient(circle, #7cffcb, #74f2ce, #3793ff);
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 22px;
    font-weight: 900;
    color: white;
    box-shadow: 0 0 18px rgba(0,0,0,0.4);
    animation: popIn 0.7s ease-out;
}
@keyframes popIn {
    0% { transform: scale(0.2); opacity: 0; }
    60% { transform: scale(1.25); opacity: 1; }
    100% { transform: scale(1); }
}
</style>
""", unsafe_allow_html=True)

row = st.container()
with row:
    col1, col2, col3 = st.columns([1, 2, 1])  # middle column is larger
    col2.markdown("<div class='app-title'>SmartCV.ai 😃</div>", unsafe_allow_html=True)
    score_placeholder = col3.empty()



st.markdown(
    """
    <style>
    .stApp {
       background: linear-gradient(120deg, #000000, #3a0ca3, #7209b7);
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown("""
    <style>
    .center-title {
        text-align: center;
        font-size: 40px;
        color: white;
        font-weight: 700;
        margin-top: -40px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <h6 style='text-align: center; color: #d0d0d0; margin-top: -10px;'>
        <i>"Analyze your resume with AI-powered precision"</i>
    </h6>
""", unsafe_allow_html=True)

st.divider()

# Extracting text from pdf
def extract_text_from_pdf(pdf_path):

    doc = fitz.open(pdf_path)
    full_text = ""

    for page in doc:

        text = page.get_text()
        full_text += text + "\n"

    doc.close()
    return full_text

st.markdown("""
    <style>
    .center-title {
        text-align: center;
        font-size: 40px;
        color: white;
        font-weight: 700;
        margin-top: -40px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h5 class='center-title'>Upload your Resume below 🚀 </h5>", unsafe_allow_html=True)


uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

# Sidebar: History
st.sidebar.title("Uploaded Resumes History")

# Initialize session state for history
if "file_history" not in st.session_state:
    st.session_state.file_history = []

# When user uploads a file
if uploaded_file is not None:
    file_name = uploaded_file.name

    # Save uploaded PDF temporarily
    with open(file_name, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Add to history if not already there
    if file_name not in st.session_state.file_history:
        st.session_state.file_history.append(file_name)

# Display history in sidebar
if st.session_state.file_history:
    for idx, fname in enumerate(st.session_state.file_history, 1):
        st.sidebar.write(f"{idx}. {fname}")


st.divider()

# UPLOADING FILE.pdf
if uploaded_file is not None:

    st.markdown("""
    <style>
    .center-title {
        text-align: center;
        font-size: 40px;
        color: white;
        font-weight: 700;
        margin-top: -40px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h5 class='center-title'>Summary of your Resume 😎 </h5>", unsafe_allow_html=True)

     
    file_name = uploaded_file.name

    # Save uploaded PDF temporarily
    with open(file_name, "wb") as f:
        f.write(uploaded_file.getbuffer())

    extracted_text = extract_text_from_pdf(file_name)
    
    st.code(extracted_text)


    st.divider()

    st.markdown("""
    <style>
    .center-title {
        text-align: center;
        font-size: 40px;
        color: white;
        font-weight: 700;
        margin-top: -40px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h5 class='center-title'>Improvements you should follow 😁 </h5>", unsafe_allow_html=True)


    # SETTING UP LLM -> [Gemini-2.0-flash]
    os.environ["GRPC_VERBOSITY"] = "NONE"
    os.environ["GRPC_TRACE"] = ""

    #API KEY
    API_KEY = 'API_KEY'

    #authentication
    genai.configure(api_key=API_KEY)

    #selecting the model
    model = genai.GenerativeModel('gemini-2.0-flash')

    #giving command to the model to start the chat
    chat = model.start_chat()

    prompt = f"""

        You are a professional ATS-grade Resume Analyzer AI.

        Analyze the following resume and return the results in a clean, structured, and unique format.

        Provide the output in this exact format:

        🎯 **Overall Resume Score:** <score out of 100>

        📌 **Summary (3–5 lines):**
        - A short, crisp summary of the candidate
        - Mention strengths
        - Highlight major gaps

        🛠️ **Key Improvements Needed:**
        - Bullet point improvements
        - Be specific and avoid generic advice
        - Mention missing skills, formatting issues, and ATS problems

        📂 **Skill Match Evaluation (based on standard industry roles):**
        - Technical Skills:
        - Soft Skills:
        - Missing but Recommended Skills:

        📄 **Section Quality Check (Rate each out of 10):**
        - Summary:
        - Skills:
        - Experience:
        - Education:
        - Projects:

        🧪 **ATS Compatibility Review:**
        - Formatting Issues:
        - Keyword Issues:
        - Readability issues:

        Finally, give a short one-line verdict like:
        "Overall, this resume is moderately strong and can be made interview-ready with the suggested changes."

        ---  
        Here is the resume content to analyze:
        {extracted_text}

"""

    # --- LLM RESPONSE ---
    response = chat.send_message(prompt) 
    reply = response.candidates[0].content.parts[0].text
    clean_reply = reply.replace("*", "")
    st.code(clean_reply)

    score_match = re.search(r"Overall Resume Score:\s*(\d+)", clean_reply)
    score_ = int(score_match.group(1)) if score_match else None

    if score_ is not None:
        score_placeholder.markdown(
            f"<div class='score-circle'>{score_}/100</div>",
            unsafe_allow_html=True
        )
