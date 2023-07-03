from heapq import heappush, heappop


# find a median of the stream of numbers by creating min- and max-heaps
class MedianOfStream:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def add_number(self, num: float) -> None:
        if len(self.min_heap) == 0 and len(self.max_heap) == 0:
            heappush(self.max_heap, -num)
        elif len(self.min_heap) == 0:
            if -self.max_heap[0] < num:
                heappush(self.min_heap, num)
            else:
                self.min_heap.append(-self.max_heap[0])
                self.max_heap[0] = -num
        else:
            if num >= self.min_heap[0]:
                heappush(self.min_heap, num)
            else:
                heappush(self.max_heap, -num)

            if len(self.min_heap) - len(self.max_heap) > 1:
                heappush(self.max_heap, -heappop(self.min_heap))

            if len(self.max_heap) - len(self.min_heap) > 1:
                heappush(self.min_heap, -heappop(self.max_heap))
        return

    def get_median(self) -> float:

        if len(self.min_heap) == 0:
            return -self.max_heap[0]
        elif len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + -self.max_heap[0]) / 2
        elif len(self.min_heap) < len(self.max_heap):
            return -self.max_heap[0]
        else:
            return self.min_heap[0]


if __name__ == '__main__':
    # sample input: 6 1 2 3 get 4 get
    median_of_stream = MedianOfStream()
    n = int(input())
    for _ in range(n):
        line = input().strip()
        if line == 'get':
            median = median_of_stream.get_median()
            print(f'{median:.1f}')
        else:
            num = float(line)
            median_of_stream.add_number(num)
