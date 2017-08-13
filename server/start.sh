#!/bin/bash

./create_docklan.sh


echo "Restarting tinc"
cd tinc
./restart.sh
cd ..

echo "Restarting openvpn"
cd openvpn
./restart.sh
cd ..