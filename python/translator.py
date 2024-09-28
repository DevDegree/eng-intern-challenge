import sys
from constants import *

def print_text_from_braille(braille):
    """Converts Braille to text then prints text to stdout.
    """
    is_upper = False
    is_number = False

    for i in range(len(braille) // 6):
        converted = BRAILLE_TO_CHAR[braille[i*6:(i+1)*6]]
        if converted == " ":
            is_number = False

        if converted == DECIMAL:
            continue
        elif converted == UPPER:
            is_upper = True
        elif converted == NUMBER:
            is_number = True
        else:
            if is_number:
                converted = (ord(converted)-ord("a")+1)%10
            if is_upper:
                converted = converted.upper()
                is_upper = False
            print(converted, end="")

def print_braille_from_text(text):
    """Converts text to Braille then prints Braille to stdout.
    """
    phrases = text.split()
    is_digit = False
    for i, phrase in enumerate(phrases):
        for char in phrase:
            if char.isdigit() and not is_digit:
                is_digit = True
                print(CHAR_TO_BRAILLE[NUMBER], end="")
            
            if is_digit:
                char = chr((int(char)-1)%10 + ord("a"))
                print(CHAR_TO_BRAILLE[char], end="")
            elif char.isupper():
                print(CHAR_TO_BRAILLE[UPPER], end="")
                print(CHAR_TO_BRAILLE[char.lower()], end="")
            elif char in CHAR_TO_BRAILLE:
                print(CHAR_TO_BRAILLE[char], end="")
            else:
                continue
        if i < len(phrases)-1:
            is_digit = False
            print(CHAR_TO_BRAILLE[" "], end="")

def main():
    data_in = " ".join(sys.argv[1:])
    is_braille = data_in.strip(".O") == ""

    if is_braille:
        print_text_from_braille(data_in)
    else:
        print_braille_from_text(data_in)

if __name__=="__main__":main()
