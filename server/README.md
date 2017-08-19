These files can be used to run the three docker containers and connect them to
the docker network.

The docker network is defined at the top of most scripts and is called `VPNLAN`,
except for in tinc's [remote_server](tinc/etc/vpn/hosts/remote_server) host
configuration file. If the these containers are to be deployed on more than one
server, and connected to each other through tinc, the `VPNLAN` variable needs to
be changed to ensure that the docker networks are different subnets and the tinc
daemons can expose their respective subnets.

## OpenVPN
The [openvpn/start_openvpn.sh](openvpn/start_openvpn.sh) script can be used to 
start the two OpenVPN containers with the default configuration of one on port
443 using TCP and another one on 1194 using UDP. This script also gives the
containers their static ip addresses on the `VPNLAN`.

[openvpn/bin/opvn_run](openvpn/bin/opvn_run) is the main entrypoint for the 
OpenVPN containers. It adds some genneric options to the OpenVPN configuration.
Pushes the routes to expose the entire VPN network to the clients, sets up the
routing to provide NAT to clients and route traffic aimed for the VPN subnet to
use the tinc daemon's ip as gateway. Finally it checks which part of the subnet
it should claim and on which port / protocol it should bind.

## Tinc
The [tinc/start_tinc.sh](tinc/start_tinc.sh) shows how to start the container
for the tinc daemon.

The main entrypoint for tinc is [tinc/bin/tinc_run](tinc/bin/tinc_run), which
just adds routes to ensure that traffic that reaches the tinc daemon from the
VPN network and is intended at the OpenVPN clients gets routed to the correct
OpenVPN instances. The ip addresses in this file should thus correspond to those
in the OpenVPN start script and their configurations.


## Generic
 * [create_vpnlan.sh](create_vpnlan.sh) can be used to create the docker
    network prior to starting the containers
 * [start.sh](start.sh) and [stop.sh](stop.sh) can be used to start and stop the
    docker containers.

## Credentials
 * [openvpn/copy_credentials.sh](openvpn/copy_credentials.sh) copies the server
    certificate from the PKI directory, should be created prior to deployment
    with the [create_server.sh](../pki/create_server.sh) script.
 * The credentials for the tinc 'server' are created from the tinc
    ['client'](../clients/tinc/) example and should be ran prior to deployment.

