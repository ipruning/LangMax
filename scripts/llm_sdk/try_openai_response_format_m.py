import asyncio
import os
from enum import Enum

from openai import OpenAI
from pydantic import BaseModel
from rich.console import Console

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_BASE_URL"),
)


class Search(BaseModel):
    class Backend(str, Enum):
        VIDEO = "video"
        EMAIL = "email"
        MISC = "misc"

    query: str
    backend: Backend

    async def execute(self) -> str:
        return f"Burrrrr {self.query} {self.backend}"


class MultiSearch(BaseModel):
    searches: list[Search]

    async def execute(self) -> list[str]:
        return await asyncio.gather(*[search.execute() for search in self.searches])


def segment_searches(data: str) -> MultiSearch:
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": f"Consider the data below:\n\n{data}\n\n segment_searches it into multiple search queries",
            },
        ],
        response_format=MultiSearch,
    )

    if completion.choices[0].message.parsed is None:
        raise ValueError("OpenAI SDK returned an invalid structured outputs")

    return completion.choices[0].message.parsed


query = """Hi,
I am looking for a video on how to cook a pizza.
I am also looking for an email on how to cook a pizza.
我还想学游戏王
"""

output = segment_searches(query)


console = Console()
console.print("Segmented Searches:", style="bold")
console.print(output)
console.print("Search Execution Results:", style="bold")
console.print(asyncio.run(output.execute()))
