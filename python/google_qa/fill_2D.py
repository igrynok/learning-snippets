from typing import List
import math


def fill_2d_array(n: int) -> List[List[int]]:

    nums = [num for num in range(1, n*n + 1)]
    answer = []

    def dfs(letter_mask, path):

        if sum(letter_mask) == 0:

            n = int(math.sqrt(len(path)))
            sums = -1
            for i in range(n):
                row_sum = 0
                for j in range(n):
                    row_sum += path[i*n + j]
                if sums == -1:
                    sums = row_sum
                elif sums != row_sum:
                    return

            for i in range(n):
                column_sum = 0
                for j in range(n):
                    column_sum += path[j*n + i]
                if sums != column_sum:
                    return

            diag_sum = 0
            for i in range(n):
                diag_sum += path[i*n + i]
            if sums != diag_sum:
                return

            anti_diag = 0
            for i in range(n - 1, -1, -1):
                anti_diag += path[i*n + i]
            if sums != anti_diag:
                return

            for i in range(n):
                ans = []
                for j in range(n):
                    ans.append(path[i*n + j])
                answer.append(ans)

            return
        for index, mask in enumerate(letter_mask):
            if mask == 1:
                letter_mask[index] = 0
                path.append(nums[index])
                dfs(letter_mask, path)
                path.pop()
                letter_mask[index] = 1


    dfs([1]*(n*n), [])

    return answer[0:n]


if __name__ == '__main__':
    n = int(input())
    res = fill_2d_array(n)
    print(res)
    if not res:
        print("Impossible")
        exit()
    magic_sum = (1 + n ** 2) * n / 2
    if len(res) != n:
        print("Invalid rows")
        exit()
    numbers_used = set()
    for row in res:
        if len(row) != n:
            print("Invalid columns")
        for entry in row:
            if entry < 1 or entry > n ** 2 or not isinstance(entry, int):
                print("Invalid entry")
                exit()
            if entry in numbers_used:
                print("Duplicate numbers")
                exit()
            numbers_used.add(entry)
    for i in range(n):
        if sum(res[i]) != magic_sum:
            print("Invalid sum")
            exit()
        if sum([res[j][i] for j in range(n)]) != magic_sum:
            print("Invalid sum")
            exit()
    if sum([res[i][i] for i in range(n)]) != magic_sum:
        print("Invalid sum")
        exit()
    if sum([res[i][n - i - 1] for i in range(n)]) != magic_sum:
        print("Invalid sum")
        exit()
    print("Valid matrix")
