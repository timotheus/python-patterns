
def assertEquals(a, b, label):
    try:
        assert(a == b)
        print "%s == %s: %s ..Pass" % (a, b, label)
    except:
        print("%s == %s: %s ..Fail" % (a, b, label))
    
class Foo():
    pass