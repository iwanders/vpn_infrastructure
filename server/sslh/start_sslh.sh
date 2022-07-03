#!/bin/bash
VPNLAN='172.30.2'

docker run -d -P --restart always --privileged --cap-add=NET_ADMIN --ip $VPNLAN.7 --net vpnlan --name sslh   -p 443:443/tcp  sslh:latest run_sslh

