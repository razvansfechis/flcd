class Scanner:
    def __init__(self):

        # Special Symbols

        self.operators = ["+", "-", "*", "/", "==", "<", "<=", ">", ">=", "=", "<-", "%", ":"]
        self.separators = ["{", "}", "(", ")", "[", "]", ";", " ", "\t", "\n", ","]
        self.reserved_words = ["if", "else", "read", "write", "integer", "string", "return"]

        # # Identifiers
        #
        # self.letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
        #                 "s", "t", "u", "v", "w", "x", "y", "z",
        #                 "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
        #                 "S", "T", "U", "V", "W", "X", "Y", "Z"]
        #
        # self.digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
