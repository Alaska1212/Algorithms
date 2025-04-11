class Node:
    def __init__(self):
        self.children = {}

def insert_path(root, parts):
    node = root
    for part in parts:
        if part not in node.children:
            node.children[part] = Node()
        node = node.children[part]

def print_tree(node, depth=0):
    for name in sorted(node.children.keys()):
        print(' ' * depth + name)
        print_tree(node.children[name], depth + 1)

# Зчитування
n = int(input())
root = Node()

for _ in range(n):
    path = input().strip().split('\\')
    insert_path(root, path)

print_tree(root)
