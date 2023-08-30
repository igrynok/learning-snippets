from typing import List


def min_decreasing_partitions(arr: List[int]) -> int:

    def binary_insert(elem):
        left, right = 0, len(ends) - 1
        first_true_index = -1
        while left <= right:
            mid = (left + right) // 2
            if ends[mid] > elem:
                first_true_index = mid
                right = mid - 1
            else:
                left = mid + 1
        return first_true_index

    ends = []

    for elem in arr:
        first_index = binary_insert(elem)
        if first_index >= 0:
            ends[first_index] = elem
        else:
            ends.append(elem)

    return len(ends)


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = min_decreasing_partitions(arr)
    print(res)