# compute the longest common subsequence of two sequences
def longest_common_subsequence(word1: str, word2: str) -> int:
    memo = {}
    return count_lcs(word1, word2, memo, len(word1) - 1, len(word2) - 1)


def count_lcs(w1, w2, memo, i, j):
    if i == -1 or j == -1:
        return 0

    if (i, j) in memo:
        return memo[(i, j)]

    if word1[i] == word2[j]:
        total = count_lcs(w1, w2, memo, i - 1, j - 1) + 1
        memo[(i, j)] = total
        return total
    else:
        total = max(count_lcs(w1, w2, memo, i, j - 1), count_lcs(w1, w2, memo, i - 1, j))
        memo[(i, j)] = total
        return total


if __name__ == '__main__':
    word1 = input()
    word2 = input()
    res = longest_common_subsequence(word1, word2)
    print(res)
