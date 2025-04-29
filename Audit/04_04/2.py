from collections import deque


class Tree:

    def __init__(self, key, parent=None):
        self.key = key
        self.parent = parent
        self.children = []




    def bfs(self, key):
        queue = deque()
        queue.append(self)
        while queue:
            node = queue.popleft()
            if node.key == key:
                return node
            for child in node.children:
                queue.append(child)

    def add(self, parent_key, key):
        parent = self.bfs(parent_key)
        node = Tree(key, parent)
        parent.children.append(node)

    def lca(self, i, j):
        node = self.bfs(i)
        while True:
            pass


if __name__ == "__main__":
    pass