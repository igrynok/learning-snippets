from typing import List


def count_salads(onions, day, k):
    adj = 0
    salads = 0
    for onion in onions:
        if onion <= day:
            adj += 1
            if adj % k == 0:
                salads += 1
        else:
            adj = 0
    return salads


def min_days_salads(onions: List[int], k: int, n: int) -> int:

    max_days = max(onions)
    min_days = min(onions)

    left, right = min_days, max_days
    first_index = -1

    while left <= right:
        mid = (left + right) // 2
        if count_salads(onions, mid, k) >= n:
            first_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return first_index


if __name__ == '__main__':
    onions = [int(x) for x in input().split()]
    k = int(input())
    n = int(input())
    res = min_days_salads(onions, k, n)
    print(res)
