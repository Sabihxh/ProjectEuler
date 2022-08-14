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
	limit = 1.5 * (10**6)
	a_formulae = lambda m, n: 2 * m * n
	b_formulae = lambda m, n: (m ** 2) - (n ** 2)
	c_formulae = lambda m, n: (m ** 2) + (n ** 2)
	
	for n in range(1, 10000):
		for m in range(n+1, 10000):
			a = a_formulae(m, n)
			b = b_formulae(m, n)
			c = c_formulae(m, n)

			print(m, n, "triangle", a, b, c, (a**2)+(b**2) == (c**2), f"L={a+b+c}")
			print('---')



if __name__ == '__main__':
	main()
