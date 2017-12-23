#!/bin/bash

# source the original ca.
source setup.sh

# import the request from the client-pki folder as 'client-ca'
easyrsa import-req ./client-pki/reqs/ca.req client-ca

# Sign the 'client-ca' shortname.
easyrsa sign-req ca client-ca

# copy the now signed certificate to the client-pki infrastructure such that it
# can be used to create certificates.
cp ./pki/issued/client-ca.crt ./client-pki/ca.crt


# Need this later, this contains the client-ca and the original root ca,
# creating the 'entire chain'.
cp ./pki/issued/client-ca.crt ./client-pki/client-ca-with-root-ca.crt
cat ./pki/ca.crt >> ./client-pki/client-ca-with-root-ca.crt
