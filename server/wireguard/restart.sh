#!/bin/bash

docker stop wireguard
docker rm wireguard
./create_image.sh
./start_wireguard.sh
