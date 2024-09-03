from banks import Prompt

PROMPT_TEMPLATE = """Write a 500-word blog post on {{ topic }}.
"""

p = Prompt(PROMPT_TEMPLATE)

topic = "retrogame computing"

print(
    p.text(
        {
            "topic": topic,
        }
    )
)
