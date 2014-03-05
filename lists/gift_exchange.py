
import random
import itertools

def valid(a, b):

    for i, j in itertools.izip(a, b):
        if i[0] == j[0]:
            return False
    return True

givers = [('tim', 'shirt'), ('jim', 'shoe'), ('john', 'ball'), ('joe', 'fruit')]

if len(givers) < 2:
    print "must have more than 1 givers"
else:    
    a = list(givers)
    b = list(givers)

    while not valid(a, b):
        random.shuffle(a)
        random.shuffle(b)

    for i, j in itertools.izip(a, b):
        print '%s gives %s to %s.' % (i[0], i[1], j[0])
