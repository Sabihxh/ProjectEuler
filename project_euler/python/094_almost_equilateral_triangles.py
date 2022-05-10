import numpy as np
from math import sqrt


n = 10 ** 2


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def solution(limit):
    squares = {x ** 2: x for x in np.arange(2, int(sqrt(limit) + 1))}
    result = []
    for p_2 in squares:
        factors = prime_factors(p_2)
        if factors.count(2) > 1:
            continue

        if 2 in factors:
            factors.remove(2)

        for factor in factors:
            if factor % 4 != 1:
                break
        else:
            q_2 = 0.25 * ((squares[p_2] + 1) ** 2)
            if p_2 - q_2 in squares:
                result.append(p_2)

    result = [squares[x] + 1 for x in result]
    return result


print(solution(10 ** 9))
