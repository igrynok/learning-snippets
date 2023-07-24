from typing import List


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:

    intervals.sort()

    i = 0
    while i < len(intervals) - 1:

        x1, x2 = intervals[i]
        y1, y2 = intervals[i+1]

        if y1 <= x2:
            intervals[i:i+2] = [[min(x1, y1), max(x2, y2)]]
        else:
            i += 1

    return intervals


if __name__ == '__main__':
    intervals = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = merge_intervals(intervals)
    for row in res:
        print(' '.join(map(str, row)))