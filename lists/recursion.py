# -*- coding: utf-8 -*-


def outer(max):

    a = 1
    b = 1
    count = 1

    def inner(num):
        print(a)
        print(b)
        print(num)
        
        def inner2(num2, num3):
            print(num2)
            print(max)

        return inner2

    return inner

def build_sets(s):
    if len(s) == 1:
        return [s]

    mylist = []
    for i in s:
        subStr = s.replace(i, '', 1)
        z = build_sets(subStr)

        for b in z:
            mylist.append(i+b)

    return mylist


if __name__ == '__main__':

    s = 'abc'
    a = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    assert(a == build_sets(s))

    outer(99)(22)(10, 11)

