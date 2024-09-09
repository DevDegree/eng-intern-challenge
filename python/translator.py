import sys

def braille2text(braille_str):
    return "hello"

def text2braille(word_list):
    return "......"

def main():
    if len(sys.argv) > 1:
        text2braille(sys.argv)
    elif len(sys.argv[0]) % 6 == 0 and sys.argv[0].count(".") + sys.argv[0].count("O") == len(sys.argv[0]):
        braille2text(sys.argv[0])
    else: 
        text2braille(sys.argv)

if __name__ == '__main__':
    main()