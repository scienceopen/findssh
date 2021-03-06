"""
normally we use coroutines, but for demo purposes we have threadpool too.
"""
import ipaddress

import findssh.threadpool

PORT = 22
SERVICE = ""
TIMEOUT = 1.0


def test_threadpool():
    net = findssh.netfromaddress(findssh.getLANip())
    hosts = findssh.threadpool.get_hosts(net, PORT, SERVICE, TIMEOUT)
    for host, svc in hosts:
        assert isinstance(host, ipaddress.IPv4Address)
        assert isinstance(svc, str)
        break
