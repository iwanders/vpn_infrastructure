#!/bin/bash

docker stop fileserver
sleep 1
docker rm fileserver
docker run -d -P --name fileserver -v /home/ivor/http_files/:/usr/share/nginx/html:ro  -v /etc/letsencrypt/:/etc/letsencrypt/:ro -p 8080:443/tcp fileserver:latest
