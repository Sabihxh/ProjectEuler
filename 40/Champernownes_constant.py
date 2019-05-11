
def champernowne_constant():
	
	d_n = [1, 10, 100, 1000, 10000, 100000, 1000000]
	
	string = ''
	
	for x in range(200000):
		string += str(x)
	
	product = 1

	for y in d_n:
		print string[y]
		product *= int(string[y])

	print product

champernowne_constant()
