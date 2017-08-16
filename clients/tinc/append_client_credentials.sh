#!/bin/bash

echo "Overwriting the client.priv file."
cat client.priv > vpn/client.priv

echo "Appending the public key to the client configuration."
cat client.pub >> vpn/hosts/client

echo "Appending the public key to the server configuration."
cat client.pub >> ../../server/tinc/etc/tinc/vpn/hosts/client