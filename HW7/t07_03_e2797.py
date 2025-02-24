EMPTY = None


class HashTable:
    def __init__(self, size=13):
        self._size = size
        self._count = 0
        self._keys: list[EMPTY | int] = [EMPTY for _ in range(size)]

    def hash(self, key: int):
        return key % self._size

    def set(self, key: int):
        i = self.hash(key)
        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                return
            i = (i + 1) % self._size

        self.count += 1
        self.keys[i] = key

    def count(self):
        return self._count


if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    contact = HashTable(size=2 * n)

    for number in numbers:
        contact.set(number)

    print(contact.count())