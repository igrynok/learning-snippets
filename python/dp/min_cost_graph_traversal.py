from typing import List


def min_cost_to_visit_every_node(graph: List[List[int]]) -> int:
    dp = [[0] * len(graph) for _ in range(2 ** len(graph))]

    def min_cost(bitmask, node):

        if bitmask == (1 << len(graph)) - 1:
            return 0

        if dp[bitmask][node] != 0:
            return dp[bitmask][node]

        ans = 10e9
        for dest, cost in enumerate(graph[node]):
            if (bitmask & (1 << dest)) == 0 and cost != 0:
                ans = min(ans, min_cost((bitmask | (1 << dest)), dest) + cost)
        dp[bitmask][node] = ans

        return ans

    cost = min_cost(1, 0)

    return cost if cost != 10e9 else -1


if __name__ == '__main__':
    graph = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = min_cost_to_visit_every_node(graph)
    print(res)
