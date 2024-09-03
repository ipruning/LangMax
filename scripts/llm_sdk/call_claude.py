import os

from anthropic import Anthropic

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

res = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=256,
    messages=[
        {
            "role": "user",
            "content": "What flavors are used in Dr. Pepper?",
        }
    ],
)
print(res)
