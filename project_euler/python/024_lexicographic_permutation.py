def n_factorial(n):
    total = 1
    for x in range(1, n + 1):
        total *= x
    return total


# print 274240 - factorial(8)*6

# n = 10 in for our case, since there are 10 digits
def lexico_sol(n):
    limit = 24
    final_num = ""
    x = 1
    while len(final_num) < n:
        final_num += "o"
        subtract_num = 0
        y = x
        multiple = 1
        product = n_factorial(n - 1)
        # limit in original question will be a million
        while product * multiple < limit - subtract_num:
            multiple += 1
        print multiple
        x += 1
    print final_num


lexico_sol(4)
