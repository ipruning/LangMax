import os
from typing import List

from openai import OpenAI
from openai.types.chat import (
    ChatCompletionMessage,
    ChatCompletionToolMessageParam,
    ChatCompletionToolParam,
    ChatCompletionUserMessageParam,
)


def send_messages(messages: List) -> ChatCompletionMessage:
    tools: List[ChatCompletionToolParam] = [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get weather of a location, the user should supply a location first",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        }
                    },
                    "required": ["location"],
                },
            },
        },
    ]

    response = client.chat.completions.create(
        model=os.getenv("DEEPSEEK_DEFAULT_MODEL") or "deepseek-chat",
        messages=messages,
        tools=tools,
    )
    return response.choices[0].message


def main():
    global client
    client = OpenAI(
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        base_url=os.getenv("DEEPSEEK_BASE_URL"),
    )

    messages: List = [
        ChatCompletionUserMessageParam(
            role="user",
            content="How's the weather in Hangzhou?",
        )
    ]

    print(f"<User:> {messages[0]['content']}")

    message = send_messages(messages)

    if not message.tool_calls:
        raise ValueError("Failed to get tool call id.")

    tool = message.tool_calls[0]
    tool_call_id = tool.id

    messages.extend(
        [
            message,
            ChatCompletionToolMessageParam(
                role="tool",
                tool_call_id=tool_call_id,
                content="24℃",
            ),
        ]
    )

    message = send_messages(messages)
    print(f"<Model:> {message.content}")
    print("\n")

    for m in messages:
        print(m)


if __name__ == "__main__":
    main()
