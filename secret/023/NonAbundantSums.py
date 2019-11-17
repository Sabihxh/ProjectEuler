import helper_proper_divisors as hpd
from datetime import datetime
#find all abundant numbers
print hpd.proper_divisors(28)

start_time = datetime.now()

def abundant_numbers(i = 28124):
	with open('abundant_nums.txt', 'w') as a_file:
		for x in range(1, i):
			if sum(hpd.proper_divisors(x)) > x:
				a_file.write('{}\n'.format(x))


print datetime.now() - start_time

