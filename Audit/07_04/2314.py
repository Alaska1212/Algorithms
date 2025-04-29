class SearchTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key ):
        node = self
        while True:
            if key < node.key:
                if node.left is None:
                    node.left = SearchTree(key)
                else:
                    node = node.left
            elif key > node.key:
                if node.right is None:
                    node.right = SearchTree(key)
                    break
                else:
                    node = node.right
            else:
                break

    def bigger(self):
        parent = None
        node = self
        while node.right:
            parent = node
            node = node.right

        if node.left:
            node = node.left
            while node.right:
                node = node.right
            return node.key
        return parent.key




if __name__=="__main__":
    lst = [int(x) for x in input().split()]
    if lst[0] == 0:
        print(0)
        exit(0)
    tree = SearchTree(lst[0])
    for i in range(1, len(lst) - 1):
        if lst[i] == 0:
            break
        tree.insert(lst[i])
    print(tree.bigger())