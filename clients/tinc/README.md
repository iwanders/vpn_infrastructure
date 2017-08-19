#tinc

This client example is a bit of an odd one, because [tinc][tinc] does not
discern between client and server nodes.

The example 'client' configuration here shows how to configure a linux machine
to simply join the tinc network by connecting to the `remote_server` that's
running the tinc configuration provided in the [server](../../server/tinc/)
folder. This example does not expose a subnet to the tinc network but merely
joins it and ensures the entire tinc network is accessible.

It is intended to be run from this directory, this can be done by starting it
with the [start_tinc.sh](start_tinc.sh) script.

## Credentials
Tinc uses RSA keys for security. For two nodes in the network to connect to each
other they should have each others public key, in tinc the configuration for a
node is in the same file as its public RSA key.

The [create_client_credentials.sh](create_client_credentials.sh) and
[create_server_credentials.sh](create_server_credentials.sh) files should be
used to create the RSA public/private keypairs for both the client and the 
server. The [append_client_credentials.sh](append_client_credentials.sh) then
copies the private key to the client private key file and appends the
public keys to the client configuration and to the remote_server's
configuration file for the client. The
[append_server_credentials.sh](append_server_credentials.sh) file does the same
but then for the remote_server's keypair.
The [reset_credential_files.sh](reset_credential_files.sh) script can be used
to remove the credentials from the files.

## Up and down
Tinc allows various scripts to be run when events occur such as subnets or hosts
coming online or going online. These are described in the 
[tinc.conf][tinc_conf] documentation.
The most important one is [tinc-up](vpn/tinc-up), which is used to bring up the
network interface in most networks. The [host-up](vpn/host-up) script provided
outputs a libnotify message whenever a host comes online or goes offline.

[tinc]: https://www.tinc-vpn.org/
[tinc_conf]: https://www.tinc-vpn.org/documentation/tinc.conf.5