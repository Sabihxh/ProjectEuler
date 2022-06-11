"""
Powerful digit sum
https://projecteuler.net/problem=56

A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the
maximum digital sum?
"""


def main():
	max_sum = 0
	for a in range(100):
		for b in range(100):
			digital_sum = sum(map(int, list(str(a**b))))
			if digital_sum > max_sum:
				max_sum = digital_sum
				print(f"max_sum: {max_sum}, a: {a}, b: {b}")


if __name__ == '__main__':
	main()
