import streamlit as st
from yt_dlp import YoutubeDL
import os
from dotenv import load_dotenv
from groq import Groq
import whisper
from fpdf import FPDF
from URL_DB import insert_url

# BACKGROUND
def futuristic_bg():
    page_bg = """
    <style>
    /* MAIN APP BACKGROUND */
    .stApp {
        background: radial-gradient(circle at 20% 30%, #0f0f1a, #050509 70%);
        background-attachment: fixed;
        overflow: hidden;
    }

    /* ANIMATED GRADIENT WAVES */
    .stApp::before {
        content: "";
        position: fixed;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: conic-gradient(
            from 180deg at 50% 50%,
            #6a00ff,
            #00eaff,
            #ff00c8,
            #6a00ff
        );
        animation: spin 12s linear infinite;
        filter: blur(140px);
        opacity: 0.18;
        z-index: 0;
    }

    /* FLOATING PARTICLES */
    .stApp::after {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image:
            radial-gradient(circle, rgba(255,255,255,0.15) 2px, transparent 2px),
            radial-gradient(circle, rgba(255,255,255,0.1) 1.5px, transparent 1.5px);
        background-size: 120px 120px, 90px 90px;
        animation: drift 25s linear infinite;
        z-index: 0;
    }

    @keyframes spin {
        from { transform: rotate(0deg); }
        to   { transform: rotate(360deg); }
    }

    @keyframes drift {
        0%   { transform: translate(0px, 0px); }
        50%  { transform: translate(25px, 25px); }
        100% { transform: translate(0px, 0px); }
    }

    /* Content above effects */
    .stApp > * {
        position: relative;
        z-index: 1;
    }
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

futuristic_bg()

# ADDING CUSTOM CSS
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
    flex-direction: column;
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
        VidLense.ai
    </h1>
    <p style="
        font-family: 'Poppins', sans-serif;
        font-size: 18px;
        font-weight: 500;
        color: #00FFF7;
        margin-top: 30px;
        text-align: center;
        opacity: 0.85;
    "><i>
        "AI-powered video insights at a glance"
      </i>
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

st.subheader("User guide 👇")

st.success('''
        👉 Step 1: Paste your YouTube video link in the input box.

        👉 Step 2: Click on Analyze Video.

        👉 Step 3: VidLense.ai fetches the video summary automatically.

        👉 Step 4: Get a concise summary of the video with key points highlighted.

        👉 Step 5: Read the summary and understand the content in seconds.
           
        👉 Step 6: Download the summary as pdf format.
        ''')

st.divider()

# LLM-SET-UP
load_dotenv()

# API KEY FROM ENVIORONMENT (.env) FILE
API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=API_KEY)
def ask_llama(prompt):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role":"user", "content":prompt}
        ]
    )

    return response.choices[0].message.content

# CREATING A PERMANENT FOLDER IN YOUR DIRECTORY (FOR STORING THE AUDIO FORMATED file)
os.makedirs("download_audio_folder", exist_ok=True)

# FUNCTION FOR DOWNLOADING THE AUDIO
def download_audio(url):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "download_audio_folder/audio_yt.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return "download_audio_folder/audio_yt.mp3"

# DOWNLOAD SUMMARY AS PDF
def download_summary(summary_text, filename="summary.pdf"):

    clean_text = summary_text.encode("latin-1", "ignore").decode("latin-1")

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Heading
    pdf.set_font("Arial", "B", 18)
    pdf.cell(0, 10, "Summary", ln=True, align="C")

    pdf.ln(5)

    # Body
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, clean_text)

    pdf.output(filename)
    return filename

# LINK-VERIFICATION
link = st.text_input("Paste your YouTube link here : ")

model = whisper.load_model("base")

if st.button("Analyze Video"):
    st.divider()
    st.markdown("""
        <div style="
            background: rgba(0, 255, 247, 0.08);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-radius: 15px;
            padding: 12px 25px;
            margin-top: 20px;
            margin-bottom: 15px;
            box-shadow: 0 0 18px rgba(0, 255, 247, 0.35);
            color: #00FFF7;
            font-family: 'Poppins', sans-serif;
            font-size: 22px;
            font-weight: 700;
            text-align: center;
            letter-spacing: 1px;
            text-transform: uppercase;
        ">
        SUMMARY
        </div>
        """, unsafe_allow_html=True)

    if link:

        insert_url(link)

        # download the audio
        audio_path = download_audio(link)

        #transcribe audio
        with st.spinner("🤖 LLaMA is analyzing..."):
            result = model.transcribe(audio_path)

        # transcripted text 
        transcript_text = result["text"]

        st.success("Transcription Completed!")

        prompt = f"""
