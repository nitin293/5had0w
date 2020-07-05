#!/usr/bin/env python3

import socket
import subprocess
import optparse
import requests
import re
import webtech


class colors:
    white = '\033[37m'
    red = '\033[31m'
    green = '\033[32m'
    blue = '\033[34m'
    yellow = '\033[33m'


try:
    def get_arg():
        parser = optparse.OptionParser()
        parser.add_option("-d", "--domain", dest="domain", help="set domain name")
        (options, arguments) = parser.parse_args()

        return options


    def dns_recon(domain):
        domain = domain.split("://")
        url = domain[1]
        ip = socket.gethostbyname(url)
        print("\n" + colors.red + "[+] DNS Recon : ")
        print(colors.green + "\n\n[+] IP Address : " + colors.yellow + ip)
        print(colors.blue + "\n----------------------------------------------------------------\n\n")


        print(colors.green + "[+] DNS type=ANY Records : \n" + colors.yellow)
        subprocess.call(["nslookup -type=ANY " + url], shell=True)
        print(colors.blue + "\n----------------------------------------------------------------\n\n")


        try:
            print(colors.green + "[+] SPF Record : \n" + colors.yellow)
            subprocess.call(["nslookup -type=txt " + url + " | grep text"], shell=True)
        except subprocess.CalledProcessError:
            print(colors.red + "[+] No SPF Record found !")
        print(colors.blue + "\n----------------------------------------------------------------\n\n")


        try:
            print(colors.green + "[+] DMARC Record : \n" + colors.yellow)
            subprocess.call(["nslookup -type=txt _dmarc." + url + " | grep text"], shell=True)
        except subprocess.CalledProcessError:
            print(colors.red + "[+] No DMARC Record found !")
        print(colors.blue + "\n----------------------------------------------------------------\n\n")


        try:
            print(colors.green + "[+] DKIM Record : \n" + colors.yellow)
            subprocess.call(["nslookup -type=txt _domainkey." + url], shell=True)
        except subprocess.CalledProcessError:
            print(colors.red + "[+] No DKIM Record found !")
        print(colors.blue + "\n----------------------------------------------------------------\n\n")


    def get_targetip_info(target):
        domain = target.split("://")
        url = domain[1]
        response = requests.get("https://tools.keycdn.com/geo.json?host=" + url)
        data = response.json()["data"]["geo"]

        print(colors.red + "[+] IP Geolocation : \n")

        for element in data:
            print(colors.yellow + element + " : " + str(data[element]))

        print("\nGoogle Map : https://www.google.com/maps/search/" + str(data["latitude"]) + "," + str(data["longitude"]) +"\n")

        print(colors.blue + "\n----------------------------------------------------------------\n\n")


    def whois(site):
        domain = site.split("://")
        url = domain[1]

        response = requests.get("https://whois.ws/whois/" + url)
        content = str(response.content)
        whois_raw = re.findall('(?:</a></small></div>)(.*)(?:<br\s/>)', content)

        if "<br />\\n" in whois_raw[0]:
            whois_data = whois_raw[0].split("<br />\\n")
        else:
            whois_data = whois_raw[0].split("<br />\\r\\n")

        print(colors.red + "[+] WHOIS Records : \n\n")

        for element in whois_data:
            print(colors.yellow + element)
        print(colors.blue + "\n\n----------------------------------------------------------------\n\n")


    def get_tech_info(url):
        obj = webtech.WebTech(options={"json":True})
        data = obj.start_from_url(url)

        # print(data)

        tech_data = data["tech"]
        header_data = data["headers"]

        print(colors.red + "[+] Technologies : ")
        print(colors.green + "\n[+] Web-Technologies : ")
        for datas in tech_data:
            print("\t" + colors.yellow + "Name:" + " " + datas["name"] + " " + " \tVersion :", datas["version"])

        print(colors.green + "\n[+] Header Info : ")
        for datas in header_data:
            print("\t" + colors.yellow + datas["name"] + " " + datas["value"])
        print(colors.blue + "\n\n----------------------------------------------------------------\n\n")


    def main():
        options = get_arg()
        domain = options.domain

        if domain:
            if "http://" in domain or "https://" in domain:
                dns_recon(domain)
                get_targetip_info(domain)
                whois(domain)
                get_tech_info(domain)
            else:
                print("\n[-] Please use http:// or https:// before URL.\n")
        else:
            print("[-] Domain not specified.\nUse -h or --help for more info.")


    if __name__=="__main__":
        main()

except KeyboardInterrupt:
    print(colors.red + "\n[+] Ctrl+C detected !\n")
except IndexError:
    subprocess.call(["clear"], shell=True)
    main()