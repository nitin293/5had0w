#!/usr/bin/env python

import mod_shadow as ms
import subprocess
import re

subprocess.call(["clear ; figlet subdomain scan"], shell=True)
print("\t\t\t\t\t\tA script by SHADOW\n====================================================================\n\n")

try:
    site = input("Enter URL: ")

    with open("./wordlists/subdomain.list","r") as subdomain_list:
        for element in subdomain_list:
            subdomain = element.strip()

            URL = re.search("(?://)(.*)", site)

            if "http://" in site:
                url = "http://" + subdomain + "." + URL.group(1)
                s_rspns = ms.scan_domain(url)
                if s_rspns:
                    print("[+] Discovered_subdomain -->", url)
                else:
                    pass

            elif "https" in site:
                url = "https://" + subdomain + "." + URL.group(1)
                s_rspns = ms.scan_domain(url)
                if s_rspns:
                    print("[+] Discovered_subdomain -->", url)
                else:
                    pass

except KeyboardInterrupt:
    print("\n[-] Ctrl+C detected !")
