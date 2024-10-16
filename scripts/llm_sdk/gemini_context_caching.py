import datetime
import os

import google.generativeai as genai
from google.generativeai import caching

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

some_long_prompt = """
"""

some_query_prompt = """
"""

cache = caching.CachedContent.create(
    model="models/gemini-1.5-flash-001",
    display_name="long_text_identifier",
    system_instruction=("You are a helpful assistant."),
    contents=[some_long_prompt],
    ttl=datetime.timedelta(minutes=5),
)

model = genai.GenerativeModel.from_cached_content(cached_content=cache)

response = model.generate_content(some_query_prompt)

print(response.usage_metadata)
print(response.text)
