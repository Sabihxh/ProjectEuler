"""
Solution to this problem:
    https://projecteuler.net/problem=85
"""

LIMIT = 2000000
def count_rectangles(m, n):
    total = 0
    for x in range(1, m+1):
        for y in range(1, n+1):
            total += (m-x+1)*(n-y+1)
    return total


def solution():
    min_difference = LIMIT
    area = 0
    for m in range(1, 200):
        for n in range(m, 200):
            difference = abs(LIMIT - count_rectangles(m, n))
            if difference < min_difference:
                min_difference = difference
                area = m*n
                print(m, n, difference, area)

solution()