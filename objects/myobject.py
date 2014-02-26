# -*- coding: utf-8 -*-

from mydecorators import classmixin

@classmixin
class Animal(object):
    '''
    >>> a = Animal()
    >>> a.noise()
    'snort'
    >>> a.has_owner
    False
    '''

    def __init__(self):
        self.location='mountains'
        self.has_owner=False

    def __getattribute__(self, name):
        if name == 'has_owner':
            rt = object.__getattribute__(self, name)
            if rt:
                return "Yessir"
            else:
                return "Nope"
        else:
            return object.__getattribute__(self, name)

    def noise(self):
        return "snort"

    def color(self):
        return "black"


class Dog(Animal):
    '''
    >>> a = Dog()
    >>> a.noise()
    'bark'
    >>> a.has_owner
    True
    '''

    def __init__(self):
        super(self.__class__, self).__init__()

        self.has_owner=True

    def __getattribute__(self, name):
        if name == 'has_owner':
            rt = object.__getattribute__(self, name)
            if rt:
                return "YUP"
            else:
                return "Nada"
        else:
            return object.__getattribute__(self, name)

    def noise(self):
        return "bark"       


if __name__ == '__main__':
    
    '''
    std = Animal()
    print std.noise()

    riley = Dog()
    print riley.noise()
    print riley.has_owner
    print riley.location
    '''

    import doctest
    import sys

    failure_count, test_count = doctest.testmod()
    sys.exit(failure_count)

    
