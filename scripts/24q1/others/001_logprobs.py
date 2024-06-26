# import os

# import numpy as np
# from IPython.display import HTML, display
# from openai import OpenAI

# client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<your OpenAI API key if not set as env var>"))


# def get_completion(
#     messages: list[dict[str, str]],
#     model: str = "gpt-4",
#     max_tokens=500,
#     temperature=0,
#     stop=None,
#     seed=123,
#     tools=None,
#     logprobs=None,  # whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the content of message..
#     top_logprobs=None,
# ) -> str:
#     params = {
#         "model": model,
#         "messages": messages,
#         "max_tokens": max_tokens,
#         "temperature": temperature,
#         "stop": stop,
#         "seed": seed,
#         "logprobs": logprobs,
#         "top_logprobs": top_logprobs,
#     }
#     if tools:
#         params["tools"] = tools

#     completion = client.chat.completions.create(**params)
#     return completion


# CLASSIFICATION_PROMPT = """You will be given a headline of a news article.
# Classify the article into one of the following categories: Technology, Politics, Sports, and Art.
# Return only the name of the category, and nothing else.
# MAKE SURE your output is one of the four categories stated.
# Article headline: {headline}"""

# headlines = [
#     "Tech Giant Unveils Latest Smartphone Model with Advanced Photo-Editing Features.",
#     "Local Mayor Launches Initiative to Enhance Urban Public Transport.",
#     "Tennis Champion Showcases Hidden Talents in Symphony Orchestra Debut",
# ]

# for headline in headlines:
#     print(f"\nHeadline: {headline}")
#     API_RESPONSE = get_completion(
#         [{"role": "user", "content": CLASSIFICATION_PROMPT.format(headline=headline)}],
#         model="gpt-4",
#         logprobs=True,
#         top_logprobs=2,
#     )
#     top_two_logprobs = API_RESPONSE.choices[0].logprobs.content[0].top_logprobs
#     html_content = ""
#     for i, logprob in enumerate(top_two_logprobs, start=1):
#         html_content += (
#             f"<span style='color: cyan'>Output token {i}:</span> {logprob.token}, "
#             f"<span style='color: darkorange'>logprobs:</span> {logprob.logprob}, "
#             f"<span style='color: magenta'>linear probability:</span> {np.round(np.exp(logprob.logprob)*100,2)}%<br>"
#         )
#     display(HTML(html_content))
#     print("\n")
