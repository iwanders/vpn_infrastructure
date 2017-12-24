#!/bin/bash

# Setup the parameters, targetting client-pki
source client-setup.sh

# setup the pki infrastructure
easyrsa init-pki

# if you want a subca, use this
#~ easyrsa build-ca nopass subca

# found it was easier just to have two separate CA's for the SSL client
# certificates.
easyrsa build-ca nopass
