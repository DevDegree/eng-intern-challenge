import sys
from braille import Translate

if __name__ == "__main__":
    t = Translate()
    if len(sys.argv) <= 1:
        print("No args")
    print(t.translate(" ".join(sys.argv[1:])))
