# server
These files can be used to run the three docker containers on the remote_server.
These containers should be connected to the docker network on this server.

The docker network is defined at the top of most scripts and is called `VPNLAN`,
except for in tinc's [remote_server](tinc/etc/tinc/vpn/hosts/remote_server) host
configuration file. These three containers can be deployed to more than one
server while being part of the same VPN network, the `VPNLAN` subnet must be
changed to guarantee uniqueness throughout the network, the tinc daemons can be
used to allow the nodes on the VPN network to reach each other.

## OpenVPN
The [openvpn/start_openvpn.sh](openvpn/start_openvpn.sh) script can be used to 
start the two OpenVPN containers with the default configuration of one on ~port
443 using TCP~ and another one on 1194 using UDP. This script also gives the
containers their static ip addresses on the `VPNLAN`.

[openvpn/bin/opvn_run](openvpn/bin/ovpn_run) is the main entrypoint for the 
OpenVPN containers. It adds some generic options to the OpenVPN configuration.
It pushes the routes to expose the entire VPN network to the clients, sets up
the routing to provide NAT to clients and route traffic aimed for the VPN subnet
to use the tinc daemon's ip as gateway. Finally it checks which part of the
subnet it should claim for its clients and on which port / protocol it should
bind.

## Tinc
The [tinc/start_tinc.sh](tinc/start_tinc.sh) shows how to start the container
for the tinc daemon.

The main entrypoint for tinc is [tinc/bin/tinc_run](tinc/bin/tinc_run), which
just adds routes to ensure that traffic that reaches the tinc daemon from the
VPN network and is intended at the OpenVPN clients gets routed to the correct
OpenVPN instances. The ip addresses in this file should thus correspond to those
in the OpenVPN start script and their configurations.

## Wireguard
The wireguard server acts in the same way as the openvpn servers. Ran into some problems trying to
make wireguard bounce to an already existing subnet, so it serves just a single IP and then serves
as a gateway and NAT. Routes are added to make this work in both directions and ensure that the
ips that the clients claim can be reached from anywhere on the subnet. As well as the clients being
able to reach any other nodes on the subnet.

## sslh
Sits in front of everything, binds tcp on port 443 and forwards to the appropriate services on
the internal docker lan.




## Helper scripts
 * [create_vpnlan.sh](create_vpnlan.sh) can be used to create the docker
    network prior to starting the containers
 * [start.sh](start.sh) and [stop.sh](stop.sh) can be used to start and stop the
    docker containers.
 * [openvpn/copy_credentials.sh](openvpn/copy_credentials.sh) copies the server
    certificate from the PKI directory in the directory from which the docker
    image is created, it should be created with the
    [create_server.sh](../pki/create_server.sh) script.
 * The credentials for the tinc 'server' are created from the tinc
    ['client'](../clients/tinc/) example, which appends them to the tinc
    'server' files.

