from utils import is_prime

problem = """
Starting with 1 and spiralling anticlockwise in the following way,
a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal,
but what is more interesting is that 8 out of the 13 numbers lying along both diagonals
are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral
with side length 9 will be formed. If this process is continued, what is the side
length of the square spiral for which the ratio of primes along both diagonals first
falls below 10%?
"""

def is_prime(n):
	if n == 2 or n == 3:
		return True
	if n < 2 or n % 2 == 0:
		return False
	if n < 9:
		return True
	if n % 3 == 0:
		return False
	r = int(n ** 0.5)
	f = 5
	while f <= r:
		if n % f == 0:
			return False
		if n % (f + 2) == 0:
			return False
		f += 6
	return True


def solution():
	target_ratio = 0.1
	# coefficients of the 3 quadratic equations for non-squared diagonal numbers
	coefficients = [(4, -10, 7), (4, -8, 5), (4, -6, 3)]
	primes_count = 0
	for n in range(1, 100000):
		side_length = (2*n) - 1
		diagonal_count = (4*n) - 3
		print(f'n: {n}, side_length: {side_length}, diagonal_count: {diagonal_count}')
		for coeff in coefficients:
			a, b, c = coeff
			s = a*(n**2) + (b*n) + c
			print(f'coeff: {coeff}', s)
			if is_prime(s):
				primes_count += 1
		ratio = primes_count/diagonal_count
		print(f'primes_count: {primes_count}, diagonal_count: {diagonal_count} ratio: {ratio}')
		if n > 2 and ratio < target_ratio:
			print(f'side_length: {side_length}')
			break
		print('*'*100)


if __name__ == "__main__":
	solution()
