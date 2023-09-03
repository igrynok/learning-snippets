from typing import List
from bisect import insort_left


def min_days_salads(onions: List[int], k: int, n: int) -> int:
    days = max(onions)
    onion_dict = {}

    for index, onion in enumerate(onions):
        if onion not in onion_dict:
            onion_dict[onion] = [index]
        else:
            onion_dict[onion].append(index)

    count = 0
    matured = []

    for day in range(1, days + 1):

        count += 1
        if day in onion_dict:
            for i in onion_dict[day]:
                insort_left(matured, i)

        adjacent = 0 if len(matured) == 0 else 1
        for m in range(len(matured) - 1):
            if matured[m + 1] - matured[m] == 1:
                adjacent += 1

        salads = adjacent // k

        if salads >= n:
            return count

    return -1


if __name__ == '__main__':
    onions = [int(x) for x in input().split()]
    k = int(input())
    n = int(input())
    res = min_days_salads(onions, k, n)
    print(res)
