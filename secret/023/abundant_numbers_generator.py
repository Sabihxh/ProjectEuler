import helper_proper_divisors as hpd
from datetime import datetime

start_time = datetime.now()
#finds all abundant numbers upto 28123
def abundant_numbers(i = 28124):
	non_file = open('non_abundant_nums.txt', 'w')
	with open('abundant_nums.txt', 'w') as a_file:
		for x in range(1, i):
			if sum(hpd.proper_divisors(x)) > x:
				a_file.write('{}\n'.format(x))
			else:
				non_file.write('{}\n'.format(x))
	non_file.close()

abundant_numbers()

print datetime.now() - start_time