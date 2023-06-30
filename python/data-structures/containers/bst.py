class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def find(tree, data):
    if tree is None:
        print('False')
        return
    if tree.data == data:
        print('Yes')
        return
    if tree.data > data:
        find(tree.left, data)
    else:
        find(tree.right, data)


def insert(tree, data):
    if tree.data > data and tree.left is None:
        tree.left = Node(data)
        return
    elif tree.data < data and tree.right is None:
        tree.right = Node(data)
        return
    elif tree.data > data:
        insert(tree.left, data)
    else:
        insert(tree.right, data)


def print_tree(tree):
    if tree:
        print(tree.data)
        print_tree(tree.left)
        print_tree(tree.right)


if __name__ == '__main__':
    root = Node(7)
    insert(root, 2)
    insert(root, 11)
    insert(root, 5)
    insert(root, 3)
    insert(root, 6)
    insert(root, 9)
    insert(root, 14)
    insert(root, 13)
    print_tree(root)
    find(root, 13)
    find(root, 33)
