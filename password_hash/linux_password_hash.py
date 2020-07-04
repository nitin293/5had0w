#!/usr/bin/env python3

import crypt

text = input("Enter text : ")

def sha512(text):
    return crypt.crypt(text, crypt.mksalt(crypt.METHOD_SHA512))

def sha256(text):
    return crypt.crypt(text, crypt.mksalt(crypt.METHOD_SHA256))

def MD5(text):
    return crypt.crypt(text, crypt.mksalt(crypt.METHOD_MD5))

def Blowfish(text):
    return crypt.crypt(text, crypt.mksalt(crypt.METHOD_BLOWFISH))


print("\n[+] MD-5 :", MD5(text))
print("\n[+] Blowfish :", Blowfish(text))
print("\n[+] SHA-256 :", sha256(text))
print("\n[+] SHA-512 :", sha512(text), "\n")