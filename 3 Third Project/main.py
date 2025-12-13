import os
from groq import Groq
from datetime import datetime
import time as t
import numpy as np
import pyttsx3 
import cv2
import requests
import speech_recognition as sr
import streamlit as st
import warnings
import random
from dotenv import load_dotenv
from Frontend_Main import style3_MAIN
from wake_db import insert_wake
from weather_db import insert_weather

# IGNORE WARNING
warnings.filterwarnings("ignore")

# CORE ENGINE 
class CoreEngine:
        
    def maleVoice(self, text): # <- Engine of male assistant

        engine = pyttsx3.init()
        voices = engine.getProperty("voices")
        engine.setProperty("voice",voices[0].id)
        engine.setProperty("volume",20)
        engine.setProperty("rate",175)
        engine.say(text)
        engine.runAndWait()

    ''' speech recognition '''

    # -> ----------- PASSIVE WAKE LISTENING ------------- <-
    def listen_wake_word(self):

        r = sr.Recognizer()
        r.energy_threshold = 400
        r.pause_threshold = 0.8
        r.dynamic_energy_threshold = False

        while True:
            try:
                with sr.Microphone() as source:
                    print("🎧 Listening for wake word...")
                    r.adjust_for_ambient_noise(source, duration=0.5)
                    audio = r.listen(source, timeout=30, phrase_time_limit=5)

                # Recognize speech
                said = r.recognize_google(audio, language='en-in').lower()
                print(f"Detected speech: {said}")

                # Check wake word
                if "jarvis" in said:
                    print("🚀 Wake word detected: JARVIS!!!")
                    return True  # unlocks command mode

            except sr.WaitTimeoutError:
                print("⏳ No wake word for 30 seconds — still listening...")
                continue

            except sr.UnknownValueError:
                print("❌ Wake word not understood — retrying...")
                continue

            except sr.RequestError:
                print("⚠️ Network error — wake word listening needs internet.")
                continue

            except Exception as e:
                print(f"⚠️ Unexpected error: {e}")
                continue

    # -> ----------- ACTIVE COMMAND LISTENING ------------ <-
    def take_command(self):

        r = sr.Recognizer()
        r.energy_threshold = 400
        r.pause_threshold = 0.8
        r.dynamic_energy_threshold = False

        while True:
            try:
                with sr.Microphone() as source:
                    print("🎧 Listening for command...")
                    r.adjust_for_ambient_noise(source, duration=0.5)
                    audio = r.listen(source, timeout=30, phrase_time_limit=25)

                # process after the mic closes
                query = r.recognize_google(audio, language='en-in').lower()
                print(f"You said: {query}")
                return query

            except sr.WaitTimeoutError:
                print("⏳ 30 seconds complete, no sound detected — restarting...")
                continue  # safe, reopens mic in next loop

            except sr.UnknownValueError:
                print("❌ Could not understand audio.")
                return "none"

            except sr.RequestError:
                print("⚠️ Network error.")
                return "none"

            except Exception as e:
                print(f"⚠️ Unexpected error: {e}")
                continue

