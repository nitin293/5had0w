#!/usr/bin/env python

import scapy.all as scapy
from scapy.layers import http


def get_login(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords = ["user", "pass", "login", "Login"]
        for keyword in keywords:
            if keyword in load:
                return load


def get_url(packet):
    if packet.haslayer(http.HTTPRequest):
        url = str(packet.Host + packet.Path)
        return url
