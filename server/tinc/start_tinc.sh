#!/bin/bash

DOCKLAN='172.30.2'

docker stop tinc
sleep 1 
docker rm tinc
sleep 1 
docker run -d -P --privileged  --cap-add=NET_ADMIN  --name tinc --net docklan --ip $DOCKLAN.1 -p 655:655/tcp -p 655:655/udp tinc:latest tinc_run -t