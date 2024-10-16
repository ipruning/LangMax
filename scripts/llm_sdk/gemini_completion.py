import os

import google.generativeai as genai
from rich.console import Console
from rich.panel import Panel

console = Console()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)


def generate_content(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash-002")
    response = model.generate_content(prompt, stream=True)

    for chunk in response:
        console.print(chunk)


def display_models_with_method(method):
    """
    Display the models that support the given method.

    Examples:
        display_models_with_method("generateContent")
        display_models_with_method("embedContent")
    """
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


if __name__ == "__main__":
    generate_content("What is the capital of the moon? Explain like I'm 5 in 1000 words.")
