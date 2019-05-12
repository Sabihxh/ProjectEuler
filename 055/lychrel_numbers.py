"""
Psuedo Code A:

- Make is_palindrome function which return True if number is palindrome, otherwise False.
- Make add_reverse function which adds the number and its reverse
- Loop through numbers from 1 - 10,000
- For each number, loop through 50 times
- For every iteration of this 50 loop, check if its reverse is a palindrome
- If its palindrome, break the loop
- If the loop runs upto 50 times then mark this number as a lychrel number

Complexity of Psuedo Code A:
O(n)?

"""
def is_palindrome(_num):
    return _num == int(str(_num)[::-1])

def add_reverse(_num):
    return _num + int(str(_num)[::-1])

#Add luchrel number += 1 if else is hit
def count_lychrel_numbers(_limit = 10001):
    lychrel_nums = 0
    for n in range(_limit):
        counter = 1
        test_n = n
        while counter <= 50:
            _sum = add_reverse(test_n)
            if is_palindrome(_sum):
                break
            else:
                test_n = _sum
            counter += 1
        else:
            lychrel_nums += 1
            
    return 'Number of Lychrel Numbers: %s' % lychrel_nums

print(count_lychrel_numbers())
    
