#!/usr/bin/env python3

import uuid
import base64
import sys
import argparse

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(description='Create iOS VPN on demand '
                                     ' mobileconfig file.')
    parser.add_argument('--fqdn', type=str,
                        default='remote_server',
                        help='hostname / ip of server')
    parser.add_argument("--proto", type=str, default='tcp',
                        help='use tcp or udp')
    parser.add_argument("--port", type=int, default=443,
                        help='the port to use')
    parser.add_argument("--password", type=str,
                        default=None,
                        help='The password for the pk12 file to be loaded.')
    parser.add_argument('--displayname', type=str, default='Remote Server',
                        help='Display name of server')
    parser.add_argument('--PayloadDisplayName', type=str, default=None,
                        help='Display name, defaults to VPN -'
                        ' {fqdn}:{port}/{proto}')
    parser.add_argument('--UserDefinedName', type=str, default=None,
                        help='User defined name, as shown in VPN menu'
                        ' defaults to VPN - {fqdn}:{port}/{proto}')

    args = parser.parse_args()

    if not args.PayloadDisplayName:
        args.PayloadDisplayName = "VPN - {fqdn}:{port}/{proto}".format(
            fqdn=args.fqdn, proto=args.proto, port=args.port)

    if not args.UserDefinedName:
        args.UserDefinedName = "VPN - {fqdn}:{port}/{proto}".format(
            fqdn=args.fqdn, proto=args.proto, port=args.port)

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
        p12_b64 = base64.b64encode(f.read()).decode('utf-8')

    with open("ca.crt", "r") as f:
        ca_crt = f.read()

    with open("on_demand.mobileconfig.template", "r") as f:
        template = f.read()

    """
        As per:
            https://developer.apple.com/library/content/featuredarticles/
                  iPhoneConfigurationProfileRef/Introduction/Introduction.html
        wrap on 52 characters.
    """
    def wrap(line, w=52):
        return "\n".join([line[i:i+w] for i in range(0, len(line), w)])

    res = template.format(displayname=args.displayname,
                          fqdn=args.fqdn, ca_crt=ca_crt.replace("\n", "\\n"),
                          internal_key_and_cert=wrap(p12_b64),
                          pkcs_payload_uuid=str(uuid.uuid4()).upper(),
                          vpn_payload_uuid=str(uuid.uuid4()).upper(),
                          proto=args.proto,
                          port=args.port,
                          password=args.password,
                          config_payload_uuid=str(uuid.uuid4()).upper(),
                          PayloadDisplayName=args.PayloadDisplayName,
                          UserDefinedName=args.UserDefinedName,
                          )

    with open('on_demand.mobileconfig', 'w') as f:
        f.write(res)
