#!/bin/sh
wget -O - https://dl.openfoam.org/gpg.key > /etc/apt/trusted.gpg.d/openfoam.asc
add-apt-repository http://dl.openfoam.org/ubuntu
apt update
apt install -y openfoam10
echo ". /opt/openfoam10/etc/bashrc" >> $HOME/.bashrc
# Create openfoam user
# Some examples require a non-root user to build and run
adduser --disabled-password --gecos "" openfoam
mkdir ~openfoam/.ssh
chown openfoam.openfoam ~openfoam/.ssh
chmod go-rwx ~openfoam/.ssh
cp $HOME/.ssh/authorized_keys ~openfoam/.ssh/
chown openfoam.openfoam ~openfoam/.ssh/authorized_keys
su - openfoam -c 'echo ". /opt/openfoam10/etc/bashrc" >> $HOME/.bashrc'

