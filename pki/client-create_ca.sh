#!/bin/bash

# Setup the parameters, targetting client-pki
source client-setup.sh

# setup the pki infrastructure
easyrsa init-pki

# build a subca, without a password
easyrsa build-ca nopass subca
