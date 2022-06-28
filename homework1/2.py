"""
Написать метод int32_to_ip, который принимает на вход 32-битное целое число
(integer) и возвращает строковое представление егов виде IPv4-адреса:
"""

import ipaddress


def int32_to_ip(int32: int) -> str:
    return str(ipaddress.ip_address(int32))
