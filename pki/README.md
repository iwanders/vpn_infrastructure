This contains some helper files for use with [easy-rsa][easyrsa].

* [create_ca.sh](create_ca.sh) Sets up the [PKI][PKI] and creates a certificate
    authority, it creates a folter `pki` in this directory.
* [create_server.sh](create_server.sh) Creates the server side certificate for
    the OpenVPN server.
* [create_clients.sh](create_clients.sh) Creates a client certificate for each
    of the clients in the clients folder. (Tinc does NOT use these).
* [setup.sh](setup.sh) Can be sourced from anywhere, after that the `easyrsa` 
    script can be used and the PKI infrastructure in the `pki` folder is used.


[easyrsa]: https://github.com/OpenVPN/easy-rsa
[PKI]: https://en.wikipedia.org/wiki/Public_key_infrastructure