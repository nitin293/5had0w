#!/usr/bin/env python

import subprocess
import getpass
import mod_shadow as ms

subprocess.call(["clear; figlet 5h@DoW"], shell=True)
print("\t\t\t\t\t\tA script by SHADOW\n==================================================================")
print("\n\nChooce your option:\n\n\t\t(1) Upload File\n\t\t(2) Normal Text\n\t\t(3) Exit")

try:
    input_type = input("\nEnter your choice: ")

    if input_type=='1':
        subprocess.call(["clear; figlet 5h@DoW"], shell=True)
        print("\t\t\t\t\t\tA script by SHADOW\n==================================================================")
        print("\n\nChooce your option:\n\n\t\t(1) Encryptor\n\t\t(2) Decryptor\n\t\t(3) Exit")

        option = input("\nEnter your choice: ")

        if option=='1':
            try:
                input_file = input("Input raw file name along with directory : ")
                password = getpass.getpass("Enter password: ")
                output_file = input("Input the encrypted file name along with directory : ")
                key = ms.get_key(password)

                subprocess.call(["rm " + output_file], shell=True)

                with open(input_file, "r") as in_file:
                    for line in in_file:
                        output_text = ms.algo(line, key)

                        with open(output_file, "a") as out_file:
                            out_file.write(output_text + "\n")
                            out_file.close()

                print("[+] Your file is successfully writen to >", output_file)

            except FileNotFoundError:
                print("[-] No file named", input_file)
            except ValueError:
                print("[-] Some charecters are not included in the list.")

        elif option=='2':
            try:
                input_file = input("Input raw file name along with directory : ")
                password = getpass.getpass("Enter password: ")
                output_file = input("Input the encrypted file name along with directory : ")
                key = ms.get_key(password)

                subprocess.call(["rm " + output_file], shell=True)

                with open(input_file, "r") as in_file:
                    for line in in_file:
                        output_text = ms.algo(line, key)

                        with open(output_file, "a") as out_file:
                            out_file.write(output_text + "\n")
                            out_file.close()

                print("[+] Your file is successfully writen to >", output_file)

            except FileNotFoundError:
                print("[-] No file named", input_file)
            except ValueError:
                print("[-] Some charecters are not included in the list.")

        elif option=='3':
            print("\n[+]  Thank You ! Have a nice day !")
            exit()

        else:
            pass


    elif input_type=='2':
        subprocess.call(["clear; figlet 5h@DoW"], shell=True)
        print("\t\t\t\t\t\tA script by SHADOW\n==================================================================")
        print("\n\nChooce your option:\n\n\t\t(1) Encryptor\n\t\t(2) Decryptor\n\t\t(3) Exit")

        option = input("\nEnter your choice: ")

        if option=='1':
            try:
                input_text = input("Enter text: ")
                password = getpass.getpass("Password: ")

                key = ms.get_key(password)

                output_text = ms.algo(input_text, key)
                print("[+] Your output is: " + str(output_text))
            except ValueError:
                print("[-] Some charecters are not included in the list.")

        elif option=='2':
            try:
                input_text = input("Enter text: ")
                password = getpass.getpass("Password: ")

                key = ms.get_key(password)

                output_text = ms.algo(input_text, key)
                print("[+] Your output is: " + str(output_text))

            except ValueError:
                print("[-] Wrong cipher.")

        elif option=='3':
            print("\n[+]  Thank You ! Have a nice day !")
            exit()

        else:
            print("\n[-] Wrong Input! Shutting the program...")


    elif input_type=='3':
        exit()
    else:
        print("\n[-] Wrong Input! Shutting the program...")

except KeyboardInterrupt:
    print("\n[-] Ctrl+C detected!")