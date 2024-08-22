import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

prompt = "你好！"

response = model.generate_content(prompt, stream=True)
for chunk in response:
    print(chunk.text, end="")