class MinHeap:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)
        self._sift_up(len(self.data) - 1)

    def pop(self):
        if not self.data:
            raise IndexError("pop from empty heap")
        min_val = self.data[0]
        last_val = self.data.pop()
        if self.data:
            self.data[0] = last_val
            self._sift_down(0)
        return min_val

    def _sift_up(self, idx):
        parent = (idx - 1) // 2
        while idx > 0 and self.data[idx] < self.data[parent]:
            self.data[idx], self.data[parent] = self.data[parent], self.data[idx]
            idx = parent
            parent = (idx - 1) // 2

    def _sift_down(self, idx):
        size = len(self.data)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx

            if left < size and self.data[left] < self.data[smallest]:
                smallest = left
            if right < size and self.data[right] < self.data[smallest]:
                smallest = right
            if smallest == idx:
                break
            self.data[idx], self.data[smallest] = self.data[smallest], self.data[idx]
            idx = smallest

    def __len__(self):
        return len(self.data)

def min_cost_to_add(numbers):
    heap = MinHeap()
    for num in numbers:
        heap.push(num)

    total_cost = 0
    while len(heap) > 1:
        a = heap.pop()
        b = heap.pop()
        cost = a + b
        total_cost += cost
        heap.push(cost)

    return total_cost

if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    print(min_cost_to_add(numbers))
