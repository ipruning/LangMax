#!/bin/bash

vastai search offers 'inet_up>=100 inet_down>=500 cpu_cores_effective>=8 reliability>=0.98 num_gpus=1 disk_space>=100 duration>=3' \
  --order 'dlperf_usd-'
