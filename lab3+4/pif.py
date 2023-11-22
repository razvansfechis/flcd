from pair import *


class ProgramInternalForm:
    def __init__(self):
        self.list_of_pairs = []

    def add_elem_to_list(self, value, hashed_value, position):
        self.list_of_pairs.append(Pair(value, Pair(hashed_value, position)))

    def __str__(self):
        return '\n'.join(map(str, self.list_of_pairs))
