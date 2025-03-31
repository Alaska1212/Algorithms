class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class Queue:
    def __init__(self):
        self.front_node = None
        self.rear_node = None

    def push(self, n):
        new_node = Node(n)
        if self.rear_node is None:
            self.front_node = self.rear_node = new_node
        else:
            self.rear_node.next = new_node
            self.rear_node = new_node
        print("ok")

    def pop(self):
        if self.front_node is None:
            print("error")
        else:
            print(self.front_node.value)
            self.front_node = self.front_node.next
            if self.front_node is None:
                self.rear_node = None

    def front(self):
        if self.front_node is None:
            print("error")
        else:
            print(self.front_node.value)

    def size(self):
        count = 0
        current = self.front_node
        while current is not None:
            count += 1
            current = current.next
        print(count)

    def clear(self):
        self.front_node = self.rear_node = None
        print("ok")

    def exit(self):
        print("bye")
        return False



if __name__ == "__main__":
    queue = Queue()
    while True:
        command = input().strip().split()
        if command[0] == "push":
            queue.push(int(command[1]))
        elif command[0] == "pop":
            queue.pop()
        elif command[0] == "front":
            queue.front()
        elif command[0] == "size":
            queue.size()
        elif command[0] == "clear":
            queue.clear()
        elif command[0] == "exit":
            queue.exit()
            break