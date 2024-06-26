#!/bin/bash

export LLAMACPP_DIR="$HOME"/Databases/Stacks/LLM/llama.cpp
export GGUF_MODEL_PATH="/Volumes/Workspace/Databases/Models/mistral-7b-instruct-v0.1.Q5_K_M.gguf"

"$LLAMACPP_DIR"/server \
    -m "${GGUF_MODEL_PATH}"
