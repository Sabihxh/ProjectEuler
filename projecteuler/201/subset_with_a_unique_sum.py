from collections import Counter
from itertools import combinations

import numpy as np


def solution(S, k):
	"""
	Takes a Set (S) and number of subsets (k)
	and returns sum( U(S, no_of_subsets)) where the function
	U is described here:
		https://projecteuler.net/problem=201
	"""
	a = np.array(tuple(sum(c) for c in combinations(S, k)))

	cnt = Counter()
	for x in a:
		cnt[x] += 1

	result = [x for x in cnt if cnt[x] == 1]
	print(sum(result))


# # 0.3 sec
# solution((1,3,6,8,10,11), 3)

# # 0.2 sec
# S = (x**2 for x in range(10))
# k = 5
# solution(S, k)


# # 0.5 sec
# S = (x**2 for x in range(20))
# k = 10
# solution(S, k)

# # 12.2 sec
# S = (x**2 for x in range(30))
# k = 8
# solution(S, k)




