class Jarvis(CoreEngine):

    def __init__(self):

        load_dotenv()
        API_KEY = os.getenv("GROQ_API_KEY")
        self.client = Groq(api_key=API_KEY)
        self.chat_history = [] # Chat history

    def ask_llama(self, prompt):

        self.chat_history.append({"role": "user", "content": prompt})

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=self.chat_history  # send full chat history
        )

        bot_reply = response.choices[0].message.content

        # Store assistant reply too
        self.chat_history.append({"role": "assistant", "content": bot_reply})

        return bot_reply

    def JarvisRun(self):


        while True:

            user2 = self.take_command().lower()

            if user2 == "none":
                continue

            elif "weather" in user2:

                latitude = 22.57
                longitude = 88.36

                url = (
                    f"https://api.open-meteo.com/v1/forecast?"
                    f"latitude={latitude}&longitude={longitude}"
                    f"&current_weather=true"
                    f"&hourly=relativehumidity_2m,pressure_msl,cloudcover"
                )

                try:
                    response = requests.get(url)
                    data = response.json()

                    # Current weather
                    temperature = data['current_weather']['temperature']
                    windspeed = data['current_weather']['windspeed']
                    winddirection = data['current_weather']['winddirection']
                    weather_code = data['current_weather']['weathercode']

                    # Hourly extra parameters (take index 0 = current hour)
                    humidity = data['hourly']['relativehumidity_2m'][0]
                    pressure = data['hourly']['pressure_msl'][0]
                    cloud_cover = data['hourly']['cloudcover'][0]
                    insert_weather(temperature, windspeed, winddirection, weather_code, humidity, pressure, cloud_cover)

                except Exception as e:

                    print(f"Error : {e}")
                    j.maleVoice(f"{e}")
                
                j.maleVoice(f"Today's temperature is {temperature} degree celsius ")
                j.maleVoice(f"windspeed is {windspeed} kilometre per hour")

            elif "open webcam" in user2:

                self.maleVoice("Openning webcam")
                camera = cv2.VideoCapture(0)

                while True:

                    ret, frame = camera.read()

                    if not ret:

                        j.maleVoice("I think there is a problem")
                        break

                    cv2.imshow("Camera",frame)

                    if cv2.waitKey(1) & 0xFF == ord('a'):

                        j.maleVoice("closing webcam")
                        break

                camera.release()
                cv2.destroyAllWindows()

            elif "exit" in user2:

                self.maleVoice('''Okay sir, i am going to sleep now, if you need anything, just wake me up by saying "hey jarvis" ''')
                break
            
            elif "introduce yourself" in user2:

                self.maleVoice('''Hello there, myself jarvis, i am an advanced Artificial Intelligence language model,
                   thoughtfully trained and  designed to understand, generate, and interact with human language intelligently, i am still under development, tell how can i help you''')

            else:
        
                try:
                    
                    system_prompt = """You are an AI assistant.
                    Always reply in precise answers.
                    Do not use special characters like emojis hashtags symbols.
                    Use simple English.
                    Focus only on what the user asks.
                    Do not add extra explanation.
                    Always maintain clear and direct tone."""

                    final_prompt = f"{system_prompt}\nUser: {user2}\nAssistant:"
                    
                    reply = self.ask_llama(final_prompt)
                    print("Assistant:", reply)
                    self.maleVoice(reply)

                except Exception as e:

                    print("LLM Error:", e)
                    self.maleVoice("I did not hear that properly, tell that again")
                    continue

# Accessing all classes by creating [objects -> CoreEngine -> jarvis]
j = Jarvis()

# Welcome message ->
def greet():

    latitude = 22.57
    longitude = 88.36

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

    try:
       
       response = requests.get(url)
       data = response.json()

       temperature = data['current_weather']['temperature']
       windspeed = data['current_weather']['windspeed']

    except Exception as e:

        print(f"Error : {e}")
        j.maleVoice(f"{e}")

    # TIME CONFIGURATION
    hour = datetime.now().hour

    if 5 <= hour < 12:
        j.maleVoice("Good morning sir. Welcome to a brand-new day. Jarvis and Nova are ready.")
    elif 12 <= hour < 17:
        j.maleVoice("Good afternoon sir. I hope your day is going smoothly.")
    elif 17 <= hour < 21:
        j.maleVoice("Good evening sir, welcome back.")
    else:
        j.maleVoice("Welcome back sir!")

    j.maleVoice(f"Today's temperature is {temperature} degree celsius ")
    j.maleVoice(f"windspeed is {windspeed} kilometre per hour")
    
    j.maleVoice("Tell me how can I assist you?")
    
if __name__ == "__main__":

    greet()

    while True:

        listening_responses = [
            "Yes sir?, i am listening...",
            "I'm here, sir?, tell how can i help you ?",
            "Go ahead sir? i am listening...."
            ]
        
        words = random.choice(listening_responses)

        wake_word = j.listen_wake_word()

        if wake_word:

            insert_wake(wake_word)
            j.maleVoice(words)
            j.JarvisRun()

        else:

            continue