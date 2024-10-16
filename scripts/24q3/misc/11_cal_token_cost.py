import random
import string
import time
from statistics import mean

from tokencost import calculate_all_costs_and_tokens


def cal_completion_cost(prompt: str, completion: str, model: str) -> float:
    result = calculate_all_costs_and_tokens(
        prompt,
        completion,
        model,
    )
    return result["prompt_cost"] + result["completion_cost"]


def generate_random_text(length: int) -> str:
    return "".join(random.choices(string.ascii_letters + string.digits + string.punctuation + " ", k=length))


if __name__ == "__main__":
    input_prompt = generate_random_text(200000)
    model_response = generate_random_text(8000)
    model_name = "gpt-4o-mini"

    execution_durations = []
    total_costs = []

    for _ in range(25):
        start_time = time.time()
        total_cost = cal_completion_cost(input_prompt, model_response, model_name)
        end_time = time.time()

        execution_duration = end_time - start_time
        execution_durations.append(execution_duration)
        total_costs.append(total_cost)

    print("Execution time statistics:")
    print(f"  Mean: {mean(execution_durations):.6f} seconds")
    print(f"  Min: {min(execution_durations):.6f} seconds")
    print(f"  Max: {max(execution_durations):.6f} seconds")
