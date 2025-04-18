class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)
        print("ok")

    def pop(self):
        if self.stack:
            print(self.stack.pop())
        else:
            print("error")

    def back(self):
        if self.stack:
            print(self.stack[-1])
        else:
            print("error")

    def size(self):
        print(len(self.stack))

    def clear(self):
        self.stack.clear()
        print("ok")

    def exit(self):
        print("bye")
        return False

if __name__ == "__main__":
    stack = Stack()
    while True:
        try:
            command = input().strip().split()
            if not command:
                continue
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
                stack.exit()
                break
        except EOFError:
            break

