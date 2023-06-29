class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def find(tree, data):
    if tree is None:
        return False
    if tree.data == data:
        return True
    elif tree.data < data:
        find(tree.right, data)
    else:
        find(tree.left, data)


def insert(tree, data):
    pass
