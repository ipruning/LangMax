import os

from openai import OpenAI
from rich import print

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

print(completion)

completion = client.chat.completions.create(
    model="google/gemini-flash-1.5",
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        },
    ],
    stream=True,
)

for chunk in completion:
    print(chunk.choices[0].delta.content)
