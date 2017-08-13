#!/bin/bash

DOCKLAN='172.30.2'

#~ docker network create --subnet 172.30.2.0/24 --gateway 172.30.2.1 docklan
# ok, at the time of writing there is NO way to set the gateway for the network
# to an ip that is owned by a container on the network.

# If no gateway is specified, docker creates the bridge interface with the
# first ip address in the range, so effectively preventing use of 172.30.2.1.
# We assign it to 172.30.2.254, which is inside the range, but unused.

# Also, https://github.com/docker/compose/issues/4366 means setting the gateway
# from a docker compose file is deprecated.
docker network create --subnet $DOCKLAN.0/24  --gateway $DOCKLAN.254 docklan
