from utils import generate_primes_under


def test_generate_primes_under():
    assert len(list(generate_primes_under(10000))) == 1229
