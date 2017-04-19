import sys
from common import assertEquals

'''
If you have an empty class like class Foo{} and you create an object of 
that class, what would sizeof(object) be?
'''
    
class Foo():
    pass

assertEquals(sys.getsizeof(Foo()), 72, "class size")

x = 2
assertEquals(sys.getsizeof(x), 24, "int size")
