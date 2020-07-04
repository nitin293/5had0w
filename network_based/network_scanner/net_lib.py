#!/ur/bin/env python

import scapy.all as scapy

def scan(ip_range):
    ip = scapy.ARP(pdst = ip_range)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    packet = broadcast/ip

    response_list = scapy.srp(packet, verbose=False,timeout=4)[0]

    answered_list = []

    for response in response_list:
        ip_mac_dict = {"ip":response[1].psrc, "mac":response[1].hwsrc}
        answered_list.append(ip_mac_dict)
    return answered_list

