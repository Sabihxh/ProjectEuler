from is_prime_function import is_prime
from time import sleep



def solution():
	max_count = 1
	ab = []
	for a in range(-999, 1000, 1):
		for b in range(-1000, 1001, 1):
			count = 0
			n = 0
			value = n**2 + a*n + b
			while is_prime(value):
				count += 1
				n += 1
				value = n**2 + a*n + b
			
			else:
				if count > max_count:
					max_count = count
					ab = [a, b]

	print ab, max_count
	return ab, max_count, ab[0] * ab[1]


solution()


