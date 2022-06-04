from math import gcd
from typing import Set
from fractions import Fraction

from utils import distinct_prime_factors, is_permutation, timeit

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


def phi(n: int) -> int:
    dpfs = distinct_prime_factors(n)
    t = 1
    for p in dpfs:
        t = t * (Fraction(p - 1, p))
    return int(n * t)


def test_phi():
    n_and_phi_n = [(10, 4), (97, 96), (9798, 3080), (9708131, 9701832)]
    for n, expected_phi_n in n_and_phi_n:
        phi_n = phi(n)
        print(f"n: {n}, expected_phi_n: {expected_phi_n}, phi_n: {phi_n}")
        assert phi(n) == expected_phi_n


test_phi()


@timeit
def solution(N=10**7):
    """
    Psuedocode:
        - loop through all numbers under 10**7
        - for each number, calculate Euler's Totient function, φ(n)
        - if number and its φ(n) are not a permutation, skip
        - else check if the ratio is minimum, if so, store the minimum
        - print out the number with minimum ratio, at the end of the loop

    Takes over 6 mins to run...too slow
    """
    min_ratio = 10
    result = 0
    for n in range(2, N + 1):
        phi_n = phi(n)
        if not is_permutation(n, phi_n):
            continue
        ratio = n / phi_n
        if ratio < min_ratio:
            min_ratio, result = ratio, n
            print(f"phi({n}) = {phi_n}, ratio = {ratio}")

    return result


if __name__ == "__main__":
    sol = solution(10**6)
    print(f"solution: {sol}")
    pass
