from math import gcd


problem = """
It turns out that 12 cm is the smallest length of wire that can be bent to form an 
integer sided right angle triangle in exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right 
angle triangle, and other lengths allow more than one solution to be found; for example,
using 120 cm it is possible to form exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one 
integer sided right angle triangle be formed?
"""


def main():
	"""Does not give the correct solution"""
	limit = 1.5 * (10**6)
	a_formulae = lambda m, n: 2 * m * n
	b_formulae = lambda m, n: (m ** 2) - (n ** 2)
	c_formulae = lambda m, n: (m ** 2) + (n ** 2)
	count = 0
	length_count = {}

	for n in range(1, 1224//1):
		for m in range(n, 1224//1):
			a = a_formulae(m, n)
			b = b_formulae(m, n)
			c = c_formulae(m, n)
			L = a + b + c

			# We only want triangles with length L <= limit
			if L > limit:
				break

			# Non-prime triangles
			if gcd(gcd(a, b), c) > 1:
				continue

			# We only want triangles that have exactly one integer sided right angle triangle
			if L not in length_count:
				length_count[L] = 1
			else:
				length_count[L] += 1

			values = (L, m, n, a, b, c)

			print(f"L={L}", f"(m, n)={m, n} ==>", f"triangle={a,b,c}")
			print('---')

	count = sum(v for v in length_count.values() if v == 1)
	print(f"Count: {count}")


if __name__ == '__main__':
	main()
