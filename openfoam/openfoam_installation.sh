#!/bin/sh
wget -O - https://dl.openfoam.org/gpg.key > /etc/apt/trusted.gpg.d/openfoam.asc
add-apt-repository http://dl.openfoam.org/ubuntu
apt update
apt install -y openfoam10
