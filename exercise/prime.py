# -*- coding: utf-8 -*-

'''
Below are some I have used in the last couple of weeks. But I scout for new ones every other week.
1) Implement Unix Tail command
2) Generate Prime numbers between the start and end number
3) Given an Number , print the next highest integer such that digits are in increasing order
4) Given multiple large files(each of which is > TB) containing ebay_user_id’s print only the unique id’s.
5) Function to test whether two strings are anagrams


6) Given an array of integers, find the missing element in it. 
(there is only one missing element in the array).

7) Given an array of integers, find the sub array with maximum sum.

8) Find out if a binary tree (does not matter if its BST or not) is balanced 
or not. i.e. delta of left and right subtree should not be greater than 1.

Some OOP/c++ questions:
9) If you have an empty class like class Foo{} and you create an object of 
that class, what would sizeof(object) be ?

10) What is the difference between merge and quick sort? Complexities (best and worst case)? Explain worst case of quick sort? When would you use one over other?
11) What is auto_ptr (STL)? (I had c++ written on my resume, so that's the reason I was asked this question)? Can you create a vector of auto_ptrs? What kind of issues would you encounter while managing the vector of auto_ptrs? 

12) Linked list
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
