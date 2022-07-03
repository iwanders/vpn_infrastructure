#!/bin/bash

docker stop sslh
docker rm sslh
./create_image.sh
./start_sslh.sh
