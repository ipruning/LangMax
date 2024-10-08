import os

from braintrust import init_logger, traced, wrap_openai
from openai import OpenAI

# You just need to initialize this, and `@traced` will automatically log to it.
# In more advanced cases (see below), you can initialize spans directly from the logger.
logger = init_logger(project="Say Hi Bot")

client = wrap_openai(OpenAI(api_key=os.environ["OPENAI_API_KEY"]))


@traced
def some_llm_function(input):
    return client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Classify the following text as a question or a statement.",
            },
            {
                "role": "user",
                "content": input,
            },
        ],
        model="gpt-4o",
    )


def my_route_handler(req):
    return some_llm_function(req.body)


if __name__ == "__main__":
    # Create a mock request object or use your actual request object
    class MockRequest:
        def __init__(self, body):
            self.body = body

    # Use the mock request when calling the handler
    my_route_handler(MockRequest("Hello, world!"))
