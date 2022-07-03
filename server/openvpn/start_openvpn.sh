#!/bin/bash

VPNLAN='172.30.2'

# we don't expose vpnhttps anymore, we use sslh to deal with the exposing.
docker run -d -P --restart always --privileged --cap-add=NET_ADMIN --ip $VPNLAN.3 --net vpnlan --name vpnhttps openvpn:latest ovpn_run --https
docker run -d -P --restart always --privileged --cap-add=NET_ADMIN --ip $VPNLAN.4 --net vpnlan --name vpnudp   --expose=1194/udp -p 1194:1194/udp openvpn:latest ovpn_run --udp



