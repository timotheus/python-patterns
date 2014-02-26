# -*- coding: utf-8 -*-

# off by 3 (unique and ordered)
a = [1, 2, 3, 4, 5, 6]
b = [4, 5, 6, 1, 2, 3]

print(sum(a) == sum(b))

for i in xrange(len(a)):
	if a[i] == b[0]:
		print "off by %s" % i

# matching
a = [1, 2, 3, 3, 4, 5, 6]
b = [1, 2, 3, 3, 4, 5, 6]

print((a[0] == b[0] and b[-1] == b[-1]))
print(len(a) == len(b))

# off by 3 (ordered with dup ints)
from copy import copy

def shift(num, a):
	newlist = a[-num:]
	newlist.extend(a[:-num])
	return newlist

a = [1, 2, 3, 3, 4, 5, 6]
b = [4, 5, 6, 1, 2, 3, 3]

print(sum(a) == sum(b))

go_forward = False

# less distance between a[0] and b[0]
if (abs(a[0] - b[0]) > abs(a[0] - b[-1])):
	go_forward = True

for i in range(len(a)):
	new_a = None
	if go_forward:
		new_a = shift(i, copy(a))
	else:
		new_a = shift(-i, copy(a))

	if new_a == b:
		print "off by %s" % i
		break

