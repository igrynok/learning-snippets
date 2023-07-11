from typing import List


# compute the largest divisible subset
def find_largest_subset(nums: List[int]) -> int:
    nums.sort()
    max_div = [0] * len(nums)
    for i, num in enumerate(nums):
        max_d = 1
        for j in reversed(range(i)):
            if num % nums[j] == 0:
                max_d = max(max_d, max_div[j] + 1)
                break
        max_div[i] = max_d
    return max(max_div)


if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    res = find_largest_subset(nums)
    print(res)
