import sys

if __name__ == "__main__":
    if (len(sys.argv) <= 1):
        print("Error: Not enough arguments.")
        print("Usage: python3 translator.py <words to translate>")
        exit()