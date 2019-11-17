from math import factorial
import numpy as np
from matplotlib import pyplot as plt

#Function by https://stackoverflow.com/questions/4941753/is-there-a-math-ncr-function-in-python
import operator as op
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom

# print ncr(24, 15)

#Interesting observation, a wave is made when you print ncr
def solution(limit=100):
	c = 0
	for n in range(23, limit + 1):
		for r in range(2, n):
			if ncr(n, r) > 1000000:
				c += 1
				# print ncr(n, r)
	print 'Number of values of nCr greater than 1000000: %s' % c

solution()

def list_of_ncr(limit=100):
	ncr_list = []
	for n in range(23, limit + 1):
		for r in range(2, n):
			if ncr(n, r) > 1000000:
				ncr_list.append(ncr(n, r))

	return ncr_list

plt.plot(list_of_ncr()[:100])
plt.ylabel("Pascal numbers > million")
plt.show()


