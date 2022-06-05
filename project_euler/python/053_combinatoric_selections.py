from functools import reduce
from matplotlib import pyplot as plt
import operator as op


"""
https://projecteuler.net/problem=53
"""

# Function by https://stackoverflow.com/questions/4941753/is-there-a-math-ncr-function-in-python


def ncr(n, r):
    if r > n:
        return 0
    if r == 0:
        return 1
    numerator = reduce(op.mul, range(n, n - r, -1))
    denominator = reduce(op.mul, range(1, r + 1))
    return numerator // denominator


def solution(limit=100):
    c = 0
    for n in range(23, limit + 1):
        for r in range(2, n):
            if ncr(n, r) > 1000000:
                c += 1
                print(ncr(n, r))
    print(f"Number of values of nCr greater than 1000000: {c}")


# observation, printed ncr generates a waves of numbers
def list_of_ncr(limit=100):
    ncr_list = []
    for n in range(23, limit + 1):
        for r in range(2, n):
            if ncr(n, r) > 1000000:
                ncr_list.append(ncr(n, r))

    return ncr_list


if __name__ == '__main__':
    # get solution
    solution()

    # plot the ncr
    plt.plot(list_of_ncr()[:100])
    plt.ylabel("Pascal numbers > million")
    plt.show()

