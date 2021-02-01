#This function takes a number as arguement
#and returns its proper divisors

def proper_divisors(num):
	proper_divisor_list = []
	for x in range(1, num):
		if num % x == 0:
			proper_divisor_list.append(x)
	return proper_divisor_list

# print sum(proper_divisors(28122))