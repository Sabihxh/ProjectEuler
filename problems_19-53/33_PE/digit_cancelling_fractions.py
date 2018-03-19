"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting 
to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by 
cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in
value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value 
of the denominator.
"""

from functools import reduce
from fractions import Fraction


#Return the greatest common divisor of a and b
def gcd(a, b):

    small = min(a, b)
    large = max(a, b)

    if small == 0:
        return large

    elif small == 1:
        return 1

    else:
        return gcd(small, large % small)


#Returns a fraction in its simplified form, 
#Inputs: a is numerator and b is denominator
def simplify_fraction(a, b):

    simplified_num = a/gcd(a, b)
    simplified_den = b/gcd(a, b)

    return simplified_num, simplified_den


def main_loop(loop_limit):

    #a_list gives all non-trivial fractions of type described in the problem. 
    list_of_fractions = []

    #x is numerator
    for x in range(11, loop_limit - 1):

        #y is denominator and since x/y < 1, we start y from x + 1
        for y in range(x + 1, loop_limit):
            common_digit = [q for q in set(str(x)) if q in set(str(y)) and q != '0']

            #We can have two digits in common, when x is reverse of y e.g. x = 45 and y = 54, we ignore these
            if len(common_digit) == 1:
                num_simplified_wrong = str(x).replace(common_digit[0], '', 1)
                den_simplified_wrong = str(y).replace(common_digit[0], '', 1)

                wrongly_simplified = simplify_fraction(int(num_simplified_wrong), int(den_simplified_wrong))
                simplified_xy_fraction = Fraction(x, y)

                #Matching numerator and denominator of two fractions
                if simplified_xy_fraction.numerator == wrongly_simplified[0] and simplified_xy_fraction.denominator == wrongly_simplified[1]:
                    list_of_fractions.append(simplified_xy_fraction)

    product_of_fractions = reduce((lambda x, y: x * y), [item for item in list_of_fractions])
    
    return 'Solution: %s' % product_of_fractions.denominator

print main_loop(100)

