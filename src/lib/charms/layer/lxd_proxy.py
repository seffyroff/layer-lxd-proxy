from subprocess import call
from charmhelpers.core.hookenv import unit_private_ip
from charmhelpers.contrib.network.ip import get_iface_from_addr


def save_ip_tables(host, source_port, dest_port):
    iface = get_iface_from_addr(unit_private_ip())
    host_port = {'host': host, 'source_port': source_port,
                 'dest_port': dest_port, 'iface': iface}
    call("iptables -t nat -A PREROUTING -i {iface} -p tcp --dport {source_port} "
         "-j DNAT --to {host}:{dest_port}".format(**host_port).split())
    call("iptables-save > /etc/iptables/rules.v4".split())

