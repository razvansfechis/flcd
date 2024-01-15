from Grammar import Grammar



def main():
    while True:
        print("Choose an option:")
        print("1. Run Parser 1")
        print("2. Run Parser 2")
        print("3. Run Parser 3")
        print("0. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            sequence_file = "seq1.txt"
            grammar_file = "g1.txt"
        elif choice == '2':
            sequence_file = "seq2.txt"
            grammar_file = "g3.txt"
        elif choice == '3':
            sequence_file = "seq3.txt"
            grammar_file = "g2.txt"
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please select a valid option.")
            continue

        grammar = Grammar(grammar_file)





if __name__ == "__main__":
    main()