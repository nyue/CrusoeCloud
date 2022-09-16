#!/bin/sh
apt install -y cmake libncurses5-dev libncursesw5-dev git
cd /tmp
curl -L -O https://github.com/Syllo/nvtop/archive/refs/tags/2.0.3.tar.gz
tar -xf 2.0.3.tar.gz
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/opt/nvtop ../nvtop-2.0.3/
make install

