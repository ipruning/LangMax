from openai import OpenAI

OLLAMA_API_KEY = "ollama"
OLLAMA_API_BASE_URL = "http://localhost:11434/v1/"
OLLAMA_MODEL = "llama3.1:latest"

client = OpenAI(
    base_url=OLLAMA_API_BASE_URL,
    api_key=OLLAMA_API_KEY,
)

completion = client.chat.completions.create(
    model=OLLAMA_MODEL,
    messages=[
        {
            "role": "system",
            "content": "Always answer in rhymes.",
        },
        {
            "role": "user",
            "content": "Introduce yourself.",
        },
    ],
    temperature=1.0,
)

print(completion.choices[0].message.content)
