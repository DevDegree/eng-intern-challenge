
import sys
from brailles_functions import isit_braille, poof_braille, poof_english

def main():
    NUM = 2
    if len(sys.argv) < NUM:
        raise ValueError("Please provide input to translate.")
    
    ins = ' '.join(sys.argv[1:])

    if isit_braille(ins):
        print(poof_english(ins))
    else:
        print(poof_braille(ins))

if __name__ == "__main__":
    main()
