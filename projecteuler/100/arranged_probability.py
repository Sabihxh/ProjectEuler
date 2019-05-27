"""
Arranged probability

Problem 100

If a box contains twenty-one coloured discs, composed of fifteen blue discs and 
six red discs, and two discs were taken at random, it can be seen that the 
probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two 
blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total, 
determine the number of blue discs that the box would contain.

"""


from math import sqrt

def is_pronic(n):
    x = int(sqrt(n))
    return x * (x + 1) == n



def solution(total=5):
	start, end = int(total/2), 10**13
	for blue in range(start, end):
		total = blue * (blue - 1) * 2
		if is_pronic(total):
			print(blue, total)
			return blue

solution(total=35)
# solution(total=10**12)










