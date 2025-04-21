class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.pos = {}  # id -> index in heap

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.pos[self.heap[i][1]] = i
        self.pos[self.heap[j][1]] = j

    def sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i][0] > self.heap[parent][0]:
                self.swap(i, parent)
                i = parent
            else:
                break

    def sift_down(self, i):
        size = len(self.heap)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i

            if left < size and self.heap[left][0] > self.heap[largest][0]:
                largest = left
            if right < size and self.heap[right][0] > self.heap[largest][0]:
                largest = right

            if largest != i:
                self.swap(i, largest)
                i = largest
            else:
                break

    def add(self, id, priority):
        self.heap.append((priority, id))
        i = len(self.heap) - 1
        self.pos[id] = i
        self.sift_up(i)

    def change(self, id, new_priority):
        i = self.pos[id]
        old_priority = self.heap[i][0]
        self.heap[i] = (new_priority, id)
        if new_priority > old_priority:
            self.sift_up(i)
        else:
            self.sift_down(i)

    def pop(self):
        top = self.heap[0]
        print(top[1], top[0])
        del self.pos[top[1]]

        if len(self.heap) == 1:
            self.heap.pop()
            return

        last = self.heap.pop()
        self.heap[0] = last
        self.pos[last[1]] = 0
        self.sift_down(0)


if __name__ == "__main__":
    pq = PriorityQueue()

    while True:
        try:
            line = input().strip()
            if not line:
                break
            parts = line.split()
            if parts[0] == "ADD":
                pq.add(parts[1], int(parts[2]))
            elif parts[0] == "POP":
                pq.pop()
            elif parts[0] == "CHANGE":
                pq.change(parts[1], int(parts[2]))
        except EOFError:
            break


