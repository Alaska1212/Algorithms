class Node:

    def __init__(self, data: int):
        self.data: int = data
        self.next: 'Node | None' = None

class List:

    def __init__(self):
        self.head: 'Node | None' = None
        self.tail: 'Node | None' = None

    def addToTail(self, val: int) -> None:
        """Додати число val в кінець Зв’язного Списку"""
        new_node = Node(val)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def Print(self) -> None:
        """Вивести елементи Зв’язного Списку"""
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def PrintReverse(self) -> None:
        """Вивести елементи Зв’язного Списку в зворотному порядку"""
        self._print_reverse(self.head)
        print()

    def _print_reverse(self, node: 'Node | None') -> None:
        if node is None:
            return
        self._print_reverse(node.next)
        print(node.data, end=' ')


n = int(input())
values = input().split()

lst = List()
for i in range(n):
    lst.addToTail(int(values[i]))

lst.Print()
lst.PrintReverse()
