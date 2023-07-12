# compute the longest common subsequence of two sequences
def longest_common_subsequence(word1: str, word2: str) -> int:
    return count_lcs(word1, word2, len(word1) - 1, len(word2) - 1)


def count_lcs(w1, w2, i, j):
    if i == -1 or j == -1:
        return 0
    if word1[i] == word2[j]:
        return count_lcs(w1, w2, i - 1, j - 1) + 1
    else:
        return max(count_lcs(w1, w2, i, j - 1), count_lcs(w1, w2, i - 1, j))


if __name__ == '__main__':
    word1 = input()
    word2 = input()
    res = longest_common_subsequence(word1, word2)
    print(res)
