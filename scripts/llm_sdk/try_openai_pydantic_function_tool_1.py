import json
import os
from enum import Enum

import openai
from pydantic import BaseModel
from rich import print

client = openai.OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_BASE_URL"),
)


class Currency(str, Enum):
    """The currency to get the price in."""

    USD = "USD"
    EUR = "EUR"


class CardPrice(BaseModel):
    """The parameters for the card price."""

    card_name: str
    currency: Currency

    def get(self) -> float:
        print(f"Getting the price of {self.card_name} in {self.currency}")
        return 100.0


class CardPopularity(BaseModel):
    """The parameters for the card popularity."""

    card_name: str

    def get(self) -> int:
        print(f"Getting the popularity of {self.card_name}")
        return 50


messages: list[dict] = [
    {
        "role": "system",
        "content": "你是一个有用的助手。你可以回答有关卡片价格和受欢迎程度的问题。",
    },
    {
        "role": "user",
        "content": "「地」的价格和受欢迎程度是什么？我在巴黎。",
    },
]

response = client.beta.chat.completions.parse(
    model="gpt-4o-mini",
    messages=messages,  # type: ignore
    tools=[
        openai.pydantic_function_tool(CardPrice),
        openai.pydantic_function_tool(CardPopularity),
    ],
)

message = response.choices[0].message
tool_calls = response.choices[0].message.tool_calls

if message is not None:
    messages.append(message.model_dump())

    if tool_calls:
        function_map = {
            "CardPrice": lambda args: CardPrice(**args).get(),
            "CardPopularity": lambda args: CardPopularity(**args).get(),
        }

        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)

            result = function_map.get(function_name, lambda _: "Unknown function")(function_args)

            messages.append(
                {
                    "role": "tool",
                    "content": str(result),
                    "tool_call_id": tool_call.id,
                }
            )

        response = client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=messages,  # type: ignore
            tools=[
                openai.pydantic_function_tool(CardPrice),
                openai.pydantic_function_tool(CardPopularity),
            ],
        )

    print(response.choices[0].message.content)
