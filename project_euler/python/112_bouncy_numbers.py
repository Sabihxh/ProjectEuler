"""
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""

from itertools import count


def is_bouncy(n: int) -> bool:
    """
    - get the first number that isn't equal to the first.

    """
    n = str(n)

    # Check if all numbers are the same
    if len(set(n)) == 1:
        return False

    # Find if the number should be increasing or decreasing
    for i in range(len(n) - 1):
        if n[i] > n[i + 1]:
            increasing = True
            index = i + 1
            break
        elif n[i] < n[i + 1]:
            increasing = False
            index = i + 1
            break
        else:
            continue

    # Check if the number is bouncy
    bouncy = False
    if increasing:
        for i in range(index, len(n) - 1):
            if n[i] < n[i + 1]:
                bouncy = True
                break
    else:
        for i in range(index, len(n) - 1):
            if n[i] > n[i + 1]:
                bouncy = True
                break

    return bouncy


print(f"{False}:", is_bouncy(22))
print(f"{False}:", is_bouncy(66420))
print(f"{False}:", is_bouncy(134468))
print(f"{True}:", is_bouncy(155349))


def main(target: float):
    bouncy_count = 0
    bouncy_percentage = 0
    i = 2
    while bouncy_percentage < target:
        if is_bouncy(i):
            bouncy_count += 1
        bouncy_percentage = bouncy_count / i
        if bouncy_percentage >= target:
            break
        i += 1

    print(i)
    return i


def is_bouncy(n: int) -> bool:
    """from pe forums"""
    l = list(str(n))
    s = sorted(l)
    return s != l and s != l[::-1]


def solution2():
    """from pe forums"""
    j = 0
    i = 100

    while j / i < 99 / 100:
        i += 1
        x = str(i)
        if all(x[y] <= x[y + 1] for y in range(len(x) - 1)) or all(
            x[y] >= x[y + 1] for y in range(len(x) - 1)
        ):
            pass
        else:
            j += 1

    print(i)


if __name__ == "__main__":
    # main(0.99)
    solution2()
