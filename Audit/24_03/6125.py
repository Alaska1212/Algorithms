class Queue:
    def __init__(self, maxsize=100):
        self._items = [None] * maxsize
        self._front = 0
        self._back = 0
        self.size = 0
        self.maxsize = maxsize

    def push(self, n):
        if self.size < self.maxsize:
            self._items[self._back] = n
            self._back = (self._back + 1) % self.maxsize
            self.size += 1
            print("ok")
        else:
            print("Queue is full")

    def pop(self):
        if self.size > 0:
            value = self._items[self._front]
            self._front = (self._front + 1) % self.maxsize
            self.size -= 1
            print(value)
        else:
            False

    def front(self):
        if self.size > 0:
            print(self._items[self._front])
        else:
            print("Queue is empty")

    def queue_size(self):
        print(self.size)

    def clear(self):
        self._front = 0
        self._back = 0
        self.size = 0
        print("ok")

    def exit(self):
        print("bye")
        exit()

if __name__ == "__main__":
    queue = Queue()
    while True:
        command = input().split()
        if command[0] == "push":
            queue.push(int(command[1]))
        elif command[0] == "pop":
            queue.pop()
        elif command[0] == "front":
            queue.front()
        elif command[0] == "size":
            queue.queue_size()
        elif command[0] == "clear":
            queue.clear()
        elif command[0] == "exit":
            queue.exit()