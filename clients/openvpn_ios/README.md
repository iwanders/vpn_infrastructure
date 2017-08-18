# iOS mobileconfig file for OpenVPN

Generating a mobileconfig file for iOS requires two steps:

The first step is exporting a [.p12][p12file] file, this contains the client
certificate and private key. iOS requires that this file has a password, this
password will be in plain text in the mobileconfig file. This step is
performed by the [copy_credentials.sh](copy_credentials.sh) file.

The second step is to run the [generate.py](generate.py) script to generate the
mobileconfig file. This file reads the
[on_demand.mobileconfig.xml](on_demand.mobileconfig.xml) template and
substitutes the desired values. For a full list of possible options run it with
`./generate.py --help`.

Most fields will get some useful values if nothing is provided, the following
two lines create configurations for the two OpenVPN servers used throughout this
repository.
```bash
./generate.py --password $THE_P12_PASSWORD --host $REMOTE_SERVER --proto tcp --port 443 -o vpn_https.mobileconfig --VPNPayloadOrganization "HTTPS Port"
./generate.py --password $THE_P12_PASSWORD --host $REMOTE_SERVER --proto udp --port 1194 -o vpn_udp.mobileconfig --VPNPayloadOrganization "OpenVPN Port"
```

The identifier of each certificate is `{host:s}.{port:d}.{proto:s}.vpnondemand`
this means that if these values do not change, the new profile will overwrite
the one already installed.

The default template includes VPN-on-demand configuration, there are a lot more
options to fine tune this in the [On Demand Rules][apple_vpn_ondemand].


[p12file]: https://en.wikipedia.org/wiki/PKCS_12
[apple_vpn_ondemand]: https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW36