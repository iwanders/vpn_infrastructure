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

    parser.add_argument("--not-on-ssid", type=str, default=None, nargs='*',
                        help='Specify SSIDs on which not to connect to vpn.')

    parser.add_argument('--UserDefinedName', type=str, default=None,
                        help='User defined name, as shown in VPN menu'
                        ' defaults to "{host}:{port}/{proto}"')

    # Used for the profile.
    parser.add_argument('--ProfilePayloadDescription', type=str,
                        default=None,
                        help='The profile payload description (defaults to: '
                        '{host:s}:{port:d}/{proto:s})')
    parser.add_argument('--ProfilePayloadDisplayName', type=str,
                        default=None,
                        help='The profile payload description (defaults to: '
                        '{host}:{port}/{proto})')
    parser.add_argument('--ProfilePayloadOrganization', type=str,
                        default="Organization",
                        help='The organization to display for the'
                        'configuration profile itself.')

    # Used for the actual vpn connection.
    parser.add_argument('--VPNPayloadDescription', type=str,
                        default="Configures VPN configuration, authentication"
                        " and on demand rules.",
                        help='The description to display.')
    parser.add_argument('--VPNPayloadDisplayName', type=str, default=None,
                        help='Display name, defaults to "'
                        '{host}:{port}/{proto}".')
    parser.add_argument('--VPNPayloadOrganization', type=str, default="",
                        help='The organization to display for the VPN config.'
                        ' This is shown as grey beneath the'
                        ' VPNPayloadDisplayName value in the VPN settings'
                        ' menu')

    # All these names are super confusing.
    parser.add_argument('--vpn-title', type=str, default=None,
                        help='The title to display everywhere. Overrides all other naming. Substitution for host, port proto happens.')
    parser.add_argument('--vpn-sub-title', type=str, default=None,
                        help='The grey subtitle to display everywhere. Overrides all other naming. Substitution for host, port proto happens.')
    

    args = parser.parse_args()

    if not args.VPNPayloadDisplayName:
        args.VPNPayloadDisplayName = "{host}:{port}/{proto}".format(
            host=args.host, proto=args.proto, port=args.port)

    if not args.ProfilePayloadDisplayName:
        args.ProfilePayloadDisplayName = "{host}:{port}/{proto}" \
            "".format(host=args.host, proto=args.proto, port=args.port)

    if not args.UserDefinedName:
        args.UserDefinedName = "{host}:{port}/{proto}".format(
            host=args.host, proto=args.proto, port=args.port)

    if not args.ProfilePayloadDescription:
        args.ProfilePayloadDescription = '{host:s}:{port:d}/{proto:s}' \
            ''.format(host=args.host, port=args.port,
                                        proto=args.proto)

    # Unique key used by IOS to distinguish profiles.
    payload_identifier = "{host:s}:{port:d}/{proto:s}".format(host=args.host, port=args.port,
                                        proto=args.proto)

    if args.vpn_title:
        vpn_title = args.vpn_title.format(host=args.host, port=args.port,
                                        proto=args.proto)
        args.UserDefinedName = vpn_title
        args.VPNPayloadDisplayName = vpn_title
        args.ProfilePayloadDisplayName = vpn_title
        args.ProfilePayloadDescription = vpn_title
        payload_identifier += vpn_title

    if args.vpn_sub_title:
        vpn_sub_title = args.vpn_sub_title.format(host=args.host, port=args.port,
                                        proto=args.proto)
        args.ProfilePayloadOrganization = vpn_sub_title
        args.VPNPayloadOrganization = vpn_sub_title
        payload_identifier += "_" + vpn_sub_title

    not_on_ssids = ""
    if args.not_on_ssid:
        not_on_ssids = """
                          <dict>
                                  <key>Action</key>
                                  <string>Disconnect</string>
                                  <key>InterfaceTypeMatch</key>
                                  <string>WiFi</string>
                                  <key>SSIDMatch</key>
                                  <array>
                                          {}
                                  </array>
                          </dict>
        """.format("\n                                          ".join(f"<string>{v}</string>" for v in args.not_on_ssid))

    with open("ca.crt", "r") as f:
        ca_crt = f.read()

    with open("client.crt", "r") as f:
        client_crt = f.read()

    with open("client.key", "r") as f:
        client_key = f.read()

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
            host=args.host,
            ca_crt=ca_crt.replace("\n", "\\n"),
            client_crt=client_crt.replace("\n", "\\n"),
            client_key=client_key.replace("\n", "\\n"),
            pkcs_payload_uuid=str(uuid.uuid4()).upper(),
            vpn_payload_uuid=str(uuid.uuid4()).upper(),
            proto=args.proto,
            port=args.port,
            config_payload_uuid=str(uuid.uuid4()).upper(),
            UserDefinedName=args.UserDefinedName,
            ProfilePayloadOrganization=args.ProfilePayloadOrganization,
            ProfilePayloadDisplayName=args.ProfilePayloadDisplayName,
            ProfilePayloadDescription=args.ProfilePayloadDescription,
            VPNPayloadDisplayName=args.VPNPayloadDisplayName,
            VPNPayloadOrganization=args.VPNPayloadOrganization,
            VPNPayloadDescription=args.VPNPayloadDescription,
            PayloadIdentifier=payload_identifier,
            not_on_ssids=not_on_ssids,
        )

    with open(args.output, 'w') as f:
        f.write(res)
