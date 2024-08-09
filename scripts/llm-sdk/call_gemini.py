import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro-exp-0801")
model = genai.GenerativeModel("gemini-1.5-flash")

prompt = "你好！"

response = model.generate_content(prompt, stream=True)
for chunk in response:
    print(chunk.text, end="")
