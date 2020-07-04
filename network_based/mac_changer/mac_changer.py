#!/usr/bin/env pyhton

import net_lib as nl
import subprocess
import random
from random import randint
import time
import sys

subprocess.call(["clear ; figlet mac changer"], shell=True)
print("\t\t\t\t\t\tA script by SHADOW\n===================================================================\n")
print("[+] Run The Application as ROOT.\n")

try:
    interface = input("Enter interface: ")

    print("\n\nChooce your option:\n\n\t\t(1) Chane MAC of your choice.\n\t\t(2) Change MAC in time interval.\n\t\t(3) Exit.")
    choice = int(input("\nEnter your choice: "))

    if choice==1:
        new_mac = input("Enter new MAC Address: ")
        nl.change_mac(interface, new_mac)
        print("[+] Changing MAC to : " + new_mac)


    elif choice==2:
        time_interval = int(input("Enter time interval (in seconds): "))

        while True:
            list0 = ['a', 'c', 'd', 'e']
            list1 = ['a', 'b', 'c', 'd', 'e', 'f']

            new_mac0 = str(randint(1, 9)) + random.choice(list0) + ":" + str(randint(10, 99)) + ":" + str(randint(10, 99)) + ":" + str(randint(10, 99)) + ":" + str(randint(10, 99)) + ":" + str(randint(10, 99))
            # format:    1a:22:33:11:22:33

            new_mac1 = str(randint(1, 9)) + random.choice(list0) + ":" + str(randint(1, 9)) + random.choice(list1) + ":" + str(randint(10, 99)) + ":" + str(randint(10, 99)) + ":" + str(randint(10, 99)) + ":" + str(randint(10, 99))
            # format:    1a:2b:33:11:22:33

            new_mac2 = str(randint(1, 9)) + random.choice(list0) + ":" + str(randint(1, 9)) + random.choice(list1) + ":" + str(randint(1, 9)) + random.choice(list1) + ":" + str(randint(10, 99)) + ":" + str(
                randint(10, 99)) + ":" + str(randint(10, 99))
            # format:    1a:2b:3c:11:22:33

            new_mac3 = str(randint(1, 9)) + random.choice(list0) + ":" + str(randint(1, 9)) + random.choice(list1) + ":" + str(randint(1, 9)) + random.choice(list1) + ":" + str(randint(1, 9)) + random.choice(list1) + ":" + str(randint(10, 99)) + ":" + str(randint(10, 99))
            # format:    1a:2b:3c:4d:22:33

            new_mac4 = str(randint(1, 9)) + random.choice(list0) + ":" + str(randint(1, 9)) + random.choice(
                list1) + ":" + str(randint(1, 9)) + random.choice(list1) + ":" + str(randint(1, 9)) + random.choice(list1) + ":" + str(randint(1, 9)) + random.choice(list1) + ":" + str(randint(10, 99))
            # format:    1a:2b:3c:4d:5e:33

            new_mac5 = str(randint(1, 9)) + random.choice(list0) + ":" + str(randint(1, 9)) + random.choice(
                list1) + ":" + str(randint(1, 9)) + random.choice(list1) + ":" + str(randint(1, 9)) + random.choice(list1) + ":" + str(randint(1, 9)) + random.choice(list1) + ":" + str(randint(1, 9)) + random.choice(list1)
            # format:    1a:2b:3c:4d:5e:6f

            mac_list = [new_mac0, new_mac1, new_mac2, new_mac3, new_mac4, new_mac5]
            random_mac = random.choice(mac_list)

            nl.change_mac(interface, random_mac)
            print("[+] Changing MAC to : " + random_mac)
            time.sleep(time_interval)

    elif choice==3:
        print("\n\n[-] Shutting Down...\n")
        exit()


    else:
        print("\n[-] Wrong input!")

except KeyboardInterrupt:
    print("\n\n[-] Ctrl+C detected!")