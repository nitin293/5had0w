#!/ur/bin/env python

import subprocess


def change_mac(interface, new_mac):
    subprocess.call(["ifconfig " + interface + " down"], shell=True)
    subprocess.call(["ifconfig " + interface + " hw ether " + new_mac], shell=True)
    subprocess.call(["ifconfig " + interface + " up"], shell=True)
