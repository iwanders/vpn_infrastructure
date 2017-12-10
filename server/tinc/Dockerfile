# Leaner build then Ubunutu
FROM ubuntu:trusty

RUN apt-get update && apt-get install -y tinc iptables

ADD ./etc/tinc/ /etc/tinc/


WORKDIR /etc/tinc

ADD ./bin /usr/local/bin
RUN chmod a+x /usr/local/bin/*


