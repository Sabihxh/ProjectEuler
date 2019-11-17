def pandigital_check(a_num):
	a_num = str(a_num)
	check = [1,2,3,4,5,6,7,8,9]
	sorted_list = list(map(int, sorted(list(a_num))))

	if check == sorted_list:
		return True

	return False

def main_loop():
	pandigitals_list = []
	for x in range(2, 9999):
		test_string = ''
		for y in range(1, 7):
			product = x * y
			test_string += str(product)
			if len(test_string) == 9:
				if pandigital_check(test_string):
					pandigitals_list.append(test_string)
				break
	print (pandigitals_list)

main_loop()