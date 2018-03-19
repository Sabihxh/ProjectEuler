#-*- coding: utf-8 -*-
"""
Main goal: Find fractions
1 + 1/(2+ 1/(2+...))
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
