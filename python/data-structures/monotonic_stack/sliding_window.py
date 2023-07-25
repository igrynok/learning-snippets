from collections import deque
from typing import List


# find a maximum for the sliding window
def sliding_window_maximum(nums: List[int], k: int) -> List[int]:

    stack = deque()
    result = []

    def push(element, index):

        if stack:
            if index - stack[0] >= k:
                stack.popleft()

        while stack and nums[stack[-1]] <= element:
            stack.pop()
        stack.append(index)

    for i in range(k):
        push(nums[i], i)

    result.append(nums[stack[0]])

    for i in range(k, len(nums)):
        push(nums[i], i)
        result.append(nums[stack[0]])

    return result


if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    k = int(input())
    res = sliding_window_maximum(nums, k)
    print(' '.join(map(str, res)))