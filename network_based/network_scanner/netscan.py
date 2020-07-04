#!/usr/bin/env python

import subprocess
import net_lib as nl

subprocess.call(["clear ; figlet net scan"], shell=True)
print("\t\t\t\t\t\tA script by SHADOW\n======================================================================\n")
print("[+] Run The Application as ROOT.\n")

try:
    ip_range = raw_input("Enter IP/IP_range: ")

    print("\n[+] Scanning Network for: " + ip_range)

    def print_result(result_list):
        print("\n    IP\t\t\t\t   MAC Address\n==================================================")
        for element in result_list:
            print(element["ip"] + "\t\t\t" + element["mac"])
        print("\n[+] Finished !")

    print_result(nl.scan(ip_range))

except KeyboardInterrupt:
    print("\n\n[-] Ctrl+C detected.")
except ValueError:
    pass
except KeyError:
    print("\n\n[-] Invalid Input.")