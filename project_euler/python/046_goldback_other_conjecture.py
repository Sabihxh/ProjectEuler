from math import sqrt


def is_prime(a_num):

    if a_num < 2:
        return False
    if a_num == 2:
        return True
    if not a_num & 1:
        return False  # return false for even numbers

    limit = int(sqrt(a_num)) + 2
    for x in range(3, limit, 2):
        if a_num % x == 0:
            return False

    return True


def is_square(n):
    if sqrt(n) == int(sqrt(n)):
        return True
    return False


def solution(
    prime_limit, main_loop_limit
):  # increase these limits until the function prints out a number
    primes = [x for x in range(1, prime_limit, 2) if is_prime(x)]
    for x in range(9, main_loop_limit, 2):
        if not is_prime(x):
            primes_below_x = [p for p in primes if p < x]
            count = 0
            for p in primes_below_x:
                if is_square((x - p) / 2):
                    count += 1
                    break
            if count == 0:
                print(x)
                return x


solution(10000, 10000)
