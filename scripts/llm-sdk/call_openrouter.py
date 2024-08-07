from os import getenv
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(dotenv_path=Path(__file__).resolve().parents[3] / ".env")

OPENROUTER_API_KEY = getenv("api_key_openrouter_pool_001")
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
    model="anthropic/claude-3-haiku",
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        },
    ],
)
print(completion.choices[0].message.content)
