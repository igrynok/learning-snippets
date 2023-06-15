import heapq

# where we want to store elements
h = []

# push elements into the heap
heapq.heappush(h, (5, 'medium priority'))
heapq.heappush(h, (7, 'low priority'))
heapq.heappush(h, (1, 'critical'))
heapq.heappush(h, (3, 'high priority'))

# pop the element with the highest priority
print(heapq.heappop(h))

# check the first element
print(h[0])
