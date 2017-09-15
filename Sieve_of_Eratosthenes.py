# Calculation of the prime numbers between 1 and 100 using the sieve
#  of Eratosthenes:
# using set comprehension to avoid duplicates

from math import sqrt

n = 100
sqrt_n = int(sqrt(n))

non_primes = {j for i in range(2, sqrt_n) for j in range(i*2, n, i)}
print non_primes

primes = {i for i in range(2, n) if i not in non_primes}
print primes


# recursive implementation

print "/nRecursive implementation"

def primes(n):
    if n == 0 or n ==1:
        return []
    else:
        p = primes(int(sqrt(n)))
        no_p = {j for i in p for j in range(i*2, n+1, i)}
        p = {i for i in range(2, n+1) if i not in no_p}
    return p

for i in range(1, 100):
    print i, primes(i)



