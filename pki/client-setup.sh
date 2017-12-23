#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

export PATH=$DIR/easy-rsa/easyrsa3/:$PATH
export EASYRSA_PKI=$DIR/client-pki/
mkdir -p $EASYRSA_PKI
