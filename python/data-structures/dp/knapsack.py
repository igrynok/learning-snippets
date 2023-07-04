from typing import List


def knapsack_weight_only(weights: List[int]) -> List[int]:
    sums = set()
    memo = [[False for _ in range(sum(weights) + 1)] for _ in range(len(weights) + 1)]
    generate_sums(weights, memo, sums, 0, len(weights))
    return list(sums)


def generate_sums(weights, memo, sums, level_sum, n):
    if memo[n][level_sum]:
        return
    if n == 0:
        sums.add(level_sum)
        return
    generate_sums(weights, memo, sums, level_sum, n - 1)
    generate_sums(weights, memo, sums, level_sum + weights[n - 1], n - 1)
    memo[n][level_sum] = True


if __name__ == '__main__':
    weights = [int(x) for x in input().split()]
    res = knapsack_weight_only(weights)
    res.sort()
    for i in range(len(res)):
        print(res[i], end='')
        if i != len(res) - 1:
            print(' ', end='')
    print()
