This contains guidance how to configure the clients. The `openvpn_` clients assume that the [create_clients.sh](../pki/create_clients.sh) script has been ran.

* [openvpn_ios](openvpn_ios) This contains a [Python][python] script that can be
    used to generate a valid `.mobileconfig` file to configure an OpenVPN
    connection on iOS.
* [openvpn_generic](openvpn_generic) This contains an example configuration for
    OpenVPN, it should work on most systems that support OpenVPN.
* [tinc](tinc) This contains the example files to setup the keys required for
    tinc and the 'client' configuration. Tinc does not differentiate between a
    client and a server, but this is the road warrior configuration.



[python]: https://www.python.org/