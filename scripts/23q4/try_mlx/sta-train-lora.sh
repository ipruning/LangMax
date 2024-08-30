#!/bin/bash

export MLX_PATH="$HOME/Databases/Stacks/LLM/MLX/mlx-examples"
export MODEL_PATH="/Volumes/Workspace/Databases/Models/Llama-2-7B"

"$MLX_PATH"/.venv/bin/python "$MLX_PATH"/lora/lora.py \
  --model "$MODEL_PATH"/mlx_llama_weights.npz \
  --tokenizer "$MODEL_PATH"/tokenizer.model \
  --train \
  --iters 600 \
  --adapter_file "$MODEL_PATH"/adapters.npz
