def nth_prime(n: int) -> int:

    primes = [True]*100000
    primes[0] = primes[1] = False

    count = 0
    result = -1

    for i in range(2, 100000, 1):
        if primes[i]:
            count += 1
            if count == n:
                result = i
                break
            for j in range(i + i, 100000, i):
                primes[j] = False
    return result


if __name__ == '__main__':
    n = int(input())
    res = nth_prime(n)
    print(res)
