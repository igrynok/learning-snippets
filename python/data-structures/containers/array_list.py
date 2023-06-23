class ArrayList:
    def __init__(self):
        self.capacity = 10
        self.array = [None] * self.capacity
        self.size = 0

    def add_last(self, elem):
        if self.capacity <= self.size:
            self.resize()
        self.array[self.size] = elem
        self.size += 1

    def add_first(self, elem):
        if self.capacity <= self.size:
            self.resize()
        new_array = [None] * self.capacity
        new_array[0] = elem
        for i in range(self.size):
            new_array[i + 1] = self.array[i]
        self.array = new_array
        self.size += 1

    def remove(self, index):
        if index < self.size:
            for i in range(index, self.size):
                self.array[i] = self.array[i + 1]
            self.array[self.size - 1] = None
            self.size -= 1

    def resize(self):
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def get_elem(self, index):
        return self.array[index]

    def length(self):
        return self.size

    def print_list(self):
        print(self.array[:self.size])


if __name__ == '__main__':
    al = ArrayList()
    for i in range(10):
        al.add_last(i)
    al.print_list()
    for i in range(10):
        al.add_last(i)
    al.print_list()
    print('Get element by index', al.get_elem(10))
    print('Get length of ArrayList', al.length())
    print('Add 0 to the head of the list:')
    al.add_first(0)
    al.print_list()
    print('Remove the element at index 0')
    al.remove(0)
    al.print_list()
