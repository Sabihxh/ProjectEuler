"""
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""

def is_bouncy(n: int) -> bool:
	n = str(n)
	print(f'number: {n}')
	for i, x in enumerate(n[1:]):
		if x > n[0]:
			increasing = True
			break
		elif x < n[0]:
			increasing = False
			break
	else:
		print('not bouncy because all digits are the same')
		return False

	if increasing:
		'increasing'
		for x in n[i+1:]:
			if x < n[i]:
				print('Bouncy', x, n[i])
				return True

		print('no bouncy')
		return False

	else:  # decreasing
		print('decreasing')
		for x in n[i+1:]:
			if x > n[i]:
				print('Bouncy', x, n[i])
				return True

		print('no bouncy')
		return False


print(is_bouncy(22))
assert is_bouncy(22) == False
print(is_bouncy(66420))
assert is_bouncy(66420) == False
print(is_bouncy(134468))
assert is_bouncy(134468) == False
print(is_bouncy(155349))
assert is_bouncy(155349) == True



def main(target: float):
	bouncy_count = 0

	for i in range(2, 10**6):
		if is_bouncy(i):
			bouncy_count += 1
		bouncy_percentage = bouncy_count/i
		print(i, bouncy_percentage)
		if bouncy_percentage >= target:
			break

	print(i)
	return i


# if __name__ == "__main__":
# 	main(0.6)
