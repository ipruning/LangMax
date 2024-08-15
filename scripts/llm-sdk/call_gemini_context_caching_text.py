import datetime
import os

import google.generativeai as genai
from dotenv import load_dotenv
from google.generativeai import caching

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

some_long_text = """
"""

cache = caching.CachedContent.create(
    model="models/gemini-1.5-flash-001",
    display_name="some_long_text",
    system_instruction=("You are a helpful assistant."),
    contents=[some_long_text],
    ttl=datetime.timedelta(minutes=5),
)

model = genai.GenerativeModel.from_cached_content(cached_content=cache)

response = model.generate_content("")

print(response.usage_metadata)
print(response.text)
