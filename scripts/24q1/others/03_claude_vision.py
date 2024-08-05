# 1,100 * 30000 = 33,000,000
# ( 800 * 15 / 1000000 + 300 * 75 / 1000000 ) * 23862 = 633.5361 USD = 4,560.02 CNY
# 33M Tokens
# 2.5M / Day
# 17.5M / Week
# 87.5M / Week
# 22 * 23862 / 60 / 60 / 24 = 6 Day
# 256k * 1000

import base64
import time

import anthropic
import httpx

start_time = time.time()

client = anthropic.Anthropic()

image1_url = ""
image1_media_type = "image/jpeg"
image1_data = base64.b64encode(httpx.get(image1_url).content).decode("utf-8")

message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": image1_media_type,
                        "data": image1_data,
                    },
                },
                {
                    "type": "text",
                    "text": "Describe this image. Which card is this in Yu-Gi-Oh? You can try to reason it out by looking at the picture without reading the text. Say the probability of your judgment.",
                },
            ],
        }
    ],
)

end_time = time.time()

elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")

print(message)
