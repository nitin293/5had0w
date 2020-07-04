#!/usr/bin/env python

import mod_shadow as ms
import subprocess
import urlparse

subprocess.call(["clear ; figlet dirscan"], shell=True)
print("\t\t\t\t\t\tA script by SHADOW\n====================================================================\n\n")
print("[+] Run The Application as ROOT.")


try:
    site = raw_input("Enter URL: ")

    got_link = []

    def crawler(site):
        directory_list = ms.dir_list(site)

        for directory in directory_list:
            link = urlparse.urljoin(site ,directory)

            if "#" in link:
                link = link.split("#")[0]

            if site in link and link not in got_link:
                got_link.append(link)
                crawler(link)
                print(link)

    crawler(site)

except KeyboardInterrupt:
    print("\n[-] Ctrl+C detected !")
