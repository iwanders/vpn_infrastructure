#!/bin/bash

docker stop fileserver
docker rm fileserver
./build.sh
./start.sh
docker logs fileserver