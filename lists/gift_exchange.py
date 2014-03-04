
import random
import itertools

givers = [('tim', 'shirt'), ('jim', 'shoe'), ('joe', 'fruit'), ('john', 'ball')]

def valid(a, b):
    if a == b:
        return False
    else:
        return True

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
