import os
import traceback

from scanner import Scanner
from finite_automata import FiniteAutomata

def dfa_menu():
    print("\n\tScanner options:")
    print("\t1. Print states.")
    print("\t2. Print alphabet.")
    print("\t3. Print final states.")
    print("\t4. Print transitions.")
    print("\t5. Print initial state.")
    print("\t6. Print is deterministic.")
    print("\t7. Check if sequence is accepted by DFA.")

def dfa_options():

    finite_automaton = FiniteAutomata("files/FA.txt")

    option = -1

    while option != 0:

        dfa_menu()

        print("\nOption: ", end='')
        option = int(input())

        if option == 1:
            print("States: ")
            print(finite_automaton.get_states())
            print()

        elif option == 2:
            print("Alphabet: ")
            print(finite_automaton.get_alphabet())
            print()

        elif option == 3:
            print("Final states: ")
            print(finite_automaton.get_final_states())
            print()

        elif option == 4:
            print(finite_automaton.write_transitions())

        elif option == 5:
            print("Initial state: ")
            print(finite_automaton.get_initial_state())
            print()

        elif option == 6:
            print("Is deterministic?")
            print(finite_automaton.check_if_deterministic())

        elif option == 7:
            print("Your sequence: ")
            sequence = input()

            if finite_automaton.accepts_sequence(sequence):
                print("Sequence is valid")
            else:
                print("Invalid sequence")
        else:
            print("Invalid command!")

        print()

def menu():
    print("0. Exit")
    print("1. Scanner")
    print("2. Finite Automata\n")

if __name__ == "__main__":

    while 1:
        menu()

        print("Command: ", end='')
        user_input = int(input())

        if user_input == 1:
            print("Scanner:\n")

            file_path = "files/p1.txt"
            scanner = Scanner(file_path, symbol_table_size=10)

            st_file_path = "st.out"
            pif_file_path = "pif.out"

            if os.path.exists(st_file_path):
                os.remove(st_file_path)

            if os.path.exists(pif_file_path):
                os.remove(pif_file_path)

            try:
                scanner.checkTypeToken()
                print("\nlexically correct!\n")

                symbol_table = scanner.get_symbol_table().get_hash_table()

                with open("ST.out", "w") as st_file:
                    st_file.write(str(symbol_table))

                pif = scanner.get_pif()

                with open("PIF.out", "w") as pif_file:
                    pif_file.write(str(pif))

            except ValueError as ve:
                traceback.print_exc()

        elif user_input == 2:
            dfa_options()

        elif user_input == 0:
            break

        else:
            print("Invalid input!")
            break