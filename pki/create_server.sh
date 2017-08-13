#!/bin/bash


source setup.sh

SERVER_CERT_COMMON_NAME='openvpn_server'

easyrsa build-server-full "$SERVER_CERT_COMMON_NAME" nopass
easyrsa gen-dh