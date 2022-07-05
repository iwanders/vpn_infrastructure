#!/bin/bash

VPNLAN='172.30.2'

# We don't expose vpnhttps anymore, we use sslh to deal with the exposing. Ip is passed in as a second
# argument to allow the route for eth0 to be changed easily.
docker run -d -P --restart always --privileged --cap-add=NET_ADMIN --ip $VPNLAN.3 --net vpnlan --name vpnhttps openvpn:latest ovpn_run --https $VPNLAN.3
docker run -d -P --restart always --privileged --cap-add=NET_ADMIN --ip $VPNLAN.4 --net vpnlan --name vpnudp   --expose=1194/udp -p 1194:1194/udp openvpn:latest ovpn_run --udp  $VPNLAN.4



