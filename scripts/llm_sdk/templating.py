from banks import Prompt
from jinja2 import Template

PROMPT_TEMPLATE = """
Write a 500-word blog post on {{ topic }}.
"""
prompt = Template(PROMPT_TEMPLATE).render(
    topic="retrogame computing",
)
print(prompt)

PROMPT_TEMPLATE = """
Write a 500-word blog post on {{ topic }}.
"""
prompt = Prompt(PROMPT_TEMPLATE).text(
    {
        "topic": "retrogame computing",
    }
)
print(prompt)
