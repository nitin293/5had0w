#!/usr/bin/env python3

import webtech
import sys
import subprocess

subprocess.call(["clear ; figlet Web - Tech"], shell=True)
print("\t\t\t\t\tA script by SHADOW\n===========================================================")

try:
    class colors:
        white = '\033[37m'
        red = '\033[31m'
        green = '\033[32m'
        blue = '\033[34m'
        yellow = '\033[33m'

    def arguments():
        if sys.argv[1]=="-u" or sys.argv[1]=="--url":
            url = sys.argv[2]
            get_tech_info(url)

        elif sys.argv[1]=="-r" or sys.argv[1]=="--reset":
            print("\n[+] Reseting...")
            subprocess.check_output(["pip3 uninstall webtech -y; pip3 install webtech"], shell=True)
            print("[+] Reset Successfull !\n")

        elif sys.argv[1]=="-h" or sys.argv[1]=="--help":
            print("Usage:\n\tpython3 webtech.py [options] [domain]\n")
            print("Options:\n\t-h,  --help=HELP            show help menu and exit")
            print("\t-u,  --url=URL              set URL")
            print("\t-r,  --reset=RESET          reset all")

        else:
            print("[-] Invalid input.\nUse -h or --help usage and more info.\n")


    def get_tech_info(url):
        obj = webtech.WebTech(options={"json":True})
        data =obj.start_from_url(url)

        # print(data)

        tech_data = data["tech"]
        header_data = data["headers"]


        print("\n[+] Web-Technologies : ")
        for datas in tech_data:
            print("\t", "Name:", datas["name"], " \tVersion :", datas["version"])

        print("\n[+] Header Info : ")
        for datas in header_data:
            print("\t", datas["name"], datas["value"])
        print("\n")



    if __name__ == '__main__':
        arguments()


except KeyboardInterrupt:
    print("\n[-] Ctrl+C detected !\n")
except ValueError:
    print("\n[-] Use http:// or https:// and try again.\n")
except IndexError:
    print("\nUsage:\n\tpython3 webtech.py [options] [domain]\n")
    print("Options:\n\t-h,  --help=HELP            show help menu and exit")
    print("\t-u,  --url=URL              set URL")
    print("\t-r,  --reset=RESET          reset all")
except webtech.utils.ConnectionException:
    print("\n[-] Check URL or Network Connectivity and try again.\n")
except:
    print("[-] Reset all and try again.")