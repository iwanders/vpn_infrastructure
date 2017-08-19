#!/bin/bash

VPNLAN='172.30.2'

docker run -d -P --privileged --cap-add=NET_ADMIN  --ip $VPNLAN.3 --net vpnlan --name vpnhttps --expose=443/tcp -p 443:443/tcp openvpn:latest ovpn_run --https
docker run -d -P --privileged --cap-add=NET_ADMIN  --ip $VPNLAN.4 --net vpnlan  --name vpnudp --expose=1194/udp -p 1194:1194/udp openvpn:latest ovpn_run --udp


