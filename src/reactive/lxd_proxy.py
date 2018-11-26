from charms.reactive import when_not
from charmhelpers.core.hookenv import status_set


@when_not('lxd.proxy.not.available')
def status_set_avail():
    status_set('active', "LXD proxy available")
