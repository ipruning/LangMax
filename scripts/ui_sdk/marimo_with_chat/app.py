# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo",
# ]
# ///

import marimo

__generated_with = "0.9.10"
app = marimo.App()


@app.cell
def __():
    import marimo as mo

    return (mo,)


@app.cell
def __(mo):
    import os

    os_key = os.environ.get("GOOGLE_AI_API_KEY")

    if os_key is None:
        input_key = mo.ui.text(label="Google AI API key", kind="password")
    else:
        input_key = None
    return input_key, os, os_key


@app.cell
def __(input_key, mo, os_key):
    key = os_key or input_key.value

    mo.stop(
        not key,
        mo.md("Please provide your Google AI API key in the input field."),
    )
    return (key,)


@app.cell
def __(key, mo):
    chatbot = mo.ui.chat(
        mo.ai.llm.google(
            "gemini-1.5-flash-latest",
            system_message="You are a helpful assistant.",
            api_key=key,
        ),
        prompts=[
            "Hello",
            "How are you?",
            "I'm doing great, how about you?",
        ],
    )
    chatbot
    return (chatbot,)


@app.cell(hide_code=True)
def __(mo):
    mo.md("""Access the chatbot's historical messages with `chatbot.value`.""")
    return


@app.cell
def __(chatbot):
    # chatbot.value is the list of chat messages
    chatbot.value
    return


if __name__ == "__main__":
    app.run()
