import json
import os

import requests
from openai import OpenAI

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
YOUR_SITE_URL = "https://www.qkvlab.com"
YOUR_APP_NAME = "QKV Lab"

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

completion = client.chat.completions.create(
    extra_headers={
        "HTTP-Referer": YOUR_SITE_URL,
        "X-Title": YOUR_APP_NAME,
    },
    model="google/gemini-flash-1.5",
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        },
    ],
)

# print(completion)

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": f"{YOUR_SITE_URL}",
        "X-Title": f"{YOUR_APP_NAME}",
    },
    data=json.dumps(
        {
            "model": "google/gemini-flash-1.5",
            "messages": [{"role": "user", "content": "What is the meaning of life?"}],
            "stream": True,
        }
    ),
)

print(response.json())
