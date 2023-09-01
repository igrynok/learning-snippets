from typing import List


def min_cost_to_win(nums: List[int]) -> int:

    dist = {}
    min_cost = 10**9

    for i in range(len(nums)):
        if nums[i] in dist:
            min_cost = min(min_cost, i - dist[nums[i]] + 1)
        else:
            dist[nums[i]] = i

    return min_cost if min_cost != 10**9 else -1


if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    res = min_cost_to_win(nums)
    print(res)