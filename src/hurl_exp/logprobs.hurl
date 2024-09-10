POST https://api.openai.com/v1/chat/completions
Content-Type: application/json
Authorization: Bearer {{OPENAI_API_KEY}}

{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "Hello! My name is "
    }
  ],
  "logprobs": true,
  "top_logprobs": 5
}
