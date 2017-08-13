#!/bin/bash


source setup.sh

for d in ../clients/*/ ; do
    COMMON_NAME=$(basename $d)
    easyrsa build-client-full "$COMMON_NAME" nopass
done