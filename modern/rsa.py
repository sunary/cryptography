__author__ = 'sunary'


class RSA():

    def __init__(self, p, q, e=65537):
        self.n = p * q
        self.e = e
        self.d = self.modular_inverse(self.e, self.f_totient(p, q))

    def modular_inverse(self, e, totient):
        '''
        totient*x mod e = 1
        '''
        i = 0
        while True:
            if (1 + totient*i) % e == 0:
                return (1 + totient*i)/e
            i += 1

    def f_totient(self, p, q):
        return (p - 1) * (q - 1)

    def encrypt(self, input):
        '''
        public key is (n, e)
        '''
        return self.mod_pow(input, self.e, self.n)

    def decrypt(self, input):
        '''
        private key is (d)
        '''
        return self.mod_pow(input, self.d, self.n)

    def mod_pow(self, x, y, z):
        '''
        modular of power
        '''
        c = x % z
        i = 1
        while i < y:
            c = (c * x) % z
            i += 1

        return c


if __name__ == '__main__':
    rsa = RSA(61, 53)
    print rsa.decrypt(rsa.encrypt(1290))