"""
Backward and forward
====================

The sign outside reads: Name no one man.

"Escape. We must escape." Staring at the locked door of his cage, 
Beta Rabbit, spy and brilliant mathematician, has a revelation. 
"Of course! Name no one man - it's a palindrome! Palindromes are 
the key to opening this lock!" 

To help Beta Rabbit crack the lock, write a function answer(n) 
which returns the smallest positive integer base b, at least 2, 
in which the integer n is a palindrome. The input n will satisfy 
"0 <= n <= 1000."


Test cases
==========

Inputs:
    (int) n = 0
Output:
    (int) 2

Inputs:
    (int) n = 42
Output:
    (int) 4

"""


def recurseBase(array, num, base):
    value = num % base
    if value >= 10:
        value = chr(value + 87)

    array.append(value)
    div = num / base
    if(div == 0):
        return
    recurseBase(array, div, base)


def base10toX(num, base):
    array = []
    recurseBase(array, num, base)
    return array[::-1]


def answer(num):

    for base in range(2, 30):
        base_array = base10toX(num, base)
        if base_array == base_array[::-1]:
            return base

    return None

if __name__ == "__main__":

    for i in range(1001):
        base = answer(i)
        if base:
            print "Base %d for number %d is the first palindrome" % (base, i)
