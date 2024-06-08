vastai search offers 'inet_down>=500 cpu_cores_effective>=8 reliability>=0.97 num_gpus=1 disk_space>=50 duration>=3' \
  --order 'dph-' \
  --storage 100

vastai search offers 'inet_down>=500 cpu_cores_effective>=8 reliability>=0.97 num_gpus>=9 disk_space>=50 duration>=3' \
  --order 'dlperf_usd-' \
  --storage 100

# TODO
vastai create instance 9754719 \
  --disk 100 \
  --image pytorch/pytorch:latest \
  --onstart-cmd 'bash' \
  --args -c 'git clone --depth 1 https://github.com/ipruning/dotfiles.git ~/dotfiles && source ~/dotfiles/scripts/bootstrap_linux.sh' \
  --direct \
  --ssh
