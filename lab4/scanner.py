import re
from symboltable import *
from pif import *


class Scanner:
    def __init__(self, file_path, symbol_table_size):
        self.operators = ["+", "-", "*", "/", "==", "<", "<=", ">", ">=", "=", "<-", "%", ":"]
        self.separators = ["{", "}", "(", ")", "[", "]", ";", " ", "\t", "\n", ","]
        self.reserved_words = ["if", "else", "read", "write", "integer", "string", "return"]

        self.regex_identifier = "^[a-zA-Z_][a-zA-Z0-9_]*$"
        self.regex_constant = "^[+-]?\d+$"

        self.file_path = file_path
        self.symbol_table = SymbolTable(symbol_table_size)
        self.pif = ProgramInternalForm()

    def getTokensFromFile(self):
        with open(self.file_path, 'r') as file:
            f = file.read()

        lines = f.split("\n")

        tokens = []
        for line in lines:
            line_tokens = line.split()

            non_empty_tokens = [token for token in line_tokens if token]

            tokens.extend(non_empty_tokens)

        return tokens

    def checkTypeToken(self):
        tokens = self.getTokensFromFile()

        for token in tokens:

            if token in self.reserved_words:
                self.pif.add_elem_to_list(token, -1, -1)

            elif token in self.separators:
                self.pif.add_elem_to_list(token, -1, -1)

            elif token in self.operators:
                self.pif.add_elem_to_list(token, -1, -1)

            else:
                is_identifier_or_constant = 0

                try:
                    if re.match(self.regex_identifier, token) is not None:
                        self.symbol_table.add(token)
                        position = self.symbol_table.find_position_of_term(token)
                        self.pif.add_elem_to_list(token, token, position)
                        is_identifier_or_constant = 1

                except re.error as e:
                    print("Error:", e)

                try:
                    if re.match(self.regex_constant, token) is not None:
                        self.symbol_table.add(token)
                        position = self.symbol_table.find_position_of_term(token)
                        self.pif.add_elem_to_list(token, token, position)
                        is_identifier_or_constant = 1

                except re.error as e:
                    print("Error:", e)

                if is_identifier_or_constant == 0:
                    raise ValueError(f"lexical error")

    def get_pif(self):
        return self.pif

    def get_symbol_table(self):
        return self.symbol_table
