from utils import is_permutation, timeit

"""
It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain
the same digits.
"""


@timeit
def solution():
	x = 125870
	while True:
		x_set = set(str(x))
		multiples = [x*2, x*3, x*4, x*5, x*6]
		if all([set(str(x)) == x_set for x in multiples]):
			print(x, multiples)
			break
		x += 1


if __name__ == '__main__':
	solution()
