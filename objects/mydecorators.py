# -*- coding: utf-8 -*-

def classmixin(cls):
    def shout(self):
        return self.noise().upper()
    cls.shout = shout
    return cls

