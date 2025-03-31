class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(0) if self.items else None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def game(n, first_deck, second_deck):
    first = Queue()
    second = Queue()

    for card in first_deck:
        first.push(card)
    for card in second_deck:
        second.push(card)

    moves = 0
    max_moves = 200000

    while not first.is_empty() and not second.is_empty() and moves < max_moves:
        card1 = first.pop()
        card2 = second.pop()

        if (card1 > card2 and not (card1 == n - 1 and card2 == 0)) or (card1 == 0 and card2 == n - 1):
            first.push(card1)
            first.push(card2)
        else:
            second.push(card1)
            second.push(card2)

        moves += 1

    if first.is_empty():
        return f"second {moves}"
    elif second.is_empty():
        return f"first {moves}"
    else:
        return "draw"


if __name__ == "__main__":
    n = int(input().strip())
    first_deck = list(map(int, input().strip().split()))
    second_deck = list(map(int, input().strip().split()))

    print(game(n, first_deck, second_deck))
