import pytest

problem = """
Write a function that takes a list of poker hands and returns the winner.
e.g. 
    input = 5H 5C 6S 7S KD 2C 3S 8S 8D TD
    assumtion: first 5 cards are player 1, last 5 cards are player 2
    output = player 2
"""

def is_high_card(hand) -> bool:
    return False

def is_one_pair(hand) -> bool:
    return False

def is_two_pairs(hand) -> bool:
    return False

def is_three_of_a_kind(hand) -> bool:
    return False

def is_straight(hand) -> bool:
    return False

def is_flush(hand) -> bool:
    return False

def is_full_house(hand) -> bool:
    return False

def is_four_of_a_kind(hand) -> bool:
    return False

def is_straight_flush(hand) -> bool:
    return False

def is_royal_flush(hand) -> bool:
    return False

def sort_hand(hand) -> str:
    return ""

def poker_hand(hand: str) -> str:
    """
    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    """
    hand_array: list = hand.split(" ")
    hand_player_1 = hand_array[:5]
    hand_player_2 = hand_array[5:]

    print(hand_player_1)
    print(hand_player_2)


# run tests using `python -m pytest 054_poker_hands.py`
@pytest.mark.parametrize("hand, winner", [
    ("5H 5C 6S 7S KD 2C 3S 8S 8D TD", "player 2"),
    ("5D 8C 9S JS AC 2C 5C 7D 8S QH", "player 1"),
    ("2D 9C AS AH AC 3D 6D 7D TD QD", "player 2"),
    ("4D 6S 9H QH QC 3D 6D 7H QD QS", "player 1"),
    ("2H 2D 4C 4D 4S 3C 3D 3S 9S 9D", "player 1"),
])
def test_poker_hand(hand, winner):
    assert poker_hand(hand) == winner
    assert poker_hand(hand) == winner
    assert poker_hand(hand) == winner
    assert poker_hand(hand) == winner
    assert poker_hand(hand) == winner


if __name__ == '__main__':
    hand = "5H 5C 6S 7S KD 2C 3S 8S 8D TD"
    poker_hand(hand)
