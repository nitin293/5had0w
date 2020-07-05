#!/usr/bin/env python

import os
import requests
import subprocess

subprocess.call(["clear ; figlet directory scan"], shell=True)
print("\t\t\t\t\t\tA script by SHADOW\n====================================================================\n\n")

try:
    host = raw_input("Enter host(eg. http://example.com) : ")
    wordlist = "../wordlists/common.txt"

    def request(url):
        response = requests.get(url)
        if response:
            print("[+] Found directory --> " + url)

    def scanner(wordlist, host):
        with open(wordlist,"r") as dirlist:
            for line in dirlist:
                dir = line.strip()
                url = host + "/" + dir + ".txt"
                print("[!] Scanning : " + url)
                request(url)


    scanner(wordlist, host)

except KeyboardInterrupt:
    print("[-] Ctrl+C detected !")
except requests.exceptions.ConnectionError:
    print("[-] Check your Network Connectivity.")
except requests.exceptions.MissingSchema:
    print("[-] Use http:// or http:// and try again !")
