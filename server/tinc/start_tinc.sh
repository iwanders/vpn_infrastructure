#!/bin/bash

VPNLAN='172.30.2'


docker run -d -P --privileged  --cap-add=NET_ADMIN  --name tinc --net vpnlan --ip $VPNLAN.1 -p 655:655/tcp -p 655:655/udp tinc:latest tinc_run