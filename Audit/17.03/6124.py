class Node:
    def __init__(self, item ):
        self.item = item
        self.next = None

class Stack:
        def __init__(self):
            self.top = None
            self.count = 0

        def push(self, n):
            new_node = Node(n)
            new_node.next = self.top
            self.top = new_node
            self.count += 1
            print("ok")

        def pop(self):
            if self.top is not None:
                print(self.top.item)
                self.top = self.top.next
                self.count -= 1
            else: print("error")

        def back(self):
            if self.top is not None:
                print(self.top.item)
            else:
                print("error")
        def size(self):
            print(self.count)

        def clear(self):
            self.top = None
            self.count = 0
            print("ok")

if __name__ == "__main__":
    stack = Stack()
    while True:
        command = input().split()
        if command[0] == "push":
            stack.push(int(command[1]))
        elif command[0] == "pop":
            stack.pop()
        elif command[0] == "back":
            stack.back()
        elif command[0] == "size":
            stack.size()
        elif command[0] == "clear":
            stack.clear()
        elif command[0] == "exit":
            print("bye")
            break