#!/bin/sh

# Ansible
gnome-terminal --geometry 80x24+0 --profile=CrusoeRecording

# Port
gnome-terminal --geometry 80x24+500 --profile=CrusoeRecording

# pvserver
gnome-terminal --geometry 80x24+1000 --profile=CrusoeRecording

# paraview
$HOME/systems/ParaView/ParaView-5.10.1-MPI-Linux-Python3.9-x86_64/bin/paraview --geometry 1200x1200+1000 &
# $HOME/systems/ParaView/ParaView-5.11.0-RC1-MPI-Linux-Python3.9-x86_64/bin/paraview  --geometry 1200x1200+1000 &

# top
gnome-terminal --geometry 80x48+3100 --profile=CrusoeRecording

# nvtop
gnome-terminal --geometry 80x24+3100+700 --profile=CrusoeRecording
