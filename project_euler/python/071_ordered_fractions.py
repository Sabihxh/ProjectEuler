"""https://projecteuler.net/problem=71

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.

"""
from math import gcd
import time


def solution(D: int = 10**6):
    smallest_difference = 0.5
    solution = (0, 0)
    for d in range(2, D+1):
        numerator_limit_from = int( d * (3/7) - smallest_difference )
        numerator_limit_to = int( d * (3/7) )
        for n in range(numerator_limit_from, numerator_limit_to+1):
            if n == 3 and d == 7: continue
            if gcd(n, d) == 1:
                difference = (3/7) - (n/d)
                if difference < smallest_difference:
                    smallest_difference = difference
                    solution = (n, d)
    print(solution)

def main(D):
    t1 = time.perf_counter()
    solution(D)
    t2 = time.perf_counter()
    print(f'Elapsed time: {(t2-t1):0.4f} sec')

if __name__ == '__main__':
    main(D=10**6)