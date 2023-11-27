from typing import List


class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children


def ternary_tree_paths(root: Node) -> List[str]:

    result = []

    if not root:
        return result

    def dfs(node, path):

        if not node.childre:
            result.append(path)
            return

        for child in node.children:
            dfs(child, path + '->' + str(child.val))

    dfs(root, str(root.val))
    return result


# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    num = int(next(nodes))
    children = [build_tree(nodes, f) for _ in range(num)]
    return Node(f(val), children)


if __name__ == '__main__':
    root = build_tree(iter('1 3 2 1 5 0 3 0 4 0'.split()), int)
    res = ternary_tree_paths(root)
    for line in res:
        print(line)
