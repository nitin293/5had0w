#!/usr/bin/env python

from random import randint
import subprocess
import time

subprocess.call(["clear ; figlet NumRem"], shell=True)
print("\t\t\t\tA CLI based number game by SHADOW\n===================================================================")


try:
    print("\n\n\t\t\tWelcome to NumRem.\n\n\t\t\t   Description\n\nThis is a CLI(Command Line Interface) based number remembering game.\nAccording to your chosen level, you will be displayed a number for\na few seconds and you have to remember it. Thereafter the number will\nbe removed and you have to input that number on given place.\n\n\t\tDo you want to enter the game?")
    option0 = input("\n\t\tEnter your choice(Y/N): ")

    if option0=='Y' or option0=='y':
        subprocess.call(["clear ; figlet NumRem"], shell=True)
        print("\t\t\t\tA CLI based number game by SHADOW\n===================================================================")

        print("\n\n\t\t\tWelcome\n\t\t\t-------\n\nDifficulty level:\n\t\t(1) Easy\n\t\t(2) Medium\n\t\t(3) Hard")
        level = input("Enter Option: ")


        def random_numbers(lower_range, upper_range):
            integer = []
            integer.append(randint(lower_range, upper_range))
            return integer

        if level=='1':
            try:
                while True:
                    subprocess.call(["clear ; figlet NumRem"], shell=True)
                    print("\t\t\t\tA CLI based number game by SHADOW\n===================================================================\n\n\t\t\t[+] Press Ctrl+C to quit.")

                    random_number = random_numbers(1000,9999)[0]
                    print("\n\n\t\t\tThe number is: ", random_number)
                    time.sleep(2)

                    subprocess.call(["clear ; figlet NumRem"], shell=True)
                    print("\t\t\t\tA CLI based number game by SHADOW\n===================================================================\n\n\t\t\t[+] Press Ctrl+C to quit.")

                    input_number = int(input("\n\n\t\t\tEnter the number: "))

                    if random_number==input_number:
                        print("\t\t\t\t[+] Great!")
                    else:
                        print("\t\t\t   [-] Wrong Answer !")
                    time.sleep(3)

            except KeyboardInterrupt:
                print("\n\t\t\t!---Bye Bye---!")
            except ValueError:
                print("\n\t\t[-] Numeric value accepted only.")


        elif level=='2':
            try:
                while True:
                    subprocess.call(["clear ; figlet NumRem"], shell=True)
                    print(
                        "\t\t\t\tA CLI based number game by SHADOW\n===================================================================\n\n\t\t\t[+] Press Ctrl+C to quit.")

                    random_number = random_numbers(10000, 999999)[0]
                    print("\n\n\t\t\tThe number is: ", random_number)
                    time.sleep(4)

                    subprocess.call(["clear ; figlet NumRem"], shell=True)
                    print(
                        "\t\t\t\tA CLI based number game by SHADOW\n===================================================================\n\n\t\t\t[+] Press Ctrl+C to quit.")

                    input_number = int(input("\n\n\t\t\tEnter the number: "))

                    if random_number == input_number:
                        print("\t\t\t\t[+] Great!")
                        time.sleep(3)
                    else:
                        print("\t\t\t   [-] Wrong Answer !")
                        time.sleep(3)

            except KeyboardInterrupt:
                print("\n\t\t\t!---Bye Bye---!")
            except ValueError:
                print("\n\t\t[-] Numeric value accepted only.")


        elif level=='3':
            try:
                while True:
                    subprocess.call(["clear ; figlet NumRem"], shell=True)
                    print(
                        "\t\t\t\tA CLI based number game by SHADOW\n===================================================================\n\n\t\t\t[+] Press Ctrl+C to quit.")

                    random_number = random_numbers(1000000, 9999999999)[0]
                    print("\n\n\t\t\tThe number is: ", random_number)
                    time.sleep(6)

                    subprocess.call(["clear ; figlet NumRem"], shell=True)
                    print(
                        "\t\t\t\tA CLI based number game by SHADOW\n===================================================================\n\n\t\t\t[+] Press Ctrl+C to quit.")

                    input_number = int(input("\n\n\t\t\tEnter the number: "))

                    if random_number == input_number:
                        print("\t\t\t\t[+] Great!")
                        time.sleep(3)
                    else:
                        print("\t\t\t   [-] Wrong Answer !")
                        time.sleep(3)

            except KeyboardInterrupt:
                print("\n\t\t\t!---Bye Bye---!")
            except ValueError:
                print("\n\t\t[-] Numeric value accepted only.")


        else:
            print("[-] Wrong Input")

    elif option0=='N' or option0=='n':
        print("\n\t\t\t!!!---Bye Bye---!!!")

    else:
        print("[-] Wrong input.")

except KeyboardInterrupt:
    print("[-] Ctrl+C detected !")
except:
    pass