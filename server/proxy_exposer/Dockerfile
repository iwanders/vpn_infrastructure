# Leaner build then Ubunutu
FROM ubuntu:xenial

RUN apt-get update && apt-get install -y net-tools iproute2 socat iptables

ADD ./bin /usr/local/bin
RUN chmod a+x /usr/local/bin/*
