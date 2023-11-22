import os
import traceback

from scanner import Scanner

if __name__ == "__main__":
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

