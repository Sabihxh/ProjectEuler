from sympy import primefactors


def prime_summations(no_of_partitions):
    """
    Gives n such that the number of prime partitions
    of n is >= no_of_partitions

    n has a limit of 1000.
    i.e. no_of_partitions <= 10 quadrillion
    """
    l = [1, 0]
    for n in range(2, 1000):
        prime_partitions = (
            sum([sum(primefactors(k)) * l[n - k] for k in range(1, n + 1)]) / n
        )
        l.append(prime_partitions)
        if prime_partitions > no_of_partitions:
            return n, prime_partitions


print(prime_summations(5000))
