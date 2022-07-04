#!/bin/bash
VPNLAN='172.30.2'

docker run -d -P --restart always --privileged --cap-add=NET_ADMIN --ip $VPNLAN.8  --net vpnlan --name wireguard   -p 51820:51820/udp  wireguard:latest run_wireguard

