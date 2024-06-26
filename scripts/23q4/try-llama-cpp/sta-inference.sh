#!/bin/bash

export LLAMACPP_DIR="$HOME"/Databases/Stacks/LLM/llama.cpp
export GGUF_MODEL_PATH="/Volumes/Workspace/Databases/Models/mistral-7b-instruct-v0.1.Q5_K_M.gguf"
export PROMPT="I have three apples, I eat two pears, how many apples do I have? Give me ten examples"

"$LLAMACPP_DIR"/main \
    --model "${GGUF_MODEL_PATH}" \
    --prompt "${PROMPT}" \
    --color \
    --escape \
    --temp 0.8 \
    --n-predict 400
