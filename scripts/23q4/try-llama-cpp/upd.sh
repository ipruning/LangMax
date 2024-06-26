#!/bin/bash

export LLAMACPP_DIR="$HOME"/Databases/Stacks/LLM/llama.cpp

cd "$LLAMACPP_DIR" || exit
git pull
make clean && make
