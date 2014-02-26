# -*- coding: utf-8 -*-

import myobject

oAnimal = myobject.Animal

class PatchAnimal(myobject.Animal):
	
	def noise(self):
		mystr = oAnimal.noise(self)
		return "patched (%s)" % mystr

myobject.Animal = PatchAnimal
