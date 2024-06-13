import requests


def query_model(messages, model="gpt-4", new_chat=True, temperature=0.7, max_tokens=150):
    """
    Queries the model via the API and returns the response.

    Args:
        messages (list): A list of message dictionaries to send to the model.
        model (str): The model identifier. Default is 'gpt-4'.
        new_chat (bool): Whether to start a new conversation. Default is True.
        temperature (float): Sampling temperature. Default is 0.7.
        max_tokens (int): Maximum number of tokens in the response. Default is 150.

    Returns:
        response (dict): The response from the model.
    """
    api_url = "http://localhost:8766/v1/chat/completions"
    payload = {
        "messages": messages,
        "model": model,
        "newChat": new_chat,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

    response = requests.post(api_url, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to get response: {response.status_code}"}


# Example usage
if __name__ == "__main__":
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke."},
    ]
    response = query_model(messages)
    print(response)
