# -*- coding: utf-8 -*-

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