__author__ = 'sunary'

class Base64():

    def __init__(self):
        self.base64_chars = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')

    def _base64_value(self, char):
        for i in range(len(self.base64_chars)):
            if(char == self.base64_chars[i]):
                return i
        return 0

    def encrypt(self, text):
        base64 = ''
        i = 0
        while(i < len(text) - 2):
            t = (ord(text[i]) << 16) | (ord(text[i + 1]) << 8) | ord(text[i + 2])
            t1 = ((t & 0b111111000000000000000000) >> 18)
            t2 = ((t & 0b111111000000000000) >> 12)
            t3 = ((t & 0b111111000000) >> 6)
            t4 = (t & 0b111111)
            base64 += self.base64_chars[t1] + self.base64_chars[t2] + self.base64_chars[t3] + self.base64_chars[t4]
            i = i + 3

        if(len(text) - i == 2):
            t = (ord(text[i]) << 16) | (ord(text[i + 1]) << 8)
            t1 = ((t & 0b111111000000000000000000) >> 18)
            t2 = ((t & 0b111111000000000000) >> 12)
            t3 = ((t & 0b111111000000) >> 6)
            base64 += self.base64_chars[t1] + self.base64_chars[t2] + self.base64_chars[t3] + "="
        elif(len(text) - i == 1):
            t = (ord(text[i]) << 16)
            t1 = ((t & 0b111111000000000000000000) >> 18)
            t2 = ((t & 0b111111000000000000) >> 12)
            base64 += self.base64_chars[t1] + self.base64_chars[t2] + "=="
        return base64

    def decrypt(self, base64):
        base64 += 'AAA'
        byte = []
        i = 0
        while(i < len(base64) - 3):
            t = (self._base64_value(base64[i]) << 18) | (self._base64_value(base64[i + 1]) << 12) | (self._base64_value(base64[i + 2]) << 6) | self._base64_value(base64[i + 3])
            t1 = t >> 16
            t2 = (t >> 8) - ((t >> 16) <<8)
            t3 = t - ((t >> 8) << 8)
            byte.append(t1)
            byte.append(t2)
            byte.append(t3)
            i += 4

        if('==' in base64):
            byte = byte[0:len(byte) - 2]
        elif('=' in base64):
            byte = byte[0:len(byte) - 1]

        text = ''
        for i in range(len(byte)):
            text += chr(byte[i])
        return text

if __name__ == '__main__':
    base64 = Base64()
    print base64.encrypt('any carnal pleasure')
    print base64.decrypt('YW55IGNhcm5hbCBwbGVhc3VyZQ==')