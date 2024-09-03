#!/bin/bash

vastai search offers 'inet_up>=100 inet_down>=500 cpu_cores_effective>=8 reliability>=0.98 num_gpus=1 disk_space>=100 duration>=3' \
  --order 'dlperf_usd-'

vastai create instance 9754719 \
  --disk 100 \
  --image pytorch/pytorch:latest \
  --onstart-cmd 'bash' \
  --args -c 'git clone --depth 1 https://github.com/ipruning/dotfiles.git ~/dotfiles && source ~/dotfiles/scripts/bootstrap_linux.sh' \
  --direct \
  --ssh
