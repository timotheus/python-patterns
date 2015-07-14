
def assertEqual(a, b, label):
    try:
        assert(a == b)
        print "%s == %s: %s" % (a, b, label)
    except:
        print("%s != %s: %s" % (a, b, label))


def moveUp(x, car):
    try:
        x[car+1] -= 1
        x[car] += 1
    except IndexError:
        pass


def moveBack(x, car):
    try:
        x[car+1] += 1
        x[car] -= 1
    except IndexError:
        pass


def process(x, avg_car_load):
    new_x = list(x)

    for car, val in enumerate(x):
        if val < avg_car_load:
            moveUp(new_x, car)
        elif val > avg_car_load:
            moveBack(new_x, car)

    return new_x


def answer(x):
    #avg_car_load = sum(x) / float(len(x))
    mysum = sum(x)
    size = len(x)
    while size > 0:
        if mysum % size == 0:
            return size
        size -= 1

    return size

    avg_car_load = sum(x) / len(x)

    while True:
        new_x = process(x, avg_car_load)

        # are the rabbits no longer moving
        if new_x == x:
            print(new_x)
            equal_cars = len(new_x) - len(set(new_x)) + 1
            return equal_cars

        x = list(new_x)



if __name__ == '__main__':
    assertEqual(answer([1, 4, 1]), 3, 'size 3 event total')
    assertEqual(answer([1, 2]), 1, 'size 2 odd total')
    assertEqual(answer([1, 0]), 1, '')
    assertEqual(answer([0, 0, 0]), 3, '')
    assertEqual(answer([1, 0, 20]), 3, '')
    assertEqual(answer([3, 3, 1000000]), 2, '')
    assertEqual(answer([3, 3, 1000000, 22]), 2, '')