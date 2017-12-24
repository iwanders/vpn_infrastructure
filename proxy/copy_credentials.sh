#!/bin/bash

# Set default path, if already set, respect the PKI environment var from
# easyrsa 3
EASYRSA_PKI="${EASYRSA_PKI:-../pki/pki}"
EASYRSA_CLIENT_PKI="${EASYRSA_CLIENT_PKI:-../pki/client-pki}"

# Reuse the server_openvpn keys as an example.
cp $EASYRSA_PKI/private/openvpn_server.key etc/nginx/certs/server.key
cp $EASYRSA_PKI/issued/openvpn_server.crt etc/nginx/certs/server.crt
cp $EASYRSA_PKI/dh.pem etc/nginx/dh2048.pem

# copy the client certificate chain
cp $EASYRSA_CLIENT_PKI/ca.crt etc/nginx/certs/ca.crt
