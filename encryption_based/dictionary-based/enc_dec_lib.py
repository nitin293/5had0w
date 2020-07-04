#!/usr/bin/env python


data_dict = {
    'A': '..-.-..',
    'B': '.-.-.-.',
    'C': '...-....',
    'D': '.--.---',
    'E': '...-...',
    'F': '.-.---.',
    'G': '..-..--',
    'H': '....---',
    'I': '...---.',
    'J': '---.-.-.--.',
    'K': '--.--.-...-.-',
    'L': '--..--.---.---',
    'M': '.-.--.-.---...',
    'N': '.-.--...--.-',
    'O': '.-...-.-...-',
    'P': '.-.-.-.----.-',
    'Q': '.-.-..---.-',
    'R': '.-.-..--.-',
    'S': '..-.--.-.--',
    'T': '--..--.-..',
    'U': '--.--....-',
    'V': '..-.-...-..',
    'W': '-..-.-...-',
    'X': '--....-.-',
    'Y': '-..-.-.--..-',
    'Z': '-..-.-...-.',

    'a': '-.-.....-.-.----',
    'b': '-.-...--.-.---.-.----',
    'c': '-.-..--...-...-.----',
    'd': '-.-.....-.-.--.-..-',
    'e': '-.-.....-.-.--..---',
    'f': '-.-.....-.-.---..-',
    'g': '-.-.....-.---.-.----',
    'h': '-.-.....----.-.----',
    'i': '-.-..--...-..-.-.----',
    'j': '-.-..--.-.-.-.----',
    'k': '-.-...-.-.-.-.----...',
    'l': '-.-..--..-.-.----',
    'm': '-.-..--.-...-.-.----',
    'n': '-.-..-..--.-.-.----',
    'o': '-.-..-.-.-.-.----',
    'p': '-.-.--....-.-.----',
    'q': '-......-.-.----',
    'r': '-.-...-.-.---.....-',
    's': '-.-...-.-.-.-.----',
    't': '-.-......--.----',
    'u': '-.-....--.-.-.----',
    'v': '-.-....--.----',
    'w': '-.-..--...-.-.----',
    'x': '-.-...-.-.----',
    'y': '-.-.....-.---',
    'z': '-.-.....-.-..',

    '0': '-...-.-',
    '1': '---.-.',
    '2': '.-.---..',
    '3': '.-...-',
    '4': '-..-..',
    '5': '-.-.-',
    '6': '-.---.-',
    '7': '--.-..-',
    '8': '.-.-..-',
    '9': '-..-...-',

    ' ': '--',
    '~': '.--',
    '`': '..-.',
    '!': '-.-.---',
    '@': '.-..',
    '#': '-.-.',
    '$': '...--',
    '%': '---.',
    '^': '-.-',
    '&': '--....',
    '*': '--..',
    '(': '--.-',
    ')': '-...-',
    '-': '-.---',
    '_': '.-..--',
    '+': '-....-',
    '=': '----.....-.-.-',
    '{': '--..-.-..-',
    '[': '--......-.-.',
    '}': '--..-.-.-..',
    ']': '--.-...--.-',
    '|': '---..-.-',
    '\\': '...-.----.-',
    '"': '-----..-.',
    "'": '--...-.--.',
    ':': '-...-.-..',
    ';': '--.--..-',
    '<': '--.-...-',
    ',': '-.....-.-',
    '>': '--...-',
    '.': '--.-.-.----.--',
    '?': '--....--.',
    '/': '...--...-.-..'
}


def encryptor(text):
    encrypted_text = ""
    for letter in text:
        encrypted_text = encrypted_text + data_dict.get(letter) + " "
    return encrypted_text


def decryptor(cipher_text):
    cipher_text += " "
    keys = list(data_dict.keys())
    values = list(data_dict.values())

    enc_letter = ""
    raw_text = ""

    for element in cipher_text:
        space_count = 0
        if element != " ":
            enc_letter += element       #   if no space found, combine the cipher element
        else:
            space_count += 1
            if space_count == 1:
                raw_text = raw_text + keys[values.index(enc_letter)]    #   if space found = 1, decrypt 1st cipher to etxt and add the 2nd cipher
                enc_letter = ""         #   empty the enc_letter variable
            else:
                pass
    return raw_text

#-----------------------------------------------------------------------------------------------------------------------------------------

letter_list = []
for i in range(0, 999999):
    letter_list.append(chr(i))


def get_key(password):
    pass_list = list(password)

    ascii_value = []
    for element in pass_list:
        ascii_value.append(ord(element))

    sum_ = list(str(sum(ascii_value)))

    key_element = []
    for integer in sum_:
        key_element.append(int(integer))
    return sum(key_element)

def modified_text(text):
    return text.replace(" ", "")  # remove space

def encrypt_algo(text_to_encrypt, key):
    encrypted_list = []

    for letter in text_to_encrypt:
        letter_index = letter_list.index(letter)
        encrypted_index_algo = 2 * key - letter_index
        encrypted_list.append(letter_list[encrypted_index_algo])

    for space_index in space_indeices:
        encrypted_list.insert(space_index, " ")

    return "".join(encrypted_list)

def decrypt_algo(text_to_encrypt, key):
    decrypted_list = []

    for letter in text_to_encrypt:
        letter_index = letter_list.index(letter)
        decrypted_index_algo = 2 * key - letter_index
        decrypted_list.append(letter_list[decrypted_index_algo])

    for space_index in space_indeices:
        decrypted_list.insert(space_index, " ")

    return "".join(decrypted_list)