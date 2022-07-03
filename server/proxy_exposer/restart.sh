#!/bin/bash


docker stop proxy_exposer
docker rm proxy_exposer

./create_image.sh
./start_proxy_exposer.sh