You are an advanced AI video content explainer. Your job is to convert a YouTube video transcript into a **well-structured, clear, long, and highly readable explanation**, just like how a top teacher, analyst, or expert would explain it.

🟦 GENERAL INSTRUCTIONS  
- Understand the video topic (it may be about study, sports, entertainment, motivation, news, technology, tutorials, etc.).  
- Based on the topic, write a **detailed, high-quality explanation**.  
- The output should not be short. Make it **properly detailed** so the reader fully understands the topic, theme, and message of the entire video.  
- Make the output **PDF-ready** with clean formatting.

🟨 WRITE THE OUTPUT IN THE FOLLOWING FORMAT:

--------------------------------------------

📝 1. Overview / Summary
Write a detailed summary (not short).  
Explain the complete message of the video in simple language.  
Add relevant emojis.

--------------------------------------------

# ⭐ 2. Key Highlights 
- Use clean, simple bullet points  
- Mention the most important ideas  
- Add emojis for visual clarity  
- Bold important keywords like **concepts**, **names**, **dates**, **rules**, etc.

--------------------------------------------

# 📘 3. Deep Explanation Section
Explain the full topic in a smooth, easy-to-understand way.  
Write it like a teacher explaining the entire chapter or concept.  
Include:
- Sub-headings  
- Examples  
- Definitions  
- Important notes  
- Step-by-step explanations  
- Logical flow  

This section should be **long, detailed, and complete**.

--------------------------------------------

# 🔍 4. Important Insights / Takeaways
Provide meaningful takeaways based on the type of content.  
Examples:
- For study content → learning concepts  
- For motivation → mindset lessons  
- For sports → performance analysis  
- For entertainment → main narrative  
- For tech → features, tech details, improvements  

--------------------------------------------

# 🧠 5. Final Summary
A short concluding paragraph summarizing everything.

--------------------------------------------

🛑 RULES:
- Do NOT skip anything important from the transcript  
- Do NOT write short outputs  
- Do NOT add filler content  
- Rewrite unclear/noisy transcript parts cleanly  
- Output must be **professional, structured, clean, and highly readable**

--------------------------------------------

Transcript:
{transcript_text}
"""
        ask_llm = ask_llama(prompt)
        st.markdown(f"""
            <div style="
                background: rgba(0, 255, 247, 0.08);
                backdrop-filter: blur(12px);
                -webkit-backdrop-filter: blur(12px);
                border-radius: 20px;
                padding: 25px 30px;
                margin-top: 25px;
                margin-bottom: 25px;
                box-shadow: 0 0 25px rgba(0, 255, 247, 0.35);
                color: #00FFF7;
                font-family: 'Poppins', sans-serif;
                font-size: 16px;
                line-height: 1.6;
                letter-spacing: 0.5px;
            ">
            {ask_llm}
            </div>
            """, unsafe_allow_html=True)

        st.divider()

        st.info("Do you want to download that summary in pdf format ?")

        summary = ask_llm

        # Create PDF
        pdf_path = download_summary(summary)

        # --- DOWNLOAD BUTTON ---
        with open(pdf_path, "rb") as f:
            pdf_data = f.read()

        st.download_button(
            label="📄 Download Summary as PDF",
            data=pdf_data,
            file_name="summary.pdf",
            mime="application/pdf"
        )
        
        st.divider()

    else:

        st.warning("Please paste a video link 😥")