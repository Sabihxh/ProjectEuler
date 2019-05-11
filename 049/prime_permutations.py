from itertools import permutations


def is_prime(a_num):

	if a_num < 2:
		return False

	if a_num == 2:
		return True

	#return false for even numbers
	if not a_num & 1:
		return False

	limit = int(a_num**0.5) + 2
	for x in range(3, limit, 2):
		if a_num % x == 0:
			return False

	return True


def solution():
	for x_1 in range(1001, 9998):
		x_2 = x_1 + 3330
		x_3 = x_1 + 6660

		a_list = list(permutations(str(x_1)))
		if tuple(str(x_2)) in a_list and tuple(str(x_3)) in a_list:
			if is_prime(x_1) and is_prime(x_2) and is_prime(x_3):
				print('%s%s%s' % (x_1, x_2, x_3))


			


solution()
