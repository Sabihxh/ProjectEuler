from itertools import combinations
import math

from utils import generate_primes_under, timeit


"""
https://projecteuler.net/problem=51

Problem 51 - Prime digit replacements

By replacing the 1st digit of the 2-digit number *3, it turns out that six of
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated numbers,
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest prime
with this property.

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family.

"""

# all_primes = pickle_load()
all_primes = generate_primes_under(10000000)


@timeit
def n_digit_primes(all_primes, n=2):
    return [x for x in all_primes if (len(str(x)) == n)]


@timeit
def solution(prime_digits=6, replace_digits=3, target_prime_family=8):
    m = {}
    primes = n_digit_primes(all_primes, n=prime_digits)
    for prime in primes:
        prime_list = list(str(prime))
        digits = len(prime_list)
        for positions in combinations(range(digits), replace_digits):
            tmp_prime = prime_list.copy()
            for position in positions:
                tmp_prime[position] = "*"

            if len(set([prime_list[p] for p in positions])) == 1:
                prime_str = "".join(tmp_prime)
                if prime_str not in m:
                    m[prime_str] = []

                m[prime_str].append(prime)

    for k, v in m.items():
        if len(v) == target_prime_family:
            print(v)
            return v[0]


solution(prime_digits=5, replace_digits=1, target_prime_family=6)
# solution(prime_digits=5, replace_digits=2, target_prime_family=7)
# solution(prime_digits=6, replace_digits=3, target_prime_family=8)
