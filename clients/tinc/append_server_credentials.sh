#!/bin/bash

echo "Overwriting the server.priv file."
cat server.priv > ../../server/tinc/etc/tinc/vpn/remote_server.priv

echo "Appending the server public key to the server configuration."
cat server.pub >> ../../server/tinc/etc/tinc/vpn/hosts/remote_server

echo "Appending the server public key to the client configuration."
cat server.pub >> vpn/hosts/remote_server
