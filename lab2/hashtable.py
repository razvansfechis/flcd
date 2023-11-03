from pair import Pair


class HashTable:
    def __init__(self, size):
        self.size = size
        self.hashtable = [[] for _ in range(size)]

    def find_position_of_term(self, term):
        pos = self._hash(term)
        if self.hashtable[pos]:
            for i, elem in enumerate(self.hashtable[pos]):
                if elem == term:
                    return Pair(pos, i)
        return None

    def _hash(self, key):
        return int(key) % self.size

    def contains_term(self, term):
        return self.find_position_of_term(term) is not None

    def add(self, term):
        if self.contains_term(term):
            return self.find_position_of_term(term)

        pos = self._hash(term)
        self.hashtable[pos].append(term)

        return self.find_position_of_term(term)

    def __str__(self):
        return f"SymbolTable: {{ \n \t elements={self.hashtable} \n \t size={self.size} \n }}"
