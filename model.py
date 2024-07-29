import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

class Model:
    def __init__(self) -> None:
        self.model = genai.GenerativeModel('gemini-1.5-flash-latest')
        
    def get_response(self, user_question):
        prompt = f"""
        You are a knowledgeable assistant specialized in Indian law. Answer the following question in detail:

        {user_question}

        Ensure that your response includes:
        1. An introduction addressing the query.
        2. provide the related articles to the user query
        3. please provide response only for indian laws. if user asked unrelated question instead of indian laws. please tell to ask only on indian law
        ---

        Disclaimer: The information provided is for educational purposes only and does not constitute legal advice. Please consult a qualified lawyer for personalized legal guidance.
        """
        response = self.model.generate_content(prompt)
        return response.text
