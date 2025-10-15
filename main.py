
from modules.fetch_pdb import fetch_pdb

if __name__ == "__main__":
    result = fetch_pdb(["1TUP", "4HHB", "1A8O"])
    print(result)
