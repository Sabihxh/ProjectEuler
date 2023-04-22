from fractions import Fraction


def get_symbol_probabilities(value: str) -> dict:
    return {x: Fraction(value.count(x), len(value)) for x in set(value)}


def create_encoder(symbol_probabilities: dict) -> dict:
    result = {x: "" for x in sorted(symbol_probabilities)}
    for _ in range(len(result)-1):
        symbol_0 = min(symbol_probabilities, key=symbol_probabilities.get)
        symbol_0_value = symbol_probabilities[symbol_0]
        symbol_probabilities.pop(symbol_0)
    
        symbol_1 = min(symbol_probabilities, key=symbol_probabilities.get)
        symbol_1_value = symbol_probabilities[symbol_1]
        symbol_probabilities.pop(symbol_1)
    
        combined_symbol = symbol_0 + symbol_1
        combined_symbol_probability = symbol_0_value + symbol_1_value
        symbol_probabilities[combined_symbol] = combined_symbol_probability
        for x in symbol_0:
            result[x] = "0" + result[x]

        for x in symbol_1:
            result[x] = "1" + result[x]

    return result


def encode(value: str, encoder: dict) -> str:
    encoded_value = ""
    for symbol in value:
        encoded_value += encoder[symbol]
    return encoded_value


def main(value: str) -> str:
    symbol_probabilities =  get_symbol_probabilities(value)
    encoder = create_encoder(symbol_probabilities)
    for k, v in encoder.items():
        print(f"{k}: {v}")
    return encode(value, encoder)


if __name__ == "__main__":
    value = "Adam is great at nothing except eating and sleeping and being cute."
    encoded_value = main(value)
    print(f"value: {value}", f"encoded_value: {encoded_value}", sep="\n")
