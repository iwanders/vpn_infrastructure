This contains guidance how to configure the clients. The `openvpn_` clients assume that the [create_clients.sh](../pki/create_clients.sh) script has been ran.

* [openvpn_ios](openvpn_ios) This contains a [Python][python] script that can be
    used to generate a valid `.mobileconfig` file to configure an OpenVPN
    connection on iOS.
* [openvpn_generic](openvpn_generic) This contains an example configuration for
    OpenVPN, it should work on most systems that support OpenVPN.
* [tinc](tinc) This contains the example files to setup the keys required for
    tinc and the 'client' configuration. Tinc does not differentiate between a
    client and a server, but this is the road warrior configuration.
* [http_ssl_client](http_ssl_client) This contains a script that can be used to
    produce a `.p12` file that a browser can use to authenticate with the proxy
    that requires the client side ssl certificates.
* [client_wg](client_wg) Connects to the wireguard server, use with `wg-quick up ./wireguard.conf`
    don't forget to setup the keys correctly in both the server and the client.


[python]: https://www.python.org/
