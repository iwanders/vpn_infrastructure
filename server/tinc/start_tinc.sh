#!/bin/bash

VPNLAN='172.30.2'


docker run -d -P --restart always --privileged --cap-add=NET_ADMIN  --name tinc --net vpnlan --ip $VPNLAN.1 -p 443:443/udp tinc:latest tinc_run
