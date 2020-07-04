#!/usr/bin/env python3

from gtts import gTTS
import os
import subprocess
import optparse


try:
    def get_args():
        parser = optparse.OptionParser()
        parser.add_option("-f", "--file", dest="file", help="set filename")
        parser.add_option("-t", "--text", dest="text", help="set text")
        (options, arguments) = parser.parse_args()

        return options


    def read_line(name):
        print("[+] Reading the file... Please wait...\n\n")
        with open(name, "r") as readfile:
            for line in readfile:
                line = line.strip()
                text_to_voice(line)


    def text_to_voice(text):
        try:
            convert = gTTS(text, lang="en", slow=False)
            convert.save("./output/speak.mp3")
            print(text)
            os.system("mpg321 ./output/speak.mp3 -quiet")
            os.system("rm ./output/speak.mp3")
        except AssertionError:
            pass


    def pdf_converter(filename):
        name = filename.split(".")[0]
        command = "python3 ./converter/pdf2txt.py -o ./txt_files/" + name + ".txt" + " " + filename
        print("[+] Coverting to text file... Please wait...")
        subprocess.call([command], shell=True)
        print("[+] Process Completed Successfully !\n\n")
        read_line("./txt_files/" + name + ".txt")


    def detector(file):
        extention = file.split(".")[-1]
        extention_list = [
            "pdf", "PDF", "txt", "TXT"
        ]

        if extention==extention_list[0] or extention==extention_list[1]:
            pdf_converter(file)
        elif extention==extention_list[2] or extention==extention_list[3]:
            read_line(file)


    def main():
        options = get_args()
        filename = options.file
        text = options.text

        if filename:
            detector(filename)
        elif text:
            text_to_voice(text)
        else:
            print("[-] Missing argument.\nUse -h or --help for more info.\n")


    if __name__ == '__main__':
        main()


except KeyboardInterrupt:
    print("[-] Ctrl+C detected !\n")
except AssertionError:
    print("[-] No text found !\n")