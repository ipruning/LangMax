import os

import openai

client = openai.OpenAI(
    base_url="https://api.cerebras.ai/v1/",
    api_key=os.environ.get("CEREBRAS_API_KEY"),
)


prompt = """
Extract from this content:

Vaibhav Gupta
vbv@boundaryml.com
Experience:
- Founder at BoundaryML
- CV Engineer at Google
- CV Engineer at Microsoft
Skills:
- Rust
- C++

Answer in JSON using this schema:
```json
{
  name: string,
  email: string,
  experience: string[],
  skills: string[],
}
```
"""

response = client.chat.completions.create(
    model="llama3.1-70b",
    messages=[
        {
            "role": "user",
            "content": prompt,
        },
    ],
    temperature=1.0,
)

print(response.choices[0].message.content)
