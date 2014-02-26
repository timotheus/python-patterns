# -*- coding: utf-8 -*-

class Wrapper(object):

    def __init__(self, obj):
        self.obj = obj
        self.foo = 'boo'

    def __getattr__(self, attr):
        wattr = getattr(self.obj, attr)
        return wattr

if __name__ == '__main__':
    from myobject import Animal
    
    riley = Animal()
    wrapper = Wrapper(riley)

    print(wrapper.noise)
    print(wrapper.has_owner)
    print(wrapper.foo)
    print(wrapper.boo)