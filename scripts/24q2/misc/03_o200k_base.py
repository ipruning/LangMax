import tiktoken
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.text import Text


def display_encoded_tokens(encoding, prompt):
    encoded_prompt = encoding.encode(prompt)
    tokens = [Text(f"{i}: {token}", style="cyan") for i, token in enumerate(encoded_prompt)]

    return Panel(
        Text("\n".join(str(t) for t in tokens), justify="left"),
        title=f"Tokens for '{prompt}' using {encoding.name}",
        border_style="magenta",
    )


def compare_tokenizers(prompts, tokenizers):
    console = Console()
    for prompt in prompts:
        console.print(f"\n[bold]Comparing tokenizers for prompt: '{prompt}'[/bold]")
        panels = []
        for tokenizer_name in tokenizers:
            encoding = (
                tiktoken.encoding_for_model(tokenizer_name)
                if tokenizer_name.startswith("gpt-")
                else tiktoken.get_encoding(tokenizer_name)
            )
            panels.append(display_encoded_tokens(encoding, prompt))

        console.print(Columns(panels))


a1 = """123「23」456
"""

a2 = """[start_of_highlight_term]23[end_of_highlight_term]
"""

a3 = """[ss]23[es]
"""

prompts = [a1, a2, a3]

tokenizers = [
    "cl100k_base",
    "o200k_base",
]

compare_tokenizers(prompts, tokenizers)
