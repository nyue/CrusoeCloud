# nvtop GPU monitori software

After spinning up an instance, the following steps can be executed to setup a running remote pvserver. This means you will know the \<crusoe-cloud-instance-ip\>

```
export CRUSOE_CLOUD_INSTANCE_IP=<crusoe-cloud-instance-ip>
```

Ensure that any existing IP is not stashed in ssh's known_hosts
```
ssh-keygen -f "$HOME/.ssh/known_hosts" -R $CRUSOE_CLOUD_INSTANCE_IP
```

It is probably easier to have one console window for each step for easier monitoring

## Script to retrieve and build nvtop

```
ansible-playbook -u root --inventory $CRUSOE_CLOUD_INSTANCE_IP, crusoe-nvtop.yml
```

```
ssh root@$CRUSOE_CLOUD_INSTANCE_IP -t /opt/nvtop/bin/nvtop
```

# apt install -y cmake libncurses5-dev libncursesw5-dev git
# mkdir /tmp/build
# cd /tmp/build
# cmake /tmp/nvtop-2.0.3
# make -j 8