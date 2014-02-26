# -*- coding: utf-8 -*-

class Wrapper(object):

    def __init__(self, obj):
        self.obj = obj
        self.foo = 'boo'
        self.boo = 'who'

    def __getattr__(self, name):
        return getattr(self.obj, name)

    def bar(self):
        return "stool"

if __name__ == '__main__':
    from myobject import Animal
    
    riley = Animal()
    wrapper = Wrapper(riley)

    print(wrapper.noise)
    print(wrapper.has_owner)
    print(wrapper.foo)
    print(wrapper.boo)
    print(wrapper.bar())