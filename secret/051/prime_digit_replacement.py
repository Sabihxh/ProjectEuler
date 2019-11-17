from itertools import combinations 
import pickle
import math
import time

from pixie.primes import generate_primes_under
from pixie.utilities import timeit


@timeit
def pickle_load():
	with open('primes_10,000,000.pkl', 'rb') as f:
		return pickle.load(f)


all_primes = pickle_load()


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
				tmp_prime[position] = '*'

			if len(set([prime_list[p] for p in positions])) == 1:
				prime_str = ''.join(tmp_prime)
				if prime_str not in m:
					m[prime_str] = []

				m[prime_str].append(prime)

	for k, v in m.items():
		if len(v) == target_prime_family:
			print(v)
			return v[0]


solution(prime_digits=5, replace_digits=1, target_prime_family=6)
solution(prime_digits=5, replace_digits=2, target_prime_family=7)
solution(prime_digits=6, replace_digits=3, target_prime_family=8)








