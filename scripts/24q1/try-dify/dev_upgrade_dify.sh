#!/usr/bin/env bash

export DIFY_DIR="$HOME"/Coding/dify
export BOT_DIR="$HOME"/Coding/bot
export CONDA_BIN_DIR="$HOME"/.conda/envs/dify/bin
export LOCAL_BIN_DIR="$HOME"/.local/bin

tmux kill-session -t dify || true

cd "$DIFY_DIR" || exit
git checkout deploy/dev
git pull

cd "$DIFY_DIR"/api || exit
"$CONDA_BIN_DIR"/pip install -r requirements.txt
"$CONDA_BIN_DIR"/flask db upgrade

cd "$DIFY_DIR"/web || exit
npm install
npm run build

cd "$BOT_DIR"/scripts || exit
tmuxp load dev_dify.yaml
