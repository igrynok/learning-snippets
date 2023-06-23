class Stack:

    def __init__(self, volume):
        self.capacity = volume
        self.array = [None]*self.capacity
        self.size = 0

    def push(self, item):
        self.array[self.size] = item
        self.size += 1

    def pop(self):
        last_item = self.array[self.size - 1]
        self.array[self.size - 1] = None
        self.size -= 1
        return last_item

    def peek(self):
        return self.array[self.size - 1]

    def print_stack(self):
        print(self.array[:self.size])


if __name__ == '__main__':
    stack = Stack(10)
    stack.push(23)
    stack.push(42)
    stack.push(77)
    stack.print_stack()
    print(stack.peek())
    print(stack.pop())
