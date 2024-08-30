import os
from typing import List, Optional

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class Step(BaseModel):
    step: str


class CoTReasoning(BaseModel):
    step_details: List[Step]
    final_output: str


def get_reasoning(prompt: str) -> Optional[CoTReasoning]:
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
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
    if reasoning and reasoning.step_details:
        for step in reasoning.step_details:
            print(f"Step: {step.step}")
    else:
        print("No steps available.")

    print(f"Final Output: {reasoning.final_output if reasoning else 'No output available.'}")


if __name__ == "__main__":
    prompt = "1 + 1?"
    print_reasoning(get_reasoning(prompt))
