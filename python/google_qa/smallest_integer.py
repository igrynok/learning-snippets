def min_possible_int(digits: str) -> str:

    formatted = '0' + digits + '0'
    result = [0]

    for i in range(1, len(digits) + 1):

        prev = result[i - 1]
        digit = formatted[i]
        next_digit = formatted[i + 1]

        if digit == '?':
            candidate = 1
            if candidate == prev:
                candidate += 1
                if str(candidate) == next_digit:
                    candidate += 1
            elif str(candidate) == next_digit:
                candidate += 1
                if candidate == prev:
                    candidate += 1
            result.append(candidate)
        else:
            result.append(int(digit))

    return ''.join(str(elem) for elem in result if elem != 0)


if __name__ == '__main__':
    digits = input()
    res = min_possible_int(digits)
    print(res)