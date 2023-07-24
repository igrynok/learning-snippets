def min_distance(word1: str, word2: str) -> int:
    memo = {}
    count = count_operations(word1, word2, 0, 0, memo)
    print(len(memo))
    return count


def count_operations(word1, word2, i, j, memo):
    if i == len(word1) or j == len(word2):
        rem1 = len(word1) - i
        rem2 = len(word2) - j
        return abs(rem1 - rem2)

    if (i, j) in memo:
        return memo[(i, j)]

    if word1[i] == word2[j]:
        total = count_operations(word1, word2, i + 1, j + 1, memo)
        memo[(i, j)] = total
        return total
    else:
        insert = count_operations(word1, word2, i, j + 1, memo) + 1
        remove = count_operations(word1, word2, i + 1, j, memo) + 1
        replace = count_operations(word1, word2, i + 1, j + 1, memo) + 1

        total = min(insert, remove, replace)
        memo[(i, j)] = total

        return total


if __name__ == '__main__':
    word1 = input()
    word2 = input()
    res = min_distance(word1, word2)
    print(res)
