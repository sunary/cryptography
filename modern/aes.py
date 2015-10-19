__author__ = 'sunary'


from Crypto.Cipher import AES
from base64 import standard_b64encode, standard_b64decode


class AESCipher():

    def __init__(self):
        pass

    def encrypt(self):
        key = "abcdefghijklmnop"
        en = AES.new(key, AES.MODE_CFB, "0000000000000000")
        cipher = en.encrypt("apple")
        return standard_b64encode(cipher)

    def decrypt(self):
        key = "abcdefghijklmnop"
        en = AES.new(key, AES.MODE_CFB, "0000000000000000")
        cipher = en.decrypt(standard_b64decode("WqF9Zj0="))
        return cipher

if __name__ == '__main__':
    aes = AESCipher()
    print aes.encrypt()
    print aes.decrypt()
