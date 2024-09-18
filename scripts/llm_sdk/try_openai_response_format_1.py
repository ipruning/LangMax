import os
from typing import List, Optional

from openai import OpenAI
from pydantic import BaseModel

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class Step(BaseModel):
    step: str


class CoTReasoning(BaseModel):
    reasoning_steps: List[Step]
    final_answer: str


def get_reasoning(prompt: str) -> Optional[CoTReasoning]:
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
    return completion.choices[0].message.parsed if completion.choices else None


def print_reasoning(reasoning: Optional[CoTReasoning]) -> None:
    if reasoning and reasoning.reasoning_steps:
        for step in reasoning.reasoning_steps:
            print(f"{step.step}")
    else:
        print("No STEPS available.")

    print(f"{reasoning.final_answer if reasoning else 'No ANSWER available.'}")


if __name__ == "__main__":
    prompt = "1 + 1 ="
    print_reasoning(get_reasoning(prompt))
