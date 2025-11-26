# proxy
This is an example configuration for [nginx][nginx] that shows how to use nginx
to provide a https webserver that verifies the ssl certificate the client
provides. There are files in the `pki` folder that can be used to create the
necessary intermediate certificate authority.

The client side crt & key file can be from a CA that's completely disjoint from the server side
certificate, so it is possible to have the sever side CA be handled by a proper public CA, but have
the client side cert be signed by a private (non-trusted) CA, as long as the client has a crt & key
derived from the client side CA it will work.

When importing in Chrome, be sure to use the `Your certificates` section, not `Local certificates`,
use a pfx file, with openssl; 
```
openssl pkcs12 -export -out client-$OUR_CN_NAME.pfx -inkey $OUR_CN_NAME.key -in $OUR_CN_NAME.crt -certfile  ca.crt 
```

[nginx]: https://nginx.org/en/