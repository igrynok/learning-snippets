def unique_paths(m: int, n: int) -> int:
    def count_paths(m, n, steps_down, steps_right):
        if m == (steps_down + 1) and n == (steps_right + 1):
            return 1

        total = 0
        if steps_down < m - 1:
            total += count_paths(m, n, steps_down + 1, steps_right)
        if steps_right < n - 1:
            total += count_paths(m, n, steps_down, steps_right + 1)

        return total

    return count_paths(m, n, 0, 0)


if __name__ == '__main__':
    m = int(input())
    n = int(input())
    res = unique_paths(m, n)
    print(res)
