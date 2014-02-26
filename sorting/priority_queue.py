from heapq import heapify, heappop, heapreplace
from copy import copy

def merge_pqueue(lists, max_size=10):
    result = []
    pqueue = []

    for i in range(len(lists)):
        try:
            pqueue.append(lists[i].pop(0))
        except Exception:
            pass

    heapify(pqueue)
    val = heappop(pqueue)
    result.append(val)

    while pqueue and len(result) < max_size:
        for i in range(len(lists)):
            try:
                pqueue.append(lists[i].pop(0))
            except Exception:
                pass
        
        heapify(pqueue)

        val = heappop(pqueue)
        result.append(val)

    return result

def xmerge(*ln):
    pqueue = []
    for i in map(iter, ln):
        try:
            pqueue.append((i.next(), i.next))
        except StopIteration:
            pass

    heapify(pqueue)
    while pqueue:
        val, it = pqueue[0]
        yield val
        try:
            heapreplace(pqueue, (it(), it))
        except StopIteration:
            heappop(pqueue)
 

def merge_basic(mylists, max_size=10):
    newlist = []

    for mylist in mylists:
        for elem in mylist:
            newlist.append(elem)

    newlist.sort()

    return newlist[:max_size]

def run_basic():
    a1 = [1, 6, 20, 40, 42, 45, 56, 77, 70, 88]
    a2 = [11, 23, 25, 26, 26, 44, 66, 69, 99]
    a4 = [4, 8, 8, 12, 21, 32, 44, 66, 69]
    a3 = [5, 12, 16, 40, 50, 100, 103, 200]

    set1 = [copy(a1), copy(a2), copy(a3), copy(a4)]
    retval = merge_basic(set1, max_size=8)

def run_pqueue():
    a1 = [1, 6, 20, 40, 42, 45, 56, 77, 70, 88]
    a2 = [11, 23, 25, 26, 26, 44, 66, 69, 99]
    a4 = [4, 8, 8, 12, 21, 32, 44, 66, 69]
    a3 = [5, 12, 16, 40, 50, 100, 103, 200]

    set1 = [copy(a1), copy(a2), copy(a3), copy(a4)]
    retval = merge_pqueue(set1, max_size=8)
    
if __name__ == '__main__':

    import timeit    
    
    print("run_pqueue() %s" % \
        timeit.timeit("run_pqueue()", number=50000,
                      setup="from __main__ import run_pqueue"))

    print("run_basic() %s" % \
        timeit.timeit("run_basic()", number=50000,
                      setup="from __main__ import run_basic"))
    
    a1 = [1, 6, 20, 40, 42, 45, 56, 77, 70, 88]
    a2 = [11, 23, 25, 26, 26, 44, 66, 69, 99]
    a4 = [4, 8, 8, 12, 21, 32, 44, 66, 69]
    a3 = [5, 12, 16, 40, 50, 100, 103, 200]

    set1 = [copy(a1), copy(a2), copy(a3), copy(a4)]
    set2 = [copy(a1), copy(a2), copy(a3), copy(a4)]
    
    print(merge_pqueue(set1, max_size=8))
    print(merge_basic(set2, max_size=8))


