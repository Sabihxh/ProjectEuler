#-*- coding: utf-8 -*-
from fractions import Fraction as fr

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True  


for x in range(100):
    if is_prime(x):
        print(x)

# def all_divisors(num):
#     """Gives all divisors including num itself"""
#     divisors = set()
#     for x in range(2, int(num**0.5) + 1):
#         if num % x == 0:
#             y = int(num/x)
#             divisors.add(x)
#             divisors.add(y)
#     return {x for x in divisors if is_prime(x)}

# # print all_divisors(10)

# def solution(limit = 1000000):
#     highest_n_phi = 0
#     max_n = 0
#     for n in range(limit, 1, -1):
#         phi = n
#         pds = all_divisors(n)
#         if not pds: continue
#         for pd in pds:
#             phi *= fr(pd-1, pd)
#         n_phi = float(n)/phi
#         if n_phi > highest_n_phi:
#             highest_n_phi = n_phi
#             max_n = n
#             print(max_n, phi, highest_n_phi)
#     print(max_n, phi, highest_n_phi)
#     return max_n, highest_n_phi

# solution()

"""
The most effiecient answer does not even require programming:
Refer to Q69 pdf

2*3*5*7*11*13*17 = 510510


"""










        
