def tri_pent_hex():
    p_nums = set()
    h_nums = set()

    min_tri, max_tri = 286, 100000
    min_pent, max_pent = 165, 35000
    min_hex, max_hex = 143, 30000

    for n in range(min_pent, max_pent):
        pentagonal = int(n * (3 * n - 1) / 2)
        p_nums.add(pentagonal)

    for n in range(min_hex, max_pent):
        pentagonal = int(n * (2 * n - 1))
        h_nums.add(pentagonal)

    for n in range(min_tri, max_tri):
        triangle = int((n * (n + 1)) / 2)
        if triangle in p_nums and triangle in h_nums:
            print(triangle, n)
            return triangle


tri_pent_hex()
