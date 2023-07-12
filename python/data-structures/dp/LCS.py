
# compute the longest common subsequence of two sequences
def longest_common_subsequence(word1: str, word2: str) -> int:
    def count_lcs(w1, w2):
        if len(w1) == 0 or len(w2) == 0:
            return 0
        if w1[-1] == w2[-1]:
            return count_lcs(w1[:-1], w2[:-1]) + 1
        else:
            return max(count_lcs(w1, w2[:-1]), count_lcs(w1[:-1], w2))

    return count_lcs(word1, word2)


if __name__ == '__main__':
    word1 = input()
    word2 = input()
    res = longest_common_subsequence(word1, word2)
    print(res)
