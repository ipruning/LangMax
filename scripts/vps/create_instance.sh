#!/bin/bash

vastai create instance 9754719 \
  --disk 100 \
  --image pytorch/pytorch:latest \
  --onstart-cmd 'bash' \
  --args -c 'git clone --depth 1 https://github.com/ipruning/dotfiles.git ~/dotfiles && source ~/dotfiles/scripts/bootstrap_linux.sh' \
  --direct \
  --ssh
