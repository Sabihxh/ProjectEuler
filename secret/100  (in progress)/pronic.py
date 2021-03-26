"""
A pronic number is such a number which can be represented as a product 
of two consecutive positive integers. By multiplying these two consecutive
positive integers, there can be formed a rectangle which is represented 
by the product or pronic number. So it is also known as Rectangular Number.

The first few Pronic numbers are:
0, 2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156, 182, 210, 240, 272, 306, 342, 380, 420, 462 . . . . . .

Pronic number is a number which is the product of two consecutive integers, 
that is, a number n is a product of x and (x+1). The task is to check if a
given number is pronic or not.

"""


import math
def is_pronic(n):
    x = int(math.sqrt(n))
    return x * (x + 1) == n


print(is_pronic(210))




