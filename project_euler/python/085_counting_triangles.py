"""
Solution to this problem:
    https://projecteuler.net/problem=85
"""

import time
t1 = time.perf_counter()

LIMIT = 2000000

def count_rectangles(m, n):
    return int(((m*(m+1))/2) * ((n*(n+1))/2))

def solution():
    min_difference = LIMIT
    area = 0
    for m in range(1, 300):
        for n in range(m, 300):
            difference = abs(LIMIT - count_rectangles(m, n))
            if difference < min_difference:
                min_difference = difference
                area = m*n
                print(m, n, difference, area)

solution()

t2 = time.perf_counter()
print(f'Elapsed time: {(t2-t1):0.4f} sec')