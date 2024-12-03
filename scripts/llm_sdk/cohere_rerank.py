import base64

import cohere
import requests

co = cohere.ClientV2()  # type: ignore

image = requests.get("https://cohere.com/favicon-32x32.png")
stringified_buffer = base64.b64encode(image.content).decode("utf-8")
content_type = image.headers["Content-Type"]
image_base64 = f"data:{content_type};base64,{stringified_buffer}"
response = co.embed(
    model="embed-multilingual-v3.0",
    input_type="image",
    embedding_types=["float"],
    images=[image_base64],
)
print(response)
