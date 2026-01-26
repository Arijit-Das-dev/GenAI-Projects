import streamlit as st


def render_auth_page(sign_up, log_in):

    st.set_page_config(
        page_title="Account",
        layout="wide"
    )

    # ---------- STYLES ----------
    st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at top left, #1e1b4b, #020617 65%);
        color: white;
    }

    .block-container {
        padding: 3rem 4rem;
    }

    .brand-title {
        font-size: 48px;
        font-weight: 800;
        background: linear-gradient(90deg, #8b5cf6, #22d3ee);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .brand-subtitle {
        font-size: 18px;
        color: #c7d2fe;
        margin: 20px 0 35px 0;
        max-width: 520px;
    }

    .feature {
        display: flex;
        gap: 14px;
        margin-bottom: 18px;
    }

    .feature-icon {
        color: #22d3ee;
        font-size: 20px;
    }

    .feature-text {
        color: #e5e7eb;
        font-size: 15px;
        max-width: 480px;
    }

    .auth-title {
        font-size: 26px;
        font-weight: 600;
        margin-bottom: 25px;
    }

    .stTextInput > div > div > input {
        background: transparent;
        color: white;
        border: none;
        border-bottom: 1px solid rgba(255,255,255,0.35);
        border-radius: 0;
    }

    .stTextInput input::placeholder {
        color: rgba(255,255,255,0.6);
    }

    .stButton button {
        width: 100%;
        border-radius: 30px;
        background: linear-gradient(90deg, #7c3aed, #06b6d4);
        color: white;
        border: none;
        padding: 12px;
        font-size: 15px;
        margin-top: 18px;
    }

    .switch {
        text-align: center;
        margin-top: 18px;
        color: #c7d2fe;
        font-size: 13px;
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------- SESSION STATE ----------
    if "mode" not in st.session_state:
        st.session_state.mode = "Login"

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    # ---------- AFTER LOGIN / SIGNUP ----------
    if st.session_state.logged_in:
        st.markdown("""
        <style>
        .welcome-card {
            max-width: 520px;
            margin: 80px auto;
            padding: 35px;
            border-radius: 22px;
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(14px);
            border: 1px solid rgba(255,255,255,0.15);
            text-align: center;
            box-shadow: 0 20px 40px rgba(0,0,0,0.35);
        }

        .welcome-title {
            font-size: 28px;
            font-weight: 700;
            margin-bottom: 8px;
            background: linear-gradient(90deg, #8b5cf6, #22d3ee);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .welcome-sub {
            font-size: 15px;
            color: #cbd5f5;
            margin-bottom: 28px;
        }

        .chip {
            display: inline-block;
            padding: 6px 14px;
            border-radius: 20px;
            background: rgba(255,255,255,0.12);
            font-size: 13px;
            color: #e5e7eb;
            margin-bottom: 22px;
        }

        .action-btn button {
            width: 100%;
            border-radius: 30px;
            background: linear-gradient(90deg, #7c3aed, #06b6d4);
            color: white;
            border: none;
            padding: 12px;
            font-size: 15px;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="welcome-card">
            <div class="chip">✨ Jarvis AI</div>
            <div class="welcome-title">Welcome, {st.session_state.username}</div>
            <div class="welcome-sub">
                Your AI workspace is prepared and waiting for you.
            </div>
            <div class="welcome-sub">
                You are now all set 🚀
            </div>
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3, col4 ,col5, col6, col7, _, _ = st.columns(9)

        with col4:
            if st.button("Logout"):
                st.session_state.clear()
                st.rerun()
        return

    # ---------- LAYOUT ----------
    left, right = st.columns([1.4, 1])

    # ---------- LEFT (ABOUT) ----------
    with left:

        st.markdown("""
        <style>
        .glass-info-card {
            padding: 45px 40px;
            border-radius: 26px;
            background: rgba(255, 255, 255, 0.07);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255,255,255,0.18);
            box-shadow: 0 25px 55px rgba(0,0,0,0.35);
            max-width: 640px;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="glass-info-card">
            <div class='brand-title'>Jarvis AI</div>
            <div class='brand-subtitle'>
                An intelligent AI assistant built to understand, reason, and automate workflows.
            </div>
            <div class='feature'>
                <div class='feature-icon'>⚡</div>
                <div class='feature-text'>Real-time AI conversations with deep understanding.</div>
            </div>
            <div class='feature'>
                <div class='feature-icon'>🧠</div>
                <div class='feature-text'>Context-aware memory across sessions.</div>
            </div>
            <div class='feature'>
                <div class='feature-icon'>🔐</div>
                <div class='feature-text'>Secure, account-based access with isolated user data</div>
            </div>
            <div class='feature'>
                <div class='feature-icon'>🛠️</div>
                <div class='feature-text'>Designed for tools, automation, and future AI upgrades.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ---------- RIGHT (AUTH) ----------
    with right:
        st.markdown(f"<div class='auth-title'>{st.session_state.mode}</div>", unsafe_allow_html=True)

        username = st.text_input("Username", placeholder="Email or username")
        password = st.text_input("Password", type="password", placeholder="Password")
        
        # ---------- LOGIN ----------
        if st.session_state.mode == "Login":
            if st.button("Sign In"):

                if not username or not password:
                    st.warning("All fields are required")

                else:
                    if log_in(username, password):
                        st.session_state.logged_in = True
                        st.session_state.username = username
                        st.rerun()
                    else:
                        st.error("Invalid username or password")


            st.markdown("<div class='switch'>New to Jarvis AI?</div>", unsafe_allow_html=True)
            if st.button("Create an account"):
                st.session_state.mode = "Signup"
                st.rerun()

        # ---------- SIGNUP ----------
        else:
            
            confirm_password = st.text_input(
                "Confirm Password", type="password", placeholder="Re-enter password"
            )

            email = st.text_input(
                "Email Address", placeholder="Enter your email address"
            )
            ph = st.text_input(
                "Phone number", placeholder="Enter phone number"
            )

            if st.button("Create Account"):

                if not username or not password or not confirm_password:
                    st.warning("All fields are required")

                elif password != confirm_password:
                    st.error("Passwords do not match")

                else:
                    if sign_up(username, password, email, ph):
                        st.session_state.logged_in = True
                        st.session_state.username = username
                        st.rerun()
                    else:
                        st.warning("User already exists")

            # ---------- SWITCH ----------
            st.markdown("<div class='switch'>Already have an account?</div>", unsafe_allow_html=True)
            if st.button("Back to Login"):
                st.session_state.mode = "Login"
                st.rerun()