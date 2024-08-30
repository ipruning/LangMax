#!/bin/bash

export MLX_PATH="$HOME/Databases/Stacks/LLM/MLX/mlx-examples"
# export MODEL_PATH="/Volumes/Workspace/Databases/Models/Mistral-7B-v0.1"
export MODEL_PATH="/Users/alex/Databases/Stacks/LLM/MLX/mlx-examples/mistral/Mistral-7B-v0.1"
export PROMPT="I have three apples, I eat two pears, how many apples do I have? I think I have"

"$MLX_PATH"/.venv/bin/python "$MLX_PATH"/mistral/mistral.py \
  --model_path "$MODEL_PATH" \
  --prompt "$PROMPT" \
  --temp 0
