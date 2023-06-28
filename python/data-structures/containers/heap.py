from math import floor


class Heap:
    def __init__(self):
        self.array = []

    def insert(self, key):
        # place the element into the first free leaf then bubble up if needed
        self.array.append(key)

        index = len(self.array) - 1
        while index > 0:
            parent = floor((index - 1) / 2)
            if parent >= 0:
                if self.array[parent] > key:
                    self.array[index], self.array[parent] = self.array[parent], self.array[index]
                    index = parent
                else:
                    break

    def delete_min(self):
        # remove the top, replace with the right most node and bubble down if needed
        key_top = self.array[0]
        self.array[0] = self.array[-1]
        self.array.pop()

        index = 0
        while index < len(self.array):

            left_child = 2*index + 1
            right_child = 2*index + 2

            if left_child < len(self.array) - 1 and right_child < len(self.array) - 1:
                if left_child < right_child:
                    child = left_child
                else:
                    child = right_child

            if child < len(self.array):
                if self.array[child] < self.array[index]:
                    self.array[child], self.array[index] = self.array[index], self.array[child]
                    index = child
                else:
                    break
            else:
                break
        return key_top

    def print_heap(self):
        print(self.array)


if __name__ == '__main__':
    #    8
    #  10   9
    # 12
    heap = Heap()
    heap.insert(8)
    heap.insert(10)
    heap.insert(9)
    heap.insert(12)
    heap.print_heap()
    # insert 3
    heap.insert(3)
    #     3
    #   8    9
    # 12  10
    heap.print_heap()
    heap.delete_min()
    #     8
    #   10  9
    # 12
    heap.print_heap()