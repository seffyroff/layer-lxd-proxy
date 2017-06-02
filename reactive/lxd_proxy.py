from charms.reactive import when_not, set_state, when
from charmhelpers.core.hookenv import status_set


@when_not('lxd.proxy.available')
def init_proxy():
    set_state('lxd.proxy.available')


@when('lxd.proxy.available')
def status_set_avail():
    status_set('active', "LXD proxy available")
