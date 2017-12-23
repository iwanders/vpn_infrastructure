#!/bin/bash

# ensure this folder exists, otherwise issues..
mkdir -p /tmp/www/

# run the proxy and expose it on port 443.
docker run -d -P -v /tmp/www:/var/www/html --name nginx_proxy -p 443:443/tcp nginx_proxy:latest
