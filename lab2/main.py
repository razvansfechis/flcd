from symboltable import SymbolTable  # Assuming you have a separate file for the SymbolTable implementation

if __name__ == "__main__":
    symbol_table = SymbolTable(5)

    symbol_table.add("2")
    print("For 2: ")
    print("Contains term: " + str(symbol_table.contains_term("2")))
    position2 = symbol_table.find_position_of_term("2")
    print(position2)
    print("\n")

    symbol_table.add("7")
    print("For 7: ")
    print("Contains term: " + str(symbol_table.contains_term("7")))
    position7 = symbol_table.find_position_of_term("7")
    print(position7)
    print("\n")

    symbol_table.add("4")
    print("For 4: ")
    print("Contains term: " + str(symbol_table.contains_term("4")))
    position4 = symbol_table.find_position_of_term("4")
    print(position4)
    print("\n")

    print(symbol_table.get_hash_table())
