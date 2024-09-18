import asyncio
import os
from enum import Enum

from openai import OpenAI
from pydantic import BaseModel
from rich import print

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_BASE_URL"),
)


class SearchType(str, Enum):
    VIDEO = "video"
    EMAIL = "email"
    MISC = "misc"


class Search(BaseModel):
    search_query: str
    search_type: SearchType

    async def execute(self) -> str:
        return f"Burrrrr {self.search_query} {self.search_type}"


class MultiSearch(BaseModel):
    searches: list[Search]

    async def execute(self):
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


async def execute_searches(multi_search: MultiSearch) -> list[str]:
    return await multi_search.execute()


if __name__ == "__main__":
    query = "I am looking for a video on how to cook a pizza. I am also looking for an email on how to cook a pizza. 我还想学习游戏王的卡组怎么组。"
    multi_search = segment_searches(query)
    print(asyncio.run(execute_searches(multi_search)))
