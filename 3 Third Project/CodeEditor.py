import streamlit as st
import Frontend_Editor as ui 
from mistralai import Mistral
from dotenv import load_dotenv
from EditorDB import save_user_code, save_user_query
import uuid
import os

st.set_page_config(layout="wide")
ui.inject_css()

# ---------- Session variables (TOP) ----------
if "user_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

# ---------------- Session State ----------------
if "started" not in st.session_state:
    st.session_state.started = False

userId = st.session_state.user_id

# ---------------- Landing Page ----------------
if not st.session_state.started:
    ui.landing_section1()
    start = ui.landing_section2() # just renders user guide

    # If "Get Started" clicked, update session_state and rerun
    if start:
        st.session_state.started = True
        st.rerun()

else:
    # Editor + chat layout
    col_editor, col_chat = st.columns([5, 4])
    
    with col_editor:
        
        code, submit = ui.code_editor()

        if submit:

            save_user_code(user_id=userId, user_code=code)

            prompt1 = f'''
        You are an expert programmer and code debugger. 
    When given a piece of code, follow these instructions:

    1. Detect the programming language automatically.
    2. Execute a dry-run (simulate code execution mentally).
    3. If there are errors:
    - Show heading: **ERROR** (stylish, bold/italic if possible)
    - Specify the **error message in the style of the language** (Python, Java, C++, etc.)
    - Mention the **line number** causing the error
    - Explain **why the error occurred**
    - Provide **corrected code**
    - Explain what you changed and why
    4. If the code is correct:
    - Show heading: **" CORRECT "** (stylish, bold/italic if possible)
    - Provide the **output of the code**
    - Explain what the code does, line by line if necessary

    Use headings clearly, code blocks for code, and keep explanations concise but informative.

    Here is the user code:        
    {code}
    '''
            # Load environment variables
            load_dotenv()

            # Initialize client
            with Mistral(api_key=os.getenv("MISTRAL_API_KEY", "")) as mistral:
                completion_ = mistral.chat.complete(
                    model="mistral-small-latest",
                    messages=[
                        {"role": "user", "content": prompt1}
                    ],
                    stream=False
                )

            # Extract result
            result1 = completion_.choices[0].message.content

            # Send to UI
            ui.output_box(result1)
    
    with col_chat:

        user_input, send = ui.ai_chat_input()

        if send:

            save_user_query(user_id=userId, user_query=user_input)

            prompt2 = f"""
You are Jarvis, an expert software engineer, debugger, and programming tutor.

You are integrated into a web-based coding platform called "Jarvis Code Editor".
On the left side of the interface, there is a code editor where the user writes or pastes code.
On the right side, there is an AI chat panel (you) that assists the user in real time.

The user will paste a code-related problem. This may include:
- Source code
- Error messages
- Logical issues
- Conceptual doubts
- Expected vs actual output

Your task:

1. Automatically identify the programming language.
2. Clearly understand the user's problem in the context of the code editor.
3. If code or errors are present:
   - Explain the problem in simple, beginner-friendly terms.
   - Point out the exact issue (include line numbers when possible).
   - Provide a corrected or improved solution.
   - Show the final working code.
4. If the question is conceptual:
   - Explain the concept step-by-step.
   - Use simple examples when helpful.
5. Simulate execution (dry run) when applicable:
   - Explain how the code executes.
   - Why the error occurred.
   - Why the correction works.
6. Provide the expected output if applicable.
7. Encourage learning by explaining the logic, not just giving the answer.

Formatting rules:
- Use clear headings: PROBLEM, ANALYSIS, SOLUTION, FIXED CODE, OUTPUT, EXPLANATION.
- Use code blocks for all code.
- Keep responses clear, concise, and practical.
- Avoid unnecessary verbosity.
- Be accurate and supportive, like a personal coding mentor.

here is the user input box message:
{user_input}
"""         
            load_dotenv()
            
            with Mistral(api_key=os.getenv("MISTRAL_API_KEY", "")) as mistral:
                completion_ = mistral.chat.complete(
                    model="mistral-small-latest",
                    messages=[
                        {"role": "user", "content": prompt2}
                    ],
                    stream=False
                )

            result2 = completion_.choices[0].message.content
            
            ui.output_box(result2)