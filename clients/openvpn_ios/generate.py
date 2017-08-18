#!/usr/bin/env python3

# The MIT License (MIT)
#
# Copyright (c) 2017 Ivor Wanders
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import uuid
import base64
import sys
import argparse

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(
        description='Create iOS VPN on demand mobileconfig file. No string '
        'sanitization is done before values are inserted into the template.'
        )
    parser.add_argument('--host', type=str,
                        default='remote_server',
                        help='hostname / ip of server')

    parser.add_argument('--output', '-o', type=str,
                        default='vpn_on_demand.mobileconfig',
                        help='The output file name to write to.')

    parser.add_argument("--proto", type=str, default='tcp',
                        help='use tcp or udp')
    parser.add_argument("--port", type=int, default=443,
                        help='the port to use')
    parser.add_argument("--password", type=str,
                        default=None,
                        help='The password for the pk12 file to be loaded.')

    parser.add_argument('--UserDefinedName', type=str, default=None,
                        help='User defined name, as shown in VPN menu'
                        ' defaults to "VPN - {host}:{port}/{proto}"')

    parser.add_argument('--ProfilePayloadDescription', type=str,
                        default=None,
                        help='The profile payload description (defaults to: '
                        'VPN {host:s}:{port:d}/{proto:s} with vpn on demand)')
    parser.add_argument('--ProfilePayloadDisplayName', type=str,
                        default=None,
                        help='The profile payload description (defaults to: '
                        'VPN {host}:{port}/{proto} on demand)')
    parser.add_argument('--ProfilePayloadOrganization', type=str,
                        default="Organization",
                        help='The organization to display for the'
                        'configuration profile itself.')

    parser.add_argument('--VPNPayloadDescription', type=str,
                        default="Configures VPN configuration, authentication"
                        " and on demand rules.",
                        help='The description to display.')
    parser.add_argument('--VPNPayloadDisplayName', type=str, default=None,
                        help='Display name, defaults to "VPN -'
                        ' {host}:{port}/{proto}".')
    parser.add_argument('--VPNPayloadOrganization', type=str, default="",
                        help='The organization to display for the VPN config.'
                        ' This is shown as grey beneath the'
                        ' VPNPayloadDisplayName value in the VPN settings'
                        ' menu')

    args = parser.parse_args()

    if not args.VPNPayloadDisplayName:
        args.VPNPayloadDisplayName = "VPN - {host}:{port}/{proto}".format(
            host=args.host, proto=args.proto, port=args.port)

    if not args.ProfilePayloadDisplayName:
        args.ProfilePayloadDisplayName = "VPN {host}:{port}/{proto} on " \
            "demand".format(host=args.host, proto=args.proto, port=args.port)

    if not args.UserDefinedName:
        args.UserDefinedName = "VPN - {host}:{port}/{proto}".format(
            host=args.host, proto=args.proto, port=args.port)

    if not args.ProfilePayloadDescription:
        args.ProfilePayloadDescription = 'VPN {host:s}:{port:d}/{proto:s} ' \
            'with vpn on demand'.format(host=args.host, port=args.port,
                                        proto=args.proto)

    if not args.password:
        args.password = input("Type the .p12 file password:")

    """
    iOS mandates that the p12 file does NOT include the ca, which is default
    from easyrsa3.
    That could be done with:
    $ openssl pkcs12 -export -out client_pkcs.p12 -inkey client.key \
        -in client.crt  -name  $(basename $(pwd))
    Testing appears that it is no problem if the p12 file also contains the ca.
    """
    with open("client_pkcs.p12", "rb") as f:
        # requires to be encoded in base 64
        p12_b64 = base64.b64encode(f.read()).decode('utf-8')

    with open("ca.crt", "r") as f:
        ca_crt = f.read()

    with open("on_demand.mobileconfig.xml", "r") as f:
        template = f.read()

    """
        As per:
            https://developer.apple.com/library/content/featuredarticles/
                  iPhoneConfigurationProfileRef/Introduction/Introduction.html
        wrap on 52 characters.
    """
    def wrap(line, w=52):
        return "\n".join([line[i:i+w] for i in range(0, len(line), w)])

    res = template.format(
            host=args.host, ca_crt=ca_crt.replace("\n", "\\n"),
            internal_key_and_cert=wrap(p12_b64),
            pkcs_payload_uuid=str(uuid.uuid4()).upper(),
            vpn_payload_uuid=str(uuid.uuid4()).upper(),
            proto=args.proto,
            port=args.port,
            password=args.password,
            config_payload_uuid=str(uuid.uuid4()).upper(),
            UserDefinedName=args.UserDefinedName,
            ProfilePayloadOrganization=args.ProfilePayloadOrganization,
            ProfilePayloadDisplayName=args.ProfilePayloadDisplayName,
            ProfilePayloadDescription=args.ProfilePayloadDescription,
            VPNPayloadDisplayName=args.VPNPayloadDisplayName,
            VPNPayloadOrganization=args.VPNPayloadOrganization,
            VPNPayloadDescription=args.VPNPayloadDescription,
        )

    with open(args.output, 'w') as f:
        f.write(res)
