import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key="XXXX")

gemini_pro = genai.GenerativeModel("gemini-pro")

prompt = "こんにちは"
response = gemini_pro.generate_content(prompt)
print(response.text)
