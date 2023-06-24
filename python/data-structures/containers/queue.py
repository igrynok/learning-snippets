class Queue:
    def __init__(self, volume):
        self.capacity = volume
        self.array = [None] * self.capacity
        self.size = 0
        self.head = 0
        self.tail = -1

    def enqueue(self, item):
        if self.size >= self.capacity:
            raise IndexError('Queue overflow error')
        if self.tail < (self.capacity - 1):
            self.tail += 1
        elif self.tail == self.capacity - 1:
            self.tail = 0
        self.array[self.tail] = item
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError('Queue is empty')
        if self.head < self.capacity - 1:
            self.array[self.head] = None
            self.head += 1
        else:
            self.head = 0
        self.size -= 1

    def peek(self):
        if self.size == 0:
            raise IndexError('Queue is empty')
        return self.array[self.head]

    def print_queue(self):
        print(self.array)


if __name__ == '__main__':
    q = Queue(5)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.print_queue()
    q.dequeue()
    q.dequeue()
    q.print_queue()
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    q.print_queue()
    q.dequeue()
    q.enqueue(7)
    q.print_queue()
