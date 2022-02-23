from math import sqrt

from utils import generate_primes_under


def solution(n):
	sqrt_n = sqrt(n)
	half_n = int(n/2)
	primes = [x for x in generate_primes_under(half_n)]
	c1 = len([x for x in primes if x <= sqrt_n])
	print('squares count', c1)

	c2 = 0
	for prime in primes:
		limit = int(n/prime)
		r = [x for x in primes if x >= prime and x <= limit]
		if len(r) <= 1:
			break
		print(r)
		c2 += len(r) - 1

	total_count = c1+c2
	print(f"total count: {c1 + c2}")


if __name__ == "__main__":
	solution(34)
	# solution(10**8)
