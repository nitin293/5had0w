import hashlib

class CryptoSys:

    def gen_md5(self, password):
        hash = hashlib.md5(password.encode())

        return hash.hexdigest()


    def gen_key(self, password_hash):
        sum = 0
        length = len(password_hash)

        for char in password_hash:
            sum += ord(char)

        key = sum % length

        return key

    
    def encrypt_data(self, string, password):
        crypt = CryptoSys()

        charecters = []

        for i in range(32,127):
            charecters.append(chr(i))

        password_hash = crypt.gen_md5(password)
        key = crypt.gen_key(password_hash)

        password_hash = crypt.gen_md5(password_hash + str(key))
        key = crypt.gen_key(password_hash)

        cipher = ""

        for char in string:
            cipher += charecters[charecters.index(char) - key]

        return cipher


    def decrypt_data(self, cipher, password):
        crypt = CryptoSys()

        charecters = []

        for i in range(32,127):
            charecters.append(chr(i))

        password_hash = crypt.gen_md5(password)
        key = crypt.gen_key(password_hash)

        password_hash = crypt.gen_md5(password_hash + str(key))
        key = crypt.gen_key(password_hash)

        dec_string = ""

        for char in cipher:
            if char:
                index = charecters.index(char) + key

                if index > len(charecters):
                    index = index - len(charecters)

                dec_string += charecters[index]

        return dec_string


if __name__ == '__main__':
    crypt = CryptoSys()

    t = input("Enter E/D :")

    if t == 'E' or t == 'e':
        string = input("Enter cipher :")
        password = input("Enter password :")
        enc = crypt.encrypt_data(string, password)

        print(enc)

    elif t == 'D' or t == 'd':
        cipher = input("Enter cipher :")
        password = input("Enter password :")
        dec = crypt.decrypt_data(cipher, password)

        print(dec)
