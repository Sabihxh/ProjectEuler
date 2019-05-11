def solution_1():
	primes_list = [2,3,5,7,11,13,17]

	sum_special_numbers = 0

	for one in range(1, 10):
		for two in range(0, 10):
			if two == one:
				continue
			for three in range(0, 10):
				if three == one or three == two:
					continue
				for four in range(0, 10):
					if four == one or four == two or four == three:
						continue
					for five in range(0, 10):
						if five == one or five == two or five == three or five == four:
							continue
						for six in range(0, 10):
							if six == one or six == two or six == three or six == four or six == five:
								continue
							for seven in range(0, 10):
								if seven == one or seven == two or seven == three or seven == four or seven == five or seven == six:
									continue
								for eight in range(0, 10):
									if eight == one or eight == two or eight == three or eight == four or eight == five or eight == six or eight == seven:
										continue
									for nine in range(0, 10):
										if nine == one or nine == two or nine == three or nine == four or nine == five or nine == six or nine == seven or nine == eight:
											continue
										for ten in range(0, 10):
											if ten == one or ten == two or ten == three or ten == four or ten == five or ten == six or ten == seven or ten == eight or ten == nine:
												continue
											pandigital_number = str(one) + str(two) + str(three) + str(four) + str(five) + str(six) + str(seven) + str(eight) + str(nine) + str(ten)

											if int(pandigital_number[1:4]) % 2 == 0 and int(pandigital_number[2:5]) % 3 == 0 and int(pandigital_number[3:6]) % 5 == 0 and int(pandigital_number[4:7]) % 7 == 0 and int(pandigital_number[5:8]) % 11 == 0 and int(pandigital_number[6:9]) % 13 == 0 and int(pandigital_number[7:10]) % 17 == 0:
												print(pandigital_number)
												sum_special_numbers += int(pandigital_number)


from itertools import permutations

def solution_2():
	sum_special_numbers = 0
	for perm in permutations("0123456789"):
		pandigital_number = ''.join(perm)
		for index, prime in zip(range(1, 10), [2,3,5,7,11,13,17]): #loops through two lists simultanously
			if int(pandigital_number[index: index + 3]) % prime != 0: 
				break
		else:
			sum_special_numbers += int(pandigital_number)
	print(sum_special_numbers)

solution_2()




