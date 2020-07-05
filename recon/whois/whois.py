#!/usr/bin/env python3

import requests
import re
import optparse
import subprocess

subprocess.call(["clear ; figlet Who - IS"], shell=True)
print("\t\t\t\tA script by SHADOW\n===================================================\n")

try:
    class colors:
        white = '\033[37m'
        red = '\033[31m'
        green = '\033[32m'
        blue = '\033[34m'
        yellow = '\033[33m'

    def get_args():
        parser = optparse.OptionParser()
        parser.add_option("-d", "--domain", dest="domain", help="set domain name")
        (options, args) = parser.parse_args()

        return options

    def whois(site):
        response = requests.get("https://whois.ws/whois/" + site)
        content = str(response.content)
        whois_raw = re.findall('(?:</a></small></div>)(.*)(?:<br\s/>)', content)

        if "<br />\\n" in whois_raw[0]:
            whois_data = whois_raw[0].split("<br />\\n")
        else:
            whois_data = whois_raw[0].split("<br />\\r\\n")

        print(colors.green + "\nWHOIS Records : \n" + colors.blue + "=======================================================================\n")
        for element in whois_data:
            print(colors.yellow + element)
        print("\n")

    if __name__ == '__main__':
        options = get_args()

        if not options.domain:
            print("[-] Argument missing.\nUse -h or --help for more info.")
        else:
            whois(options.domain)

except KeyboardInterrupt:
    print("[-] Ctrl+C detected !\n")
except IndexError:
    print("[-] Program Error detected !\nTry again. Use -h or --help for usage and more info.\n")