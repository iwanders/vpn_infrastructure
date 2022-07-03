#!/bin/bash

VPNLAN='172.30.2'

docker run -d -P --restart always --privileged --cap-add=NET_ADMIN --ip $VPNLAN.5 --net vpnlan --name proxy_exposer   -p 4000:4000/tcp  proxy_exposer:latest proxy_exposer


