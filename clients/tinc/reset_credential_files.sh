#!/bin/bash

echo "Wiping the remote server keys."

# Completely clear the private key file.
echo "" > ../../server/tinc/etc/tinc/vpn/remote_server.priv
# Remove all but the first 10 lines from the remote_server host config on the server.
sed -i '11,$ d' ../../server/tinc/etc/tinc/vpn/hosts/remote_server
# Remove all but the first 10 lines from the remote_server host config on the client.
sed -i '11,$ d' vpn/hosts/remote_server

# Idem, but then for the client.
echo "Wiping client keys."
echo "" > vpn/client.priv
sed -i '11,$ d' ../../server/tinc/etc/tinc/vpn/hosts/client
sed -i '11,$ d' vpn/hosts/client