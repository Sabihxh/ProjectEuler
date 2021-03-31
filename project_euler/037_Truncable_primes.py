from math import sqrt

def truncate_left(digit):

	a_digit = str(digit)
	result = []

	for x in range(1, len(a_digit) + 1, 1):
		result.append(a_digit[:x])

	return result

def truncate_right(digit):

	a_digit = str(digit)
	result = []

	for x in range(len(a_digit) -1, -1, -1):
		result.append(a_digit[x:])

	return result


def is_prime(digit):

	if digit == 1:
		return False
	loop_limit = int(sqrt(int(digit)))

	for x in range(2, loop_limit + 1):
		if digit % x == 0:
			return False
	return True


def find_truncable_primes(loop_limit):
	result = []
	for x in range(11, loop_limit):
		if is_prime(x):

			left_list = truncate_left(x)
			right_list = truncate_right(x)
			list_count = len(left_list) - 1
			
			left_len = len([1 for y in left_list[:-1] if is_prime(int(y))])
			right_len = len([1 for y in right_list[:-1] if is_prime(int(y))])

			if left_len == list_count and right_len == list_count:
				result.append(x)

	return result, sum([int(x) for x in result])

				












