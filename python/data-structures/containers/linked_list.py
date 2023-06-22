class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, node):
        if not self.head:
            self.head = node
        else:
            node.next_node = self.head
            self.head = node

    def add_last(self, node):
        last_node = self.head
        while last_node.next_node:
            last_node = last_node.next_node
        last_node.next_node = node

    def size(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next_node
        return count

    def remove(self, node):
        candidate = self.head
        prev_node = None
        while candidate:
            if candidate == node:
                if prev_node:
                    prev_node.next_node = candidate.next_node
                else:
                    self.head = candidate.next_node
                break
            prev_node = candidate
            candidate = candidate.next_node

    def print_list(self):
        result = ''
        node = self.head
        while node:
            result = result + str(node.data) + ' '
            node = node.next_node
        print(result)


if __name__ == '__main__':
    # create linked list ll
    ll = LinkedList()
    # create Node n1
    n1 = Node(1)
    # add n1 to ll
    ll.add(n1)
    # print ll
    ll.print_list()
    # add node n2 to the list and print it
    n2 = Node(2)
    ll.add(n2)
    ll.print_list()
    # add node n3 to the end of the list and print it
    n3 = Node(3)
    ll.add_last(n3)
    ll.print_list()
    # print size of the linked list
    print('Size of the linked list:', ll.size())
    # remove n1 and print the list
    ll.remove(n1)
    ll.print_list()
