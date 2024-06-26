#!/bin/bash

export MLX_PATH="$HOME/Databases/Stacks/LLM/MLX/mlx-examples"
export MODEL_PATH="/Volumes/Workspace/Databases/Models/Llama-2-7B"

"$MLX_PATH"/.venv/bin/python "$MLX_PATH"/lora/lora.py \
  --model "$MODEL_PATH"/mlx_llama_weights.npz \
  --tokenizer "$MODEL_PATH"/tokenizer.model \
  --adapter_file "$MODEL_PATH"/adapters.npz \
  --num-tokens 50 \
  --prompt "table: 1-10015132-16
columns: Player, No., Nationality, Position, Years in Toronto, School/Club Team
Q: What is terrence ross' nationality
A: "
