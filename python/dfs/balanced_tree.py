class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def height(root: Node):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1


def is_balanced(tree: Node) -> bool:

    if not tree:
        return True

    left_tree_level = height(tree.left)
    right_tree_level = height(tree.right)

    if (abs(left_tree_level - right_tree_level) <= 1) and is_balanced(tree.left) and is_balanced(tree.right):
        return True

    return False

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree


def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)


if __name__ == '__main__':
    tree = build_tree(iter('1 2 4 x 7 x x 5 x x 3 x 6 x x'.split()), int)
    res = is_balanced(tree)
    print('true' if res else 'false')