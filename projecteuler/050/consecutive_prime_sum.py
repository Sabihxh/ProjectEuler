from math import sqrt



def is_prime(a_num):

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


def list_of_primes(limit): #returns a list of prime numbers below the limit

	primes_list = []

	for x in range(1, limit):
		if is_prime(x):
			primes_list.append(x)

	return primes_list


def consecutive_primes(prime_limit, num_limit):
	largest_primes_sum = {}
	primes = list_of_primes(prime_limit)
	primes_2 = primes
	for x in range(len(primes)):
		for y in primes_2:
			_sum = sum(primes_2[x:])
			if is_prime(_sum) and _sum < num_limit:
				largest_primes_sum[len(primes_2[x:])] = _sum
				primes_2 = primes
				break
			primes_2 = primes_2[:-1]
	y = 0
	for x in largest_primes_sum:
		if x > y: y = x
	print(y, largest_primes_sum[y])

	

consecutive_primes(4000, 1000000) 


print(sum(list_of_primes(4000))) #Test to see how many primes are needed to get sum ~ 1,000,000




