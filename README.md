# LXD PROXY

This charm exposes a simple iptables nat-type proxy for Juju deployed LXD containers.

# Deploy
```bash
juju deploy lxd-proxy
```

# Usage
This charm exposes two actions; `forward-traffic` and `remove-rule`.

Example Usage
```bash
# forward-traffic
$ juju run-action lxd-proxy/0 forward-traffic source-port=9000 dest-port=9200 host=10.0.0.119

# remove-rule
$ juju run-action lxd-proxy/0 remove-rule source-port=9000 dest-port=9200 host=10.0.0.119
```

#### Copyright
James Beedy (c) 2016 <jamesbeedy@gmail.com>

