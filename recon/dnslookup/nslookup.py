#!/usr/bin/env python3

import subprocess
import sys


types = ["A", "AAAA", "AFSDB", "ALIAS", "ATMA", "CAA", "CERT", "CNAME", "DHCID", "DNAME", "DNSKEY", "DS", "HINFO", "ISDN", "LOC","MB", "MG", "MINFO", "MR", "MX", "NAPTR", "NS", "NSAP", "NSEC", "NSEC3", "NSEC3PARAM", "PTR", "RP", "RRSIG", "RT", "SOA", "SRV", "TLSA", "TXT", "X25"]

subprocess.call(["clear ; figlet nslookup"], shell=True)
print("\t\t\t\t\t\tA script by SHADOW\n===================================================================")


try:
    if sys.argv[1]=="-h" or sys.argv[1]=="--help":
        print("\nUsage:")
        print("\tpython3 ns_lookup.py [options] [domain]\n")
        print("Options:")
        print("\t-h,  --help=HELP            show help menu and exit")
        print("\t-c,  --common=COMMON        common ns_lookup")
        print("\t-a,  --all=ALL              complete ns_lookup")
        print("\t-t,  --type=TYPE            set own ns_lookup type")
        print("\nTYPE Options:")

        for type_ in types:
            print("\t" + type_ + "\t\t\t" + type_ + " records")

    elif sys.argv[1]=="-c" or sys.argv[1]=="--common":
        subprocess.call(["nslookup -type=type " + url], shell=True)

    elif sys.argv[1]=="-a" or sys.argv[1]=="--all":
        url = sys.argv[2]
        subprocess.call(["nslookup -type=ANY " + url], shell=True)

    elif sys.argv[1]=="-t" or sys.argv[1]=="--type":
        type = sys.argv[2]
        url = sys.argv[3]
        subprocess.call(["nslookup -type="+ type + " " + url], shell=True)

    else:
        url = sys.argv[2]
        subprocess.call(["nslookup -type=ANY " + url], shell=True)

except IndexError:
    print("[-] Missing argument.\nUse -h or --help for usage.")