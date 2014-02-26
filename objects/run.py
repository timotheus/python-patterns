# -*- coding: utf-8 -*-

# patches must import prior to original class
#import mypatches

from myobject import Animal, Dog

std = Animal()
print std.noise()
print std.has_owner

riley = Dog()
print riley.noise()
print riley.shout()
print riley.has_owner
print riley.location
