# -*- coding: utf-8 -*-

# patches must import prior to original class
#import mypatches

from myobject import Animal, Dog

std = Animal()
print std.noise()

riley = Dog()
print riley.noise()
print riley.has_owner
print riley.location
