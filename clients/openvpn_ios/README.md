# iOS mobileconfig file for OpenVPN

To accomodate the changes made with OpenVPN Connect 1.2.5 the client certificate
and client key are now inlined in the configuration, this eliminates the need
to seperately create a [.p12][p12file].

To create the configuration profile run the [generate.py](generate.py) script to
 generate the mobileconfig file. This file reads the
[on_demand.mobileconfig.xml](on_demand.mobileconfig.xml) template and
substitutes the desired values. For a full list of possible options run it with
`./generate.py --help`.

Most fields will get some useful default value if nothing is provided, the
following two lines create configurations for the two OpenVPN servers used
throughout this repository.
```bash
./generate.py --host $REMOTE_SERVER --proto tcp --port 443  -o vpn_https.mobileconfig --VPNPayloadOrganization "HTTPS Port"
./generate.py --host $REMOTE_SERVER --proto udp --port 1194 -o vpn_udp.mobileconfig   --VPNPayloadOrganization "OpenVPN Port"
```

The identifier of each certificate is `{host:s}.{port:d}.{proto:s}.vpnondemand`,
this means that if these values do not change, the new profile will overwrite
the one already installed.

The default template includes VPN-on-demand configuration, there are a lot more
options to fine tune this in the [On Demand Rules][apple_vpn_ondemand].


[p12file]: https://en.wikipedia.org/wiki/PKCS_12
[apple_vpn_ondemand]: https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW36