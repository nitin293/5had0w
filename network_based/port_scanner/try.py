#!/usr/bin/python3

import socket
import threading
import time
import os


host = input("Enter hostname : ")


port_list = []

def get_ip(host):
    return socket.gethostbyname(host)

def scan(hostname, port):
    print("\r[!] Scanning for Open Port : {}".format(port), end="")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    closed = s.connect_ex((hostname, port))

    if not closed:
        print("\t[+] Open Port Found : {}".format(port))
        port_list.append(port)

    s.close()

def get_services(port_list):
    service_list = []

    for port in port_list:
        try:
            service_list.append(socket.getservbyport(port, 'tcp'))
            time.sleep(1)
        except OSError:
            service_list.append("Unknown")

    return service_list

def print_result(port_list, service_list):
    os.system("clear")

    if len(port_list) != 0:
        print("\nPort\t\tState\t\tService\n")
        for i in range(len(port_list)):
            if len(str(port_list[i])) < 4:
                print(str(port_list[i]) + "/tcp\t\tOpen\t\t" + service_list[i])
            else:
                print(str(port_list[i]) + "/tcp\tOpen\t\t" + service_list[i])

        print("[+] Finished !")

    else:
        print("\n[-] No Open Ports Found !")



if __name__ == '__main__':
    hostname = get_ip(host)

    for i in range(0, 64001, 1500):
        for port in range(i, i+1001):
            thread = threading.Thread(target=scan, args=(hostname, port,))
            thread.start()
        time.sleep(3)

    for i in range(64035, 64536, 500):
        for port in range(i, i+535):
            thread = threading.Thread(target=scan, args=(hostname, port,))
            thread.start()
        time.sleep(2)

    port_list = sorted(port_list)
    service_list = get_services(port_list)

    print_result(port_list, service_list)