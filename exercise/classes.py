import sys

'''
If you have an empty class like class Foo{} and you create an object of 
that class, what would sizeof(object) be?
'''

def assertEqual(a, b, label):
    try:
        assert(a == b)
        print "%s == %s: %s" % (a, b, label)
    except:
        print("%s != %s: %s" % (a, b, label))
    
class Foo():
    pass

assertEqual(sys.getsizeof(Foo()), 72, "class size")

x = 2
assertEqual(sys.getsizeof(x), 24, "int size")
