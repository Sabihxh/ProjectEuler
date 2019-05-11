from math import sqrt

def is_prime_slow(a_num):

	if a_num < 2:
		return False

	if a_num == 2:
		return True

	#return false for even numbers
	if not a_num & 1:
		return False

	limit = int(sqrt(a_num)) + 2
	for x in range(3, limit, 2):
		if a_num % x == 0:
			return False

	return True

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

def distinct_prime_factors(n):
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True


from fractions import gcd
def no_of_coprimes(n):
    """Finds the number of coprimes of n"""
    counter = 0
    if n == 1: return 1
    for x in range(1, n):
        if gcd(x, n) == 1:
            counter += 1

    return counter

