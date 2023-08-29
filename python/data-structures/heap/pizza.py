from collections import Counter
from heapq import heappush, heappushpop
from math import pi


def pizza_party(radii: List[int], guests: int) -> float:

    pizzas = Counter(radii)
    total = 0
    pizza_heap = []

    for pizza in pizzas:
        heappush(pizza_heap, (-(pizza)**2, 1, pizza))

    while pizza_heap:

        area, count, pizza = pizza_heap[0]

        total += pizzas[pizza]

        if total >= guests:
            return -area*pi

        count += 1
        heappushpop(pizza_heap, (-(pizza)**2/count, count, pizza))

    return 0.0


if __name__ == '__main__':
    radii = [int(x) for x in input().split()]
    guests = int(input())
    res = pizza_party(radii, guests)
    print(f'{res:.4f}')