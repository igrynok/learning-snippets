from typing import List


def insert_interval(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:

    y1, y2 = new_interval

    first_index_overlapping = -1
    first_index_greater = -1
    count = 0

    for i, interval in enumerate(intervals):
        x1, x2 = interval

        if x1 > y2 and first_index_greater == -1:
            first_index_greater = i

        if not (y1 > x2 or x1 > y2):
            if first_index_overlapping == -1:
                first_index_overlapping = i
            count += 1

    if count > 0:
        intervals[first_index_overlapping: first_index_overlapping + count] = [[min(intervals[first_index_overlapping][0], y1), max(intervals[first_index_overlapping + count - 1][1], y2)]]
    elif first_index_greater == -1:
        intervals = [new_interval]
    else:
        intervals.insert(first_index_greater, new_interval)

    return intervals


if __name__ == '__main__':
    intervals = [[int(x) for x in input().split()] for _ in range(int(input()))]
    new_interval = [int(x) for x in input().split()]
    res = insert_interval(intervals, new_interval)
    for row in res:
        print(' '.join(map(str, row)))
