'''
Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.

Example:
 array = {1, 0} after rearrange array = {0, 1} 


4, 0, 2, 1, 3  -> [3, 4, 2, 0, 1]


Lets say N = size of the array. Then, following holds true :
* All elements in the array are in the range [0, N-1]
* N * N does not overflow for a signed integer
'''


def main(a):
    try:
        a.insert(0, a.pop())
        a.append(a.pop(a.index(0)))
        a.append(a.pop(a.index(1)))
    except ValueError as e:
        print(e)

    return a


if __name__ == '__main__':
    assert(main([1, 0]) == [0, 1])
    assert(main([4, 0, 2, 1, 3]) == [3, 4, 2, 0, 1])
