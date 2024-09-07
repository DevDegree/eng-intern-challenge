import sys
from translate import Translate

def isBraille(strings):
    for string in strings:
        for i in range(len(string)):
            char = str(string[i])
            if char != '.' and char != 'O':
                return False
    return True

def main():
    translator = Translate()
    
    result=""
    if isBraille(sys.argv[1:]):
        result = translator.translate_braille_to_english(''.join(sys.argv[1:]))
    else:
        result = translator.translate_english_to_braille(' '.join(sys.argv[1:]))
    print(result)
        

if __name__ == "__main__":
    main()