def GreedyAlgorithm(amount):
    change = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.10, 0.05, 0.01]
    cashed = []
    i = 0
    while amount > 0:
        if amount >= change[i]:
            amount -= change[i]
            amount = round(amount, 2)
            cashed.append(change[i])
        else:
            i += 1
    return cashed

print(GreedyAlgorithm(232.32))

import math
def isprime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def highest_prime_factor(n):
    n = n // 2
    for i in range(n, 0, -1):
        if n % i == 0 and isprime(i):
            return i

z = highest_prime_factor(100)
print(z)

def Sum_of_multiples(n):
    sumn = 0
    i = 0
    while i < n:
        if i % 3 == 0 or i % 5 == 0:
            sumn += i
        i += 1
    return sumn

print(Sum_of_multiples(1000))


def LargestPrime(n):
    i = 2
    while n!= 1:
        if n % i == 0:
            n = n//i
        else:
            i += 1
    return i

print(LargestPrime(100))
