#!/bin/bash

docker stop nginx_proxy
docker rm nginx_proxy
./create_image.sh
./start_proxy.sh
