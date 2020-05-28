"""
__author__      = "Mohammad Mirian"
__copyright__   = "Free of charge - 1/5/2020"
__version__     = "1.0.1"
__maintainer__  = "Online training, Jadi Mirmiraie"
__email__       = "mohammad.mirian12@gmail.com"
__status__      = "Education"

"""
import math
md = []


def get_value():
    for i in range(1, 20):
        value = int(input())
        if value % i == 0:
             ch = 0
        else:
            md.append(value)
    return max(md)


def maxPrimeFactors(n):
    maxPrime = -1

    while n % 2 == 0:
        maxPrime = 2
        n >>= 1
    for i in range(3, int(math.sqrt(n)) + 1, 1):
        while n % i == 0:
            maxPrime = i
            n = n / i
    return int(maxPrime)


n = get_value()
m = maxPrimeFactors(n)
print()
print(n, m)

