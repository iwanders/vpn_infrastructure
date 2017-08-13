# Leaner build then Ubunutu
FROM ubuntu:xenial

RUN apt-get update && apt-get install -y openvpn iptables

ADD ./etc/openvpn/ /etc/openvpn/

WORKDIR /etc/openvpn

ADD ./bin /usr/local/bin
RUN chmod a+x /usr/local/bin/*
