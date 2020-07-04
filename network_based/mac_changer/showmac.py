#!/usr/bin/env python3

import subprocess
import time

iface = input("Enter interface : ")
time_intvl = int(input("Enter time interval (in seconds) : "))

print("\n\n")

while True:
	subprocess.call(["ifconfig " + iface + " | grep ether"], shell=True)
	time.sleep(time_intvl)
