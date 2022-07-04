# vpn_infrastructure

> :warning: All these Dockerfiles use super old versions, just use it as a reference.

This repository contains helper scripts I created to help setup my VPN
infrastructure. My goal was to be able to reach a local server behind a
residential router from my [road warriors][road_warrior].

For connecting the Linux based machines in my network I use [tinc][tinc]. Some
road warriors are not capable of running tinc and rely on [OpenVPN][openvpn] to
gain access to the network.

The infrastructure is best explained with a diagram:
![VPN_infrastructure](doc/vpn_infrastructure.png)

The ip addresses and configuration files in this repository should correspond
to the diagram. See the [`server/`](/server) readme for more information.

## Setup
[Docker][docker] is used on the remote server for easy deployment. All files
that are required on the remote server are placed in the server directory.

The clients directory contains example configurations, there is a script 
that generates [`.mobileconfig`][mobileconfig_apple_docs] files. These
configuration files contain a VPN profile for iOS that provides on-demand
functionality. This is a configuration where the the device always tries to
connect and route traffic through the VPN connection.

## License

MIT License, see [LICENSE](LICENSE).

Copyright (c) 2017 Ivor Wanders

[road_warrior]: https://en.wikipedia.org/wiki/Road_warrior_(computing)
[tinc]: https://www.tinc-vpn.org/
[openvpn]: https://openvpn.net/
[docker]: https://www.docker.com/
[mobileconfig_apple_docs]: https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206