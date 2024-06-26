import os
from pathlib import Path

import anthropic
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path(__file__).resolve().parents[3] / ".private.env")
api_key_anthropic = os.getenv("api_key_anthropic_edu_pool_002")

client = anthropic.Anthropic(
    api_key=api_key_anthropic,
)

message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0.0,
    system="Respond only in Yoda-speak.",
    messages=[{"role": "user", "content": "How are you today?"}],
)

print(message.content)
