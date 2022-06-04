"""
16807 = 7^5
134217728 = 8^9
How many n-digit numbers exist which are also n-th power

Solution:
- itterate through numbers from 1 - 99 (num_limit)?
- itterate through powers from 1- 20 (power_limit)?
- if the power = no. of digits in result. 
- count += 1
"""


def solution(n_limit, p_limit):
    count = 0
    for n in range(1, n_limit):
        for p in range(1, p_limit):
            n_power_p = n**p
            if len(str(n_power_p)) == p:
                count += 1
                print(n, p, n_power_p)
    print(count)


solution(99, 99)
