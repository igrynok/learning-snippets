from typing import List


def minimum_total(triangle: List[List[int]]) -> int:
    sums = set()
    generate_sums(sums, triangle[0][0], triangle, 0, 0)
    return min(list(sums))


def generate_sums(sums, sum_level, triangle, level, index):
    if level == len(triangle):
        sums.add(sum_level)
        return
    if level < len(triangle) - 1:
        generate_sums(sums, sum_level + triangle[level + 1][index], triangle, level + 1, index)
        generate_sums(sums, sum_level + triangle[level + 1][index + 1], triangle, level + 1, index + 1)
    else:
        generate_sums(sums, sum_level, triangle, level + 1, index)
        generate_sums(sums, sum_level, triangle, level + 1, index)


if __name__ == '__main__':
    triangle = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = minimum_total(triangle)
    print(res)
