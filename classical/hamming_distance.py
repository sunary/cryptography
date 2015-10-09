__author__ = 'sunary'


class HammingDistance():

    def __init__(self):
        pass

    def distance(self, t1, t2):
        dt = 0
        for i in range(len(t1)):
            dt += self._count_bit1(ord(t1[i])^ord(t2[i]))

        return dt

    def _count_bit1(self, bit):
        count = 0
        while(bit > 0):
            count += (bit - ((bit >>1) << 1))
            bit >>= 1
        return count

if __name__ == '__main__':
    distance = HammingDistance()
    print distance.distance('this is a test', 'wokka wokka!!!')