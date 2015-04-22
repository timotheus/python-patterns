from collections import deque
import copy

q = deque(range(1000))
q2 = copy.copy(q)

assert(q.pop() == 999)
q.append(999)

assert(q.popleft() == 0)
q.appendleft(0)

assert(q == q2)
