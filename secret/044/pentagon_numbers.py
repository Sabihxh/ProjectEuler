from itertools import permutations
from itertools import product


def solution():
	p_nums_set = set()
	both = []
	more_p_nums_list = []
	for n in range(1, 3000, 1): 
		pentagonal_number = int(n*(3*n - 1)/2)
		p_nums_set.add(pentagonal_number)

	for nums in set(permutations(p_nums_set, 2)):
		_sum = nums[0] + nums[1]
		_diff = nums[0] - nums[1]

		if _sum in p_nums_set and _diff in p_nums_set:
			print(nums, _diff)

solution()




