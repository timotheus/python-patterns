
import inspect

def assertEquals(a, b, label=''):
    if not label:
        filename = inspect.stack()[1][1].split('/')[-1]
        label = "Test from %s on line %s" % (filename, inspect.stack()[1][2])
    try:
        assert(a == b)
        print("%s == %s: %s ..Pass" % (a, b, label))
    except:
        print("%s == %s: %s ..Fail" % (a, b, label))
    
class Foo():
    pass