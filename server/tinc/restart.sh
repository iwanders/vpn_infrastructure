#!/bin/bash

docker stop tinc
docker rm tinc
./create_image.sh
./start_tinc.sh