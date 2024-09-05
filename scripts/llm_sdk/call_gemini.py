import os

import google.generativeai as genai
from rich.console import Console
from rich.panel import Panel


def configure_genai():
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def generate_content(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt, stream=True)
    console = Console()
    for chunk in response:
        console.print(chunk.text, end="")


def display_models_with_method(method):
    console = Console()
    console.print(Panel(f"List of models that support {method}:", expand=False))
    for m in genai.list_models():
        if method in m.supported_generation_methods:
            model_name = m.name
            if method == "generateContent":
                model_info = genai.get_model(model_name)
                console.print(f"[bold]{model_name}[/bold]")
                console.print(f"  Description: {model_info.description}")
                console.print(f"  Version: {model_info.version}")
                console.print()
            else:
                console.print(f"[bold]{model_name}[/bold]")


def main():
    configure_genai()
    generate_content("What is the capital of the moon?")
    display_models_with_method("generateContent")
    display_models_with_method("embedContent")


if __name__ == "__main__":
    main()
