
"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""
LIBRARY_SIZE = 10007

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.deleted = object()

    def _hash(self, key, attempt):
        h1 = hash(key) % self.size
        h2 = 1 + (hash(key) % (self.size - 1))
        return (h1 + attempt * h2) % self.size

    def insert(self, key, value):
        attempt = 0
        while attempt < self.size:
            index = self._hash(key, attempt)
            if self.table[index] is None or self.table[index] is self.deleted or self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            attempt += 1
        raise Exception("Хеш-таблиця переповнена")

    def search(self, key):
        attempt = 0
        while attempt < self.size:
            index = self._hash(key, attempt)
            if self.table[index] is None:
                return None
            if self.table[index] is not self.deleted and self.table[index][0] == key:
                return self.table[index][1]
            attempt += 1
        return None

    def delete(self, key):
        attempt = 0
        while attempt < self.size:
            index = self._hash(key, attempt)
            if self.table[index] is None:
                return
            if self.table[index] is not self.deleted and self.table[index][0] == key:
                self.table[index] = self.deleted
                return
            attempt += 1

library = None
author_table = None

def init():
    """ Викликається 1 раз на початку виконання програми. """
    global library, author_table
    library = HashTable(LIBRARY_SIZE)
    author_table = {}


def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    global library, author_table
    key = (author, title)
    library.insert(key, True)

    if author not in author_table:
        author_table[author] = set()
    author_table[author].add(title)


def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    global library
    key = (author, title)
    return library.search(key) is not None

def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    global library, author_table
    key = (author, title)
    library.delete(key)

    if author in author_table:
        author_table[author].discard(title)
        if not author_table[author]:
            del author_table[author]


def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    global author_table
    return sorted(author_table.get(author, []))  # Повертаємо відсортований список книг автора

