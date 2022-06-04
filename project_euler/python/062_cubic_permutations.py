def cubic_permutations(no_of_permutations):
    result = 0
    mapping = {}

    for x in range(3000000, 1, -1):
        cube = "".join(sorted(str(x**3)))

        if cube not in mapping:
            mapping[cube] = 1
        else:
            mapping[cube] += 1

        if mapping[cube] == no_of_permutations:
            result = x
            break

    return result**3


if __name__ == "__main__":
    solution = cubic_permutations(no_of_permutations=25)
    print(solution)
