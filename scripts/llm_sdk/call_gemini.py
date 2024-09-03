import os

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")
prompt = "What is the capital of the moon?"

response = model.generate_content(prompt, stream=True)

for chunk in response:
    print(chunk.text, end="")
