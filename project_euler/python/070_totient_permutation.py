from math import gcd

"""
Euler's Totient function, φ(n) [sometimes called the φ function], is used
to determinethe number of positive numbers less than or equal to n which are
relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than
nine and relatively prime to nine, φ(9)=6.

The number 1 is considered to be relatively prime to every positive number,
so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation
of 79180.

Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and
the ratio n/φ(n) produces a minimum.

"""

"""
Solution:
https://www.dcode.fr/euler-totient

"""


def distinct_prime_factors(n):
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors


def coprime(a, b):
    return gcd(a, b) == 1


def phi(n):
    dpfs = distinct_prime_factors(n)
    t = 1
    for p in dpfs:
        t = t * (1 - (1 / p))
    return n * t


def solution(N=10 ** 6):
    max_ratio = 0
    result = 0
    for n in range(2, N + 1, 2):
        phi_n = phi(n)
        ratio = n / phi_n
        if ratio > max_ratio:
            max_ratio, result = ratio, n
            print(f"phi({n}) = {phi_n}, ratio = {ratio}")

    return result


def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))


def solution2(N):
    """See docs/069_overview.pdf"""
    prime_product = 2
    x = 3
    while prime_product * 2 <= N:
        if is_prime(x):
            prime_product *= x
            print(x, prime_product)
        x += 2

    return prime_product


if __name__ == "__main__":
    sol = solution2(10 ** 7)
    print(f"solution: {sol}")
    pass
