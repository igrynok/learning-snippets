from typing import List


def knapsack(weights: List[int], values: List[int], max_weight: int) -> int:
    memo = {}
    return max_value_count(weights, values, max_weight, 0, 0, memo)


def max_value_count(weights, values, max_weight, weight, i, memo):
    if weight == max_weight or i == len(weights):
        return 0

    if (weight, i) in memo:
        return memo[(weight, i)]

    if weight + weights[i] <= max_weight:
        val1 = values[i] + max_value_count(weights, values, max_weight, weight + weights[i], i + 1, memo)
        val0 = max_value_count(weights, values, max_weight, weight, i + 1, memo)
        max_val = max(val1, val0)
        memo[(weight, i)] = max_val
        return max_val
    else:
        max_val = max_value_count(weights, values, max_weight, weight, i + 1, memo)
        memo[(weight, i)] = max_val
        return max_val


if __name__ == '__main__':
    weights = [int(x) for x in input().split()]
    values = [int(x) for x in input().split()]
    max_weight = int(input())
    res = knapsack(weights, values, max_weight)
    print(res)
