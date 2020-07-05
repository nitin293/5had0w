#!/usr/bin/env python3

import requests
import socket
import subprocess
import sys
from geoip import geolite2
from geopy.geocoders import Nominatim

subprocess.call(["clear ; figlet ip - geolocation"], shell=True)
print("\t\t\t\t\t\t\tA script by SHADOW\n===========================================================================")

try:
    class colors:
        white = '\033[37m'
        red = '\033[31m'
        green = '\033[32m'
        blue = '\033[34m'
        yellow = '\033[33m'

    def arguments():
        if sys.argv[1]=="-m" or sys.argv[1]=="--myip":
            get_myip_info()

        elif sys.argv[1]=="-t" or sys.argv[1]=="--target":
            target = sys.argv[2]
            get_targetip_info(target)

        elif sys.argv[1]=="-u" or sys.argv[1]=="--url":
            target = socket.gethostbyname(sys.argv[2])
            get_url_info(target)

        elif sys.argv[1]=="-h" or sys.argv[1]=="--help":
            print("Usage:\n\tpython3 ns_lookup.py [options] [domain]\n")
            print("Options:\n\t-h,  --help=HELP            show help menu and exit")
            print("\t-t,  --target=TARGET        set target IP")
            print("\t-u,  --url=URL              set target URL")
            print("\t-m,  --myip=MY-IP           set own IP as target\n")

        else:
            print("[-] Invalid input.\nUse -h or --help usage and more info.\n")


    def get_myip_info():
        response = requests.get("http://ifconfig.co/json")
        json_data = response.json()

        try:
            del json_data["user_agent"]
        except KeyError:
            pass

        print(colors.blue + "\n[+]------------ IP Information -----------------[+]\n")

        for info in json_data:
            print(colors.yellow + info + " : " + str(json_data[info]))

        print("\nGoogle Map : https://www.google.com/maps/search/" + str(json_data["latitude"]) + "," + str(json_data["longitude"]) +"\n")
        print(colors.blue + "\n[+] ------------------- Completed ------------------- [+]\n\n")

    def get_targetip_info(target):
        response = requests.get("https://tools.keycdn.com/geo.json?host=" + target)
        data = response.json()["data"]["geo"]

        print(colors.blue + "\n[+]------------ IP Information -----------------[+]\n")

        for element in data:
            print(colors.yellow + element + " : " + str(data[element]))

        print("\nGoogle Map : https://www.google.com/maps/search/" + str(data["latitude"]) + "," + str(data["longitude"]) +"\n")
        print(colors.blue + "\n[+] ------------------- Completed ------------------- [+]\n\n")



    def get_url_info(target):
        data = geolite2.lookup(target.encode())
        locator = Nominatim(user_agent="myGeocoder")
        location = locator.reverse(data.location)

        datas = {
            "ip" : str(data.ip),
            "country_code" : str(data.country),
            "continent" : str(data.continent),
            "sub_div" : str(data.subdivisions),
            "timezone" : str(data.timezone),
            "lattitude" : str(data.location[0]),
            "longitude" : str(data.location[1]),
            "country" : str(location.raw["address"]["country"]),
            "county" : str(location.raw["address"]["county"]),
            "state" : str(location.raw["address"]["state"]),
            "postcode" : str(location.raw["address"]["postcode"])
        }

        print(colors.blue + "\n[+]------------ IP Information -----------------[+]\n")

        for info in datas:
            if info:
                print(colors.yellow + info + " : " + datas[info])
            else:
                pass

        print("\nGoogle Map : https://www.google.com/maps/search/" + datas["lattitude"] + "," + datas["longitude"] +"\n")
        print(colors.blue + "\n[+] ------------------- Completed -------------------\n\n")

    if __name__ == '__main__':
        arguments()


except IndexError:
    print("Usage:\n\tpython3 ns_lookup.py [options] [domain]\n")
    print("Options:\n\t-h,  --help=HELP            show help menu and exit")
    print("\t-t,  --target=TARGET        set target IP")
    print("\t-u,  --url=URL              set target URL")
    print("\t-m,  --myip=MY-IP           set own IP as target\n")
except UnboundLocalError:
    pass
except socket.gaierror:
    print("[-] Check URL and try again.\nUse -h or --help for more info.")
except KeyboardInterrupt:
    print("[-] Ctrl+C detected")



'''------------------------------ JSON DATAS --------------------------------------

city = json_data["city"]
region = json_data["region"]
region_code = json_data["region_code"]
country = json_data["country"]
country_code = json_data["country_code"]
country_code_iso3 = json_data["country_code_iso3"]
country_capital = json_data["country_capital"]
country_tld = json_data["country_tld"]
country_name = json_data["country_name"]
country_name = json_data["continent_code"]
in_eu = json_data["in_eu"]
postal = json_data["postal"]
lattitude = json_data["lattitude"]
longitude = json_data["longitude"]
timezone = json_data["timezone"]
utc_offset = json_data["utc_offset"]
country_calling_code = json_data["country_calling_code"]
currency = json_data["currency"]
currency_name = json_data["currency_name"]
languages = json_data["languages"]
country_area = json_data["country_area"]
country_population = json_data["country_population"]
asn = json_data["asn"]
org = json_data["org"]

for e in json_data:
    print(e + " : " + str(json_data[e]))'''