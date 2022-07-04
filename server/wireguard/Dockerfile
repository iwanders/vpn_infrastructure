FROM ubuntu:20.04
RUN apt-get update
RUN apt-get -y dist-upgrade
RUN rm -rf /var/lib/apt/lists/*
RUN apt-get update; DEBIAN_FRONTEND=noninteractive apt-get --no-install-recommends -yq install wireguard iproute2
RUN apt-get update; DEBIAN_FRONTEND=noninteractive apt-get --no-install-recommends -yq install iptables iputils-ping

ADD ./bin /usr/local/bin
RUN chmod a+x /usr/local/bin/*
