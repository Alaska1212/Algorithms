EMPTY = None


class WordDictionary:
    MULTIPLIER = 37

    def __init__(self, capacity=10007):
        self.capacity = capacity
        self.count = 0
        self.words: list[EMPTY | str] = [EMPTY] * capacity

    def _hash(self, word: str):
        hash_value = 0
        for char in word:
            hash_value = (hash_value * self.MULTIPLIER + ord(char)) % self.capacity
        return hash_value

    def add(self, word: str):
        index = self._hash(word)
        while self.words[index] is not EMPTY:
            if self.words[index] == word:
                return
            index = (index + 1) % self.capacity

        self.count += 1
        self.words[index] = word

    def contains(self, word: str):
        index = self._hash(word)
        while self.words[index] is not EMPTY:
            if self.words[index] == word:
                return True
            index = (index + 1) % self.capacity
        return False

    def unique_words(self):
        return {word for word in self.words if word is not EMPTY}


def unknown_words(dictionary, text_words):
    for word in text_words.unique_words():
        if not dictionary.contains(word):
            return True
    return False


def missing_words(dictionary, text_words):
    for word in dictionary.unique_words():
        if not text_words.contains(word):
            return True
    return False


if __name__ == "__main__":
    n, m = map(int, input().split())

    dictionary = WordDictionary()
    for _ in range(n):
        dictionary.add(input().strip().lower())

    text_words = WordDictionary()
    for _ in range(m):
        line = input().strip().lower()
        current_word = ""

        for char in line:
            if char.isalpha():
                current_word += char
            elif current_word:
                text_words.add(current_word)
                current_word = ""

        if current_word:
            text_words.add(current_word)

    if unknown_words(dictionary, text_words):
        print("Some words from the text are unknown.")
    elif missing_words(dictionary, text_words):
        print("The usage of the vocabulary is not perfect.")
    else:
        print("Everything is going to be OK.")
