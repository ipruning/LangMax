from mlx_lm.utils import generate, load
from rich import print

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant.",
    },
    {
        "role": "user",
        "content": "帮我用 Python 写一个函数，这个函数可以计算两个数的和。",
    },
]

model, tokenizer = load("mlx-community/Llama-3.2-3B-Instruct-4bit")

res = generate(
    model,
    tokenizer,
    prompt=tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True),  # type: ignore
    verbose=True,
)

print(res)
