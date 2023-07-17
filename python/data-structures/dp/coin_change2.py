from typing import List
from math import inf


# compute the fewest number of coins to make an amount
def coin_change(coins: List[int], amount: int) -> int:

    def min_coins(coins, amount, current_amount, memo):

        if current_amount in memo:
            return memo[current_amount]

        if current_amount == amount:
            return 0
        elif current_amount > amount:
            return inf
        else:
            result = inf
            for coin in coins:
                result = min(result, min_coins(coins, amount, current_amount + coin, memo) + 1)
            memo[current_amount] = result

        return result

    memo = {}
    out = min_coins(coins, amount, 0, memo)

    return out if out != inf else -1


if __name__ == '__main__':
    coins = [int(x) for x in input().split()]
    amount = int(input())
    res = coin_change(coins, amount)
    print(res)
