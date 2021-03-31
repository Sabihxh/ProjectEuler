from datetime import datetime

start_time = datetime.now()
#This function takes a number as arguement
#and returns its proper divisors
def sum_proper_divisors(num):
	total = 0
	
	if num % 2 == 0: 
		a_set = {1}
		for x in range(2, int(num/2)):
			if num % x == 0:
				a_set.add(num/x)
				a_set.add(x)
				total += x

	else:
		a_set = set()
		for x in range(1, int(num/2), 2):
			if num % x == 0:
				a_set.add(num/x)
				a_set.add(x)
				total += x
	return a_set

print sorted(sum_proper_divisors(123456788))

#This function finds all abundant numbers into 1 file and 
#all numbers which are not adundant into a different file
def abundant_numbers(i = 28124):
	abundant_set = set()
	non_abundant_set = set()
	for x in range(1, i):
		if sum_proper_divisors(x) > x:
			abundant_set.add(x)
		# else:
		# 	non_abundant_set.add(x)
	return abundant_set

# abundant_numbers()

def sum_of_abundant_nums():
	a_set = set()
	a_list = abundant_numbers()
	
	y = 0 
	for x in a_list:
		for y in a_list:
			if x + y > 28123:
				break
			else:
				a_set.add(x+y)

	non_sums = set()
	for x in range(1, 28124):
		if x not in a_set:
			non_sums.add(x)

	print sum(non_sums)
	return sum(non_sums)

# sum_of_abundant_nums()

print datetime.now() - start_time


