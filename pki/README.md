This contains some helper files for use with [easy-rsa][easyrsa].

# Certificate authority and Servers
* [create_ca.sh](create_ca.sh) Sets up the [PKI][PKI] and creates a certificate
    authority, it creates a folter `pki` in this directory.
* [create_server.sh](create_server.sh) Creates the server side certificate for
    the OpenVPN server.
* [create_clients.sh](create_clients.sh) Creates a client certificate for each
    of the clients in the clients folder. (Tinc does NOT use these).
* [setup.sh](setup.sh) Can be sourced from anywhere, after that the `easyrsa` 
    script can be used and the PKI infrastructure in the `pki` folder is used.

# Intermediate CA for client side certificates.
For the client side SSL certificates we create a intermediate certificate
authority that signs the client side certificates. 
* [client-create_ca.sh](client-create_ca.sh) Sets up the `client-pki` folder and
    creates a sub ca that is to be signed by the original ca.
* [client-subca-sign.sh](client-subca-sign.sh) This uses the originally setup
    certificate authority to sign the intermediate authority.
* [client-create_clients.sh](client-create_clients.sh) This runs through the
    client folders and creates client certificates for each.
* [client-setup.sh](client-setup.sh) Can be sourced from anywhere, after that
    the `easyrsa`  script can be used and the PKI infrastructure in the
    `client-pki` folder is used.

[easyrsa]: https://github.com/OpenVPN/easy-rsa
[PKI]: https://en.wikipedia.org/wiki/Public_key_infrastructure