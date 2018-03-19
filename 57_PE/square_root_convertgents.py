#-*- coding: utf-8 -*-
"""
Solution uses recurence relation for infinite continued fractions i.e.

sqrt(2) = [1, 2, 2, 2, ...]

p_n = a*p_(n-1) + p_(n-2)
q_n = a*q_(n-1) + q_(n-2)

where p_n/q_n is the continued fration expansion of sqrt(2) and a = 2

Page 366 of:
http://people.math.binghamton.edu/dikran/478/Ch7.pdf
"""

def convergents():

	p_0, p_1 = 3, 7
	q_0, q_1 = 2, 5
	counter = 0

	for x in range(1000):
		p_n = 2*p_1 + p_0
		q_n = 2*q_1 + q_0
		
		p_0, q_0 = p_1, q_1
		p_1, q_1 = p_n, q_n

		if not len(str(p_n)) > len(str(q_n)): continue
		
		counter += 1
	print("No. of convergents of sqrt(2) below 1000 where no. of digits in numerator > denominator: \n", counter)

convergents()
