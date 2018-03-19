def is_permutation(num1, num2, num3, num4, num5):
	if sorted(str(num1)) == sorted(str(num2)) == sorted(str(num3)) == sorted(str(num4)) == sorted(str(num5)):
		return True
	return False


def _solution():
	for x in range(200, 400):
		for y in range(x-51, x + 51 ):
			for z in range(x-51, x + 51):
				for a in range(x-51, x + 51):
					for b in range(x-51, x + 51):
						if x == y or x == z or x == a or x == b or y == z or y == a or y == b or z == a or z == b or a == b: continue
						x_3 = x ** 3
						y_3 = y ** 3
						z_3 = z ** 3
						a_3 = z ** 3
						b_3 = z ** 3
						
						if is_permutation(x_3, y_3, z_3, a_3, b_3):
							print(x, y, z, a, b, x_3, y_3, z_3, a_3, b_3)
					
	
_solution()





