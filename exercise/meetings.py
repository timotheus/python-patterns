def assertEqual(a, b, label):
    try:
        assert(a == b)
        print "%s == %s: %s" % (a, b, label)
    except:
        print("%s != %s: %s" % (a, b, label))


def answer(meetings):
	meetings.sort()

	meeting_count = 0
	prev_start = 0
	prev_end = 0

	for meeting in meetings:
		start = meeting[0]
		end = meeting[1]

		if start >= prev_end:
			meeting_count += 1

			prev_start = start
			prev_end = end
		else:
			break

		
	return meeting_count

if __name__ == '__main__':

    assertEqual(answer([[0, 1], [1, 2], [2, 3], [3, 5], [4, 5]]), 4, 'four meetings')
    assertEqual(answer([[0, 1000000], [42, 43], [0, 1000000], [42, 43]]), 1, 'one meeting')
