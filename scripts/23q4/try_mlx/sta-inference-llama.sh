#!/bin/bash

export MLX_PATH="$HOME/Databases/Stacks/LLM/MLX/mlx-examples"
export MODEL_PATH="/Volumes/Workspace/Databases/Models/Llama-2-7B"
export PROMPT="I have three apples, I eat two pears, how many apples do I have? I think I have"

"$MLX_PATH"/.venv/bin/python "$MLX_PATH"/llama/llama.py "$MODEL_PATH"/mlx_llama_weights.npz "$MODEL_PATH"/tokenizer.model "$PROMPT"
