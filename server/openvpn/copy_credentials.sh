#!/bin/bash

# Set default path, if already set, respect the PKI environment var from
# easyrsa 3
EASYRSA_PKI="${EASYRSA_PKI:-'../../pki/pki'}"

# Assume that the name is openvpn_server.
cp $EASYRSA_PKI/private/openvpn_server.key etc/openvpn/server.key
cp $EASYRSA_PKI/issued/openvpn_server.crt etc/openvpn/server.crt
cp $EASYRSA_PKI/ca.crt etc/openvpn/ca.crt
cp $EASYRSA_PKI/dh.pem etc/openvpn/dh2048.pem
