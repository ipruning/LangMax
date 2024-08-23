import litellm
from dotenv import load_dotenv

load_dotenv()


litellm.callbacks = ["logfire"]

response = litellm.completion(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "Hi 👋 How are you?",
        },
    ],
)
