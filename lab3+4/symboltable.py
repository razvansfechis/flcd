from hashtable import HashTable


class SymbolTable:
    def __init__(self, size):
        self.hash_table = HashTable(size)

    def get_hash_table(self):
        return self.hash_table

    def find_position_of_term(self, term):
        return self.hash_table.find_position_of_term(term)

    def contains_term(self, term):
        return self.hash_table.contains_term(term)

    def add(self, term):
        return self.hash_table.add(term)
