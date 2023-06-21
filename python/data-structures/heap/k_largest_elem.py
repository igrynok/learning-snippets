from typing import List
import heapq


def find_kth_largest(nums: List[int], k: int) -> int:
    for i, num in enumerate(nums):
        nums[i] = -num

    heapq.heapify(nums)

    for i in range(k):
        result = -heapq.heappop(nums)

    return result


if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    k = int(input())
    res = find_kth_largest(nums, k)
    print(res)
