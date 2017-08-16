#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"


echo "This file copies the client.priv file to /tmp/."
echo "This is necessary because PrivateKeyFile MUST be an absolute path."
cp vpn/client.priv /tmp/client.priv

sudo tincd -c $DIR/vpn/ --pidfile /tmp/tinc_vpn

# debug with
# sudo tincd -c vpn --pidfile /tmp/tinc_vpn --no-detach

