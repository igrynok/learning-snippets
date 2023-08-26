from typing import List


def get_largest_subarray(arr: List[int], k: int) -> List[int]:

    largest_index = 0
    for i in range(1, len(arr) - k + 1):
        for j in range(k):
            if arr[largest_index + j] < arr[i + j]:
                largest_index = i
                break
            elif arr[largest_index + j] > arr[i + j]:
                break

    return [ arr[largest_index + i] for i in range(k)]


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    k = int(input())
    res = get_largest_subarray(arr, k)
    print(' '.join(map(str, res)))