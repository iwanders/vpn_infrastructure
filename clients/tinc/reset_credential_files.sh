#!/bin/bash

echo "Wiping the remote server keys."

echo "" > ../../server/tinc/etc/tinc/vpn/remote_server.priv
sed -i '11,$ d' ../../server/tinc/etc/tinc/vpn/hosts/remote_server
sed -i '11,$ d' vpn/hosts/remote_server

echo "Wiping client keys."
echo "" > vpn/client.priv
sed -i '11,$ d' ../../server/tinc/etc/tinc/vpn/hosts/client
sed -i '11,$ d' vpn/hosts/client