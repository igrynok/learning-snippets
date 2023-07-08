from typing import List


def coin_game(coins: List[int], amount: int) -> int:
    sums = set()

    def generate_coins(sums, coins_sum, coins_num, amount, coins):
        if coins_sum == amount:
            sums.add(coins_num)
            return
        elif coins_sum > amount:
            return
        else:
            for coin in coins:
                generate_coins(sums, coins_sum + coin, coins_num + 1, amount, coins)

    generate_coins(sums, 0, 0, amount, coins)

    return len(sums)


if __name__ == '__main__':
    coins = [int(x) for x in input().split()]
    amount = int(input())
    res = coin_game(coins, amount)
    print(res)
