# OpenFOAM

After spinning up an instance, the following steps can be executed to setup a running remote pvserver. This means you will know the \<crusoe-cloud-instance-ip\>

```
export CRUSOE_CLOUD_INSTANCE_IP= <crusoe-cloud-instance-ip>
```

## Script to retrieve and build nvtop

```
ansible-playbook -u root --inventory $CRUSOE_CLOUD_INSTANCE_IP, crusoe-openfoam.yml
```
