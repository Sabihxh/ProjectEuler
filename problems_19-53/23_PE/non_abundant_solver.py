from datetime import datetime

def sum_of_abundant_nums():
	a_set = set()
	start_time = datetime.now()
	with open('abundant_nums.txt', 'r') as x_file:
		a_list = map(int, x_file.read().splitlines())
	
	y = 0 
	for x in a_list:
		for y in a_list:
			a_set.add(x+y)
			if x + y > 28123:
				break
	non_sums = set()
	for x in range(1, 28124):
		if x not in a_set:
			non_sums.add(x)
	print sum(non_sums)

	print datetime.now() - start_time

sum_of_abundant_nums()