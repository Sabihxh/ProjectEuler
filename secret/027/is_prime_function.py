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
