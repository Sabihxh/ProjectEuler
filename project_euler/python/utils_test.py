from utils import generate_primes_under, is_permutation


def test_generate_primes_under():
    assert len(list(generate_primes_under(10000))) == 1229


def test_is_permutation():
    assert is_permutation(1234, 4321) is True
    assert is_permutation(1234, 4322) is False
