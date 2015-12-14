import math
import time
import sys
from .common import assertEquals


'''
WAP to find if a string exists in a matrix of characters. You can only go left to right and top to bottom 
to see if a given string exists in this matrix of characters.

"ARK"

G A U E

O I W R

K R P D

K J L R
'''


def wordmatch(word):
    word_array = list(word)
    word_array.reverse()

    matrix = [
        ['G', 'A', 'U', 'E'],
        ['I', 'R', 'W', 'F'],
        ['K', 'L', 'P', 'D'],
        ['K', 'J', 'N', 'R'],
    ]

    for sublist in matrix:
        for i in sublist:
            if word_array[-1] == i:
                word_array.pop()

                if len(word_array) == 0:
                    return True

    return False

assertEquals(wordmatch('ARK'), True, 'matched word')
assertEquals(wordmatch('RIRL'), False, 'did not matched word')

'''
Anagram
'''

def agram(word, word2):

    a = list(word)
    a.sort()

    b = list(word2)
    b.sort()

    return a == b

assertEquals(agram('tim', 'mit'), True, 'agram1')
assertEquals(agram('heart', 'earth'), True, 'agram2')
assertEquals(agram('heart', 'eartt'), True, 'agram3')

'''
Anagram list
'''

def agram_list(A, B=''):
    assert len(A) >= 0
    assert len(A) == len(set(A))
    if len(A) == 0:
        return [B]
    else:
        res = []        
        for i in range(len(A)):
            res.extend(agram_list(A[0:i] + A[i+1:], B + A[i]))

        return res

print agram_list('tim')

'''
Factorial
'''
def factorial(num):
    total = 1
    for i in range(1, num+1):
        total *= i

    return total

assertEquals(factorial(10), math.factorial(10), 'factorial 10')
assertEquals(factorial(20), math.factorial(20), 'factorial 20')
assertEquals(factorial(99), math.factorial(99), 'factorial 99')


'''
Fib
'''

fibval = 1
last = 0
last2 = 0

print(fibval)
for count in range(0, 9):
    last2 = last
    last = fibval
    fibval = last2 + last
    print(fibval)

# Fib generator
def fib_seq():
    a = 1
    b = 1
    yield a
    yield a
    for i in xrange(0, sys.maxint):
        total = a + b
        a = b
        b = total
        yield total

# 1, 1, 2, 3, 5, 8, 13
for i in fib_seq():
    if i > 40000:
        break
    print i,

'''
Generate Prime numbers between the start and end number
'''
def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if (num % i) == 0:
            return False

    return True

primes = []
for i in range(1, 100):
    if is_prime(i):
        primes.append(i)

print(primes)

'''
Given an array of integers, find the missing element in it. 
(there is only one missing element in the array).
''' 
a = [0, 1, 3, 4, 5, 6]

def find_missing(a):
    
    for i in range(a[0], a[-1]):
        if a[i] != i:
            return i

print(find_missing(a))


'''
Given an array of integers, find the sub array with maximum sum.
'''

max_sum = []
total = 0
for a in primes:
    total += a
    max_sum.append(total)

print(primes)
print(max_sum)
