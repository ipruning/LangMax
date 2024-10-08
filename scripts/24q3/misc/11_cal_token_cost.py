from tokencost import calculate_prompt_cost

prompt_string = "Hello world"
response = "How may I assist you today?"
model = "gpt-4o"

prompt_cost = calculate_prompt_cost(prompt_string, model)
print(f"Cost: ${prompt_cost}")
