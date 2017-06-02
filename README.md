# LXD PROXY

This charm exposes a simple iptables nat-type proxy for Juju deployed LXD containers.

# Deploy
```bash
juju deploy lxd-proxy
```

# Usage
This charm exposes the action `forward-traffic` which accepts two input arguments; port, and host.

Example Usage
```bash
# Add Rule
$ juju run-action lxd-proxy/0 forward-traffic source-port=9000 dest-port=9200 host=10.0.0.119

# Remove Rule
$ juju run-action lxd-proxy/0 remove-rule source-port=9000 dest-port=9200 host=10.0.0.119
```

#### Copyright
James Beedy (c) 2016 <jamesbeedy@gmail.com>

