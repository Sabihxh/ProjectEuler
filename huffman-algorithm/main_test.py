from main import get_symbol_probabilities, create_encoder, encode, main, Fraction


def test_get_symbol_probabilities():
    value = "abbccc"
    excepted_value = {"a": Fraction(1,6), "b": Fraction(2, 6), "c": Fraction(3, 6)}
    assert get_symbol_probabilities(value) == excepted_value


def test_create_encoder():
    symbol_frequencies = {'b': Fraction(1, 3), 'c': Fraction(1, 2), 'a': Fraction(1, 6)}
    expected_tree = {'a': '10', 'b': '11', 'c': '0'}
    assert create_encoder(symbol_frequencies) == expected_tree


def test_encode():
    value = "abbccc"
    expected_value = "101111000"
    encoder = {'a': '10', 'b': '11', 'c': '0'}
    encoded_value = encode(value, encoder)
    assert encoded_value == expected_value


def test_main():
    value = "abbccc"
    expected_value = "101111000"
    assert main(value) == expected_value