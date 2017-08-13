#!/bin/bash


docker stop vpnhttps
docker stop vpnudp
docker rm vpnhttps
docker rm vpnudp

./create_image.sh
./start_openvpn.sh
