from math import sqrt
import time

test = 'Hello...'

def sieve_of_eratosthenes(n):
	# Create a boolean array "prime[0..n]" and 
	# initialize all entries it as true. A value 
	# in prime[i] will finally be false if i is 
	# Not a prime, else true. 

	"""
	t0 = time.time() 
	c = sieve_of_eratosthenes(100000)
	print("Total prime numbers in range:", c) 

	t1 = time.time() 
	print("Time required:", t1 - t0)

	"""
	prime = [True for i in range(n+1)] 
	
	p = 2
	while(p * p <= n): 
		
	# If prime[p] is not changed, then it is a prime 
		if (prime[p] == True): 
			
			# Update all multiples of p 
			for i in range(p * 2, n + 1, p): 
				prime[i] = False
		p += 1
	c = 0
	# Print all prime numbers
	for p in range(2, n): 
		if prime[p]: 
			c += 1
	return c 


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

