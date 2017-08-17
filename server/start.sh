#!/bin/bash

./create_vpnlan.sh


echo "Restarting tinc"
cd tinc
./restart.sh
cd ..

echo "Restarting openvpn"
cd openvpn
./restart.sh
cd ..