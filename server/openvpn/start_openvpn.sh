#!/bin/bash

DOCKLAN='172.30.2'

docker run -d -P --privileged --cap-add=NET_ADMIN  --ip $DOCKLAN.3 --net docklan --name vpnhttps --expose=443/tcp -p 443:443/tcp openvpn:latest ovpn_run --https
docker run -d -P --privileged --cap-add=NET_ADMIN  --ip $DOCKLAN.4 --net docklan  --name vpnudp --expose=1194/udp -p 1194:1194/udp --cap-add=NET_ADMIN openvpn:latest ovpn_run --udp


