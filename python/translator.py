import sys

def check_braille(sentence):
    return all(ch in '.O' for ch in sentence)

def main():
    sentence = ' '.join(sys.argv[1:])
    is_braille = check_braille(sentence)

if __name__ == "__main__":
    main()
