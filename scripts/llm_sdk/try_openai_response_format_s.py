import os
from typing import List

from openai import OpenAI
from pydantic import BaseModel
from rich import print

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class Step(BaseModel):
    step: str


class CoTReasoning(BaseModel):
    reasoning_steps: List[Step]
    final_answer: str


prompt = "1 + 1 = ?"

completion = client.beta.chat.completions.parse(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful reasoning assistant.",
        },
        {
            "role": "user",
            "content": prompt,
        },
    ],
    response_format=CoTReasoning,
)

print(completion.choices[0].message.parsed)

with client.beta.chat.completions.stream(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": prompt,
        },
    ],
    response_format=CoTReasoning,
) as stream:
    for event in stream:
        if event.type == "content.delta":
            print(event.snapshot, flush=True, end="\n")
