#!/bin/bash

export SPACE_NAME="TheBloke/Nous-Hermes-2-SOLAR-10.7B-GGUF" # TheBloke/Yi-6B-GGUF
export MODEL_NAME="nous-hermes-2-solar-10.7b.Q5_K_M.gguf"   # yi-6b.Q5_K_M.gguf
export MODELS_DIR="/Volumes/Workspace/Databases/Models"     # /Volumes/Workspace/Databases/Models

huggingface-cli download "${SPACE_NAME}" "${MODEL_NAME}" \
    --local-dir "${MODELS_DIR}" \
    --local-dir-use-symlinks False
