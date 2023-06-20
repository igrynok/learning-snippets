from typing import List
import heapq


def merge_k_sorted_lists(lists: List[List[int]]) -> List[int]:

    indices = [0] * len(lists)
    heap = []
    result = []

    for i, i_list in enumerate(lists):
        heapq.heappush(heap, (i_list[0], i))

    while len(heap) > 0:
        elem, i = heapq.heappop(heap)
        result.append(elem)
        if indices[i] < len(lists[i]) - 1:
            indices[i] = indices[i] + 1
            heapq.heappush(heap, (lists[i][indices[i]], i))

    return result


if __name__ == '__main__':
    lists = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = merge_k_sorted_lists(lists)
    print(' '.join(map(str, res)))
