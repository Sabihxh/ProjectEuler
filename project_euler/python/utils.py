from html.parser import HTMLParser
from math import gcd
from time import time


def timeit(func):
    """
    This function shows the execution time of the function object passed
    """

    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"Function {func.__name__!r} executed in {(t2-t1):.4f}s")
        return result

    return wrap_func


def generate_primes_under(n: int):
    """
    Returns list of all prime numbers <= n
    """
    for possiblePrime in range(
        2, n + 1
    ):  # Assume number is prime until shown it is not.
        isPrime = True
        for num in range(2, int(possiblePrime**0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            yield possiblePrime


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def is_permutation(x: int, y: int) -> bool:
    return sorted(str(x)) == sorted(str(y))


def distinct_prime_factors(n):
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True


def is_prime_2(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))


def no_of_coprimes(n):
    """Finds the number of coprimes of n"""
    counter = 0
    if n == 1:
        return 1
    for x in range(1, n):
        if gcd(x, n) == 1:
            counter += 1

    return counter


def display_html(html):

    class MyHTMLParser(HTMLParser):
        def handle_data(self, data):
            print(data)

    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()
