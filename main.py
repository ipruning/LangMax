import os
from typing import List, Optional

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

console = Console()

SYSTEM_PROMPT = """
You are an intent recognition assistant.
You need to remember that common trading card games (TCG) include Pokémon TCG, Magic: The Gathering, Yu-Gi-Oh! (YGO), etc.
Your task is to determine whether the user's question is related to these games. You will try your best to identify the user's intent, which may be one or multiple intents, and finally provide a comprehensive judgment. For example, questions related to politics are obviously not relevant.
"""


class Intent(BaseModel):
    """
    Represents an identified intent from the user's query.

    Attributes:
        description (str): The description of the identified intent.
        relevance (float): The relevance score of the intent to TCG (1.0 is the highest).
    """

    description: str
    relevance: float


class IntentRecognition(BaseModel):
    """
    Represents the result of intent recognition from the user's query.

    Attributes:
        intents (List[Intent]): A list of intents identified from the query.
        is_tcg_related (bool): Indicates whether the query is related to TCG.
    """

    intents: List[Intent]
    is_tcg_related: bool


def get_intent(prompt: str) -> Optional[IntentRecognition]:
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        response_format=IntentRecognition,
    )
    return completion.choices[0].message.parsed if completion.choices else None


def print_intent(intent_recognition: Optional[IntentRecognition]) -> None:
    if intent_recognition:
        table = Table(title="Intent Recognition Results")
        table.add_column("Intent", justify="left", style="magenta")
        table.add_column("Relevance", justify="right", style="green")

        for intent in intent_recognition.intents:
            table.add_row(intent.description, f"{intent.relevance:.2f}")

        console.print(table)
        tcg_related_text = Text(f"Is TCG Related: {intent_recognition.is_tcg_related}", style="bold yellow")
        console.print(Panel(tcg_related_text, title="TCG Related Check"))
    else:
        console.print(Panel("No intents identified.", style="bold red", title="Error"))


if __name__ == "__main__":
    test_set = [
        "你的目标是召回 Diversity 和 Quality 都不错的数据，你应该训练多个小模型，每个能贡献一个 F1 不错的指标来过滤，这样来取并，效果就不错。每个小模型只关注召回一个 Domain 的高质量数据。"
        "今天是打牌的好天气么？",
        "教教我政治？",
        "教教我卡牌里的政治要素？我想了解，然后用这些信息构建一个卡组！",
        "能教我打 LOL 么？哎，好难受。",
    ]
    for prompt in test_set:
        print_intent(get_intent(prompt))
