#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
OUR_CN_NAME=$(basename $DIR)

# Set default path, if already set, respect the PKI environment var from
# easyrsa 3
EASYRSA_CLIENT_PKI="${EASYRSA_CLIENT_PKI:-../../pki/client-pki}"

# copy all the relevant files here
cp $EASYRSA_CLIENT_PKI/private/$OUR_CN_NAME.key client.key
cp $EASYRSA_CLIENT_PKI/issued/$OUR_CN_NAME.crt client.crt
cp $EASYRSA_CLIENT_PKI/ca.crt client-ca.crt

# manually craft the p12, this includes the client-ca and root ca.
echo "iOS demands the p12 file in the certificate has a password, don't leave it empty."
openssl pkcs12 -export -out $OUR_CN_NAME.p12 -inkey client.key -in client.crt -certfile client-ca.crt