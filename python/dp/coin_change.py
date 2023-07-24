from typing import List


def coin_game(coins: List[int], amount: int) -> int:
    def count_ways(coins_sum, index, amount, coins, memo):
        if coins_sum == amount:
            return 1
        elif coins_sum > amount:
            return 0
        if memo[index][coins_sum] != -1:
            return memo[index][coins_sum]

        total = 0
        for i in range(index, len(coins)):
            total += count_ways(coins_sum + coins[i], i, amount, coins, memo)

        memo[index][coins_sum] = total
        return total

    n = len(coins)
    memo = [[-1 for _ in range(amount + 1)] for _ in range(n + 1)]
    return count_ways(0, 0, amount, coins, memo)


if __name__ == '__main__':
    coins = [int(x) for x in input().split()]
    amount = int(input())
    res = coin_game(coins, amount)
    print(res)
