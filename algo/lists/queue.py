
class Stack(object):

    def __init__(self, a=None):
        self._stack = a or []

    def push(self, e):
        self._stack.append(e)

    def pop(self):
        return self._stack.pop()

    def isEmpty(self):
        if len(self._stack) == 0:
            return True
        else:
            return False


class Queue(object):

    def __init__(self):
        self._stack = Stack()
        self._stack2 = Stack()

    def enqueue(self, e):
        return self._stack.push(e)

    def denqueue(self):

        while not self._stack.isEmpty():
            self._stack2.push(self._stack.pop())

        first = self._stack2.pop()

        while not self._stack2.isEmpty():
            self._stack.push(self._stack2.pop())

        return first

if __name__ == '__main__':

    q = Queue()

    q.enqueue('a')
    q.enqueue('b')
    q.enqueue('c')

    assert('a' == q.denqueue())
    assert('b' == q.denqueue())
    assert('c' == q.denqueue())

    from collections import deque

    cq = deque()
    cq.append('a')
    cq.append('b')
    cq.append('c')

    assert('a' == cq.popleft())
    assert('b' == cq.popleft())
    assert('c' == cq.popleft())


