#!/usr/bin/env python

import subprocess
import enc_dec_lib as ndl

subprocess.call(["clear; figlet SHADOW"], shell=True)
print("\t\t\t\t\t\tA script by SHADOW\n==================================================================")
print("\n\nChooce your option:\n\n\t\t(1) Encryptor\n\t\t(2) Decryptor\n\t\t(3) Exit")

try:
    option = input("\nEnter your choice: ")

    if option=='1':
        input_text = input("Enter your text to encrypt: ")

        print("Your cipher text is: ", ndl.encryptor(input_text), "\n")

    elif option=='2':
        try:
            cipher_text = input("Enter cipher text: ")
            print("Your raw text is: ", ndl.decryptor(cipher_text), "\n")

        except ValueError:
            print("[-] Wrong cipher.")

    elif option=='3':
        exit()

    else:
        print("\n[-] Wrong Input! Shutting the program...")


except KeyboardInterrupt:
    print("\n[-] Ctrl+C detected!")
