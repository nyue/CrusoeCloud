# OpenFOAM

After spinning up an instance, the following steps can be executed to setup a running remote pvserver. This means you will know the \<crusoe-cloud-instance-ip\>

```
export CRUSOE_CLOUD_INSTANCE_IP= <crusoe-cloud-instance-ip>
```

## Script to retrieve and build nvtop

```
ansible-playbook -u root --inventory $CRUSOE_CLOUD_INSTANCE_IP, crusoe-openfoam.yml
```

## Setup to run example
```
mkdir -p $FOAM_RUN
cd $FOAM_RUN
cp -r $FOAM_TUTORIALS/incompressible/simpleFoam/pitzDaily .
cd pitzDaily
blockMesh
simpleFoam
foamToVTK
```

```
ssh root@$CRUSOE_CLOUD_INSTANCE_IP /opt/paraviewopenfoam56/bin/pvserver
```

## Resources

https://openfoam.org/download/10-ubuntu/

