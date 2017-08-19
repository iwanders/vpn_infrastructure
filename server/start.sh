#!/bin/bash

# Ensure we run from this directory.
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR

./create_vpnlan.sh


echo "Restarting tinc"
cd tinc
./restart.sh
cd ..

echo "Restarting openvpn"
cd openvpn
./restart.sh
cd ..