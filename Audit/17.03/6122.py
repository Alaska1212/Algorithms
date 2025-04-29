class Stack:
    def __init__(self, maxsize = 100):
        self._items = [0 for _ in range(maxsize)]
        self._size = 0
        self._top = 0

#push n — Додайте у стек число n (значення n задається після команди). Програма повинна вивести ok.
    def push(self, n):
        if len (self.items ) < self.maxsize:
            self.items.append(n)
            print("ok")

#pop — Видаліть зі стеку останній елемент. Програма повинна вивести його значення.

    def pop(self):
        print(self.item(self.top))

    def back(self):
        print(self.items[self.top])

    def size(self):
        print(self.top + 1)

    def clear(self):
        self.__init__(len(self._items))
        print("")
