from dotenv import load_dotenv
from google import genai
import os

class GenaiModel:

    def __init__(self):

        load_dotenv()

        self.API_KEY = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    def modelPrompt(self, query):

        with open("prompt.txt", "r", encoding="utf-8") as f:

            system_prompt = f.read()

        self.prompt = f"""

        {system_prompt}

        user query : {query}

        """

        return self.prompt
    

    def query_response(self, query):

        self.modelPrompt(query=query)

        response = self.API_KEY.models.generate_content(

            model= "gemini-3-flash-preview",
            contents = self.prompt

        )

        return response.text