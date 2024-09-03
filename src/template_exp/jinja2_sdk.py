from jinja2 import Template

template = """{{ context }}

User: {{ user_input }}

{{ instructions }}
"""

prompt = Template(template).render(
    user_input="Tell me about Python",
    context="You are a helpful AI assistant",
    instructions="Provide a concise explanation",
)

print(prompt)
