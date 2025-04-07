class Node:

    def __init__(self, data: int):
        self.data: int = data
        self.next: 'Node | None' = None

class List:

    def __init__(self):
        self.head: 'Node | None' = None
        self.tail: 'Node | None' = None

    def addToTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def Print(self) -> None:
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def RotateRight(self, k: int) -> None:
        if not self.head or not self.head.next or k == 0:
            return
        length = 1
        current = self.head
        while current.next:
            current = current.next
            length += 1
        k = k % length
        if k == 0:
            return
        current.next = self.head
        new_tail = self.head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        self.head = new_head
        self.tail = new_tail


if __name__ == "__main__":
    try:
        n = int(input())
        values = input().split()
    except:
        n = 0
        values = []

    linked_list = List()
    for i in range(n):
        linked_list.addToTail(int(values[i]))

    while True:
        try:
            line = input()
            if not line.strip():
                continue
            k = int(line)
            linked_list.RotateRight(k)
            linked_list.Print()
        except EOFError:
            break
        except:
            continue
