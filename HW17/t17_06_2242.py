class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_bst(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_bst(root.left, value)
    else:
        root.right = insert_bst(root.right, value)
    return root

def f(root):
    if not root:
        return ""
    return root.value + f(root.left) + f(root.right)

if __name__ == "__main__":
    lines = []
    while True:
        line = input().strip()
        if line == '*':
            break
        lines.append(line)

    letters = "".join(lines)
    root = None
    for ch in reversed(letters):
        root = insert_bst(root, ch)
    result = f(root)
    print(result)
