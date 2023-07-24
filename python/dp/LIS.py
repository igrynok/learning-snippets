from typing import List


# compute the length of longest increasing subsequence
def longest_sub_len(nums: List[int]) -> int:
    dp = [0] * (len(nums))

    for i in range(len(nums)):
        f_max = 0
        for j in range(i):
            if nums[j] < nums[i]:
                f_max = max(dp[j], f_max)
        dp[i] = f_max + 1

    return max(dp) if dp else 0


if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    res = longest_sub_len(nums)
    print(res)
    res = longest_sub_len(nums)
    print(res)
