from openai import OpenAI

API_KEY = "ollama"
API_BASE_URL = "http://localhost:11434/v1/"
MODEL = "chatfire/bge-m3:q8_0"

client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)

completion = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "Always answer in rhymes."},
        {"role": "user", "content": "Introduce yourself."},
    ],
    temperature=0.7,
)

print(completion.choices[0].message)
