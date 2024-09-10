from banks import Prompt

PROMPT_TEMPLATE = """
Write a 500-word blog post on {{ topic }}.
"""

prompt = Prompt(PROMPT_TEMPLATE).text(
    {
        "topic": "retrogame computing",
    }
)

print(prompt)
