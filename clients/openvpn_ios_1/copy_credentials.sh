#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
OUR_CN_NAME=$(basename $DIR)

# Set default path, if already set, respect the PKI environment var from
# easyrsa 3
EASYRSA_PKI="${EASYRSA_PKI:-'../../pki/pki'}"

# iOS requires p12 export.
echo "iOS demands the p12 file in the certificate has a password, don't leave it empty."
easyrsa export-p12 $OUR_CN_NAME


# Assume that the name is openvpn_server.
cp $EASYRSA_PKI/private/$OUR_CN_NAME.key client.key
cp $EASYRSA_PKI/issued/$OUR_CN_NAME.crt client.crt
cp $EASYRSA_PKI/ca.crt ca.crt
cp $EASYRSA_PKI/private/$OUR_CN_NAME.p12 client_pkcs.p12

