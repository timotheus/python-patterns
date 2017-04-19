from common import assertEquals


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

    # day1 meetings consist of the following meetings
    # 0am to 1am, 1am to 2, 2 to 3, 3 to 5 and 4 to 5
    day1_meetings = [
        [0, 1], [1, 2], [2, 3], [3, 5], [4, 5]
    ]

    day1_consecutive = answer(day1_meetings)
    assertEquals(day1_consecutive, 4, 'four meetings')

    # day2 meetings
    day2_meetings = [
        [0, 1000000], [42, 43], [0, 1000000], [42, 43]
    ]

    day2_consecutive = answer(day2_meetings)
    assertEquals(day2_consecutive, 1, 'one meeting')
