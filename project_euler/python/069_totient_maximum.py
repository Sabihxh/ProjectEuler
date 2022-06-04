from math import gcd

"""
Problem:

Euler's Totient function, φ(n) is used to determine the number of numbers
less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8,
are all less than nine and relatively prime to nine, φ(9)=6.

n   Relatively Prime    φ(n)    n/φ(n)
2   1                   1       2
3   1,2                 2       1.5
4   1,3                 2       2
5   1,2,3,4             4       1.25
6   1,5                 2       3
7   1,2,3,4,5,6         6       1.1666...
8   1,3,5,7             4       2
9   1,2,4,5,7,8         6       1.5
10  1,3,7,9             4       2.5

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

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


def solution(N=10**6):
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
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))


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
    sol = solution2(10**7)
    print(f"solution: {sol}")
    pass
