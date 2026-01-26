from pymongo import MongoClient
import os
from datetime import datetime
from dotenv import load_dotenv
from Frontend_Account import render_auth_page

# ---------- MONGODB SETUP ----------
load_dotenv()
url = os.getenv("MONGODB_URL")

client = MongoClient(url)
db = client["Jarvis_auth_db"]
user_collection = db["users"]

# ---------- USER SIGNUP ----------
def sign_up(username, password, email, ph):

    if not username or not password:
        return False

    if user_collection.find_one({"username": username}):
        return False

    user_collection.insert_one({
        "username": username,
        "password": password,
        "email": email,
        "ph": ph, 
        "created_at": datetime.now()
    })

    return True


# ---------- USER LOGIN ----------
def log_in(username, password):

    user = user_collection.find_one({
        "username": username,
        "password": password
    })

    if user:
        return True
    return False


# ---------- APP ENTRY ----------
render_auth_page(sign_up, log_in)