import os

from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam, ChatCompletionToolParam

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_BASE_URL"),
)


def get_card_price(card_name: str, currency: str) -> float:
    return 100.0


tool: ChatCompletionToolParam = {
    "type": "function",
    "function": {
        "name": "get_card_price",
        "description": "Fetches the price of a given trading card",
        "parameters": {
            "type": "object",
            "properties": {
                "card_name": {
                    "type": "string",
                    "description": "The name of the card to get the price for",
                },
                "currency": {
                    "type": "string",
                    "description": "The currency to return the price in",
                    "enum": ["USD", "EUR"],
                },
            },
            "required": ["card_name", "currency"],
        },
    },
}

tools = [tool]

messages: list[ChatCompletionMessageParam] = [
    {
        "role": "system",
        "content": "You are a helpful assistant that can answer questions about the price of cards.",
    },
    {
        "role": "user",
        "content": "What is the price of the card 'The Mysterious Card'? 我生活在巴黎。",
    },
]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    tools=tools,
    tool_choice="auto",
)

print(response.model_dump_json(indent=2))
