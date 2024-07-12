POST https://api.openai.com/v1/chat/completions
Content-Type: application/json
Authorization: Bearer {{OPENAI_API_KEY}}

{
  "model": "gpt-4o",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "Hello!"
    }
  ],
  "logprobs": true,
  "top_logprobs": 5
}
