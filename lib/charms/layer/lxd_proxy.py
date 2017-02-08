from subprocess import call


def save_ip_tables(host, port):
    host_port = {'host': host, 'port': port}
    call("iptables -t nat -A OUTPUT -p tcp --dport {port} "
         "-j DNAT --to-destination {host}:{port}".format(**host_port).split())
    call("iptables-save".split())

