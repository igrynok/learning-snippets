class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def find(node, data):
    if node is None:
        return None
    if node.data == data:
        return node
    if node.data > data:
        find(node.left, data)
    else:
        find(node.right, data)


def insert(node, data):
    if node.data > data and node.left is None:
        node.left = Node(data)
        return
    elif node.data < data and node.right is None:
        node.right = Node(data)
        return
    elif node.data > data:
        insert(node.left, data)
    else:
        insert(node.right, data)


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
