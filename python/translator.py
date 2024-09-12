import sys

letters_to_braille_dict = {
   'a': 'O.....',    'b': 'O.O...',    'c': 'OO....',    'd': 'OO.O..',
   'e': 'O..O..',    'f': 'OOO...',    'g': 'OOOO..',    'h': 'O.OO..',
   'i': '.OO...',    'j': '.OOO..',    'k': 'O...O.',    'l': 'O.O.O.',
   'm': 'OO..O.',    'n': 'OO.OO.',    'o': 'O..OO.',    'p': 'OOO.O.',
   'q': 'OOOOO.',    'r': 'O.OOO.',    's': '.OO.O.',    't': '.OOOO.',
   'u': 'O...OO',    'v': 'O.O.OO',    'w': '.OOO.O',    'x': 'OO..OO',
   'y': 'OO.OOO',    'z': 'O..OOO',    ' ': '......',
}

digit_to_braille_dict = {
   '0': '.OOO.O',    '1': 'O.....',    '2': 'O.O...',    '3': 'OO....',
   '4': 'OO.O..',    '5': 'O..O..',    '6': 'OOO...',    '7': 'OOOO..',
   '8': 'O.OO..',    '9': '.OO...'
}

number_sign = '.O.OOO'
capital_sign = '.....O'

## braille_to_letters_dict reverses the key in letters_to_braille_dict
braille_to_letters_dict = {v: k for k, v in letters_to_braille_dict.items()}

## braille_to_digit reverses the keys in digit_to_braille_dict 
braille_to_digit_dict = {v: k for k, v in digit_to_braille_dict.items()} 

## text_to_braille(string) converts given text to braille format
##  Example:  Input: `Hello world`, Output: `.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..`
##  Time: O(n)
def text_to_braille(text):
    converted = ""
    is_number = False
    for char in text:
        if char.isupper():
            converted += capital_sign
            converted += letters_to_braille_dict[char.lower()]
        elif char == ' ':
            converted += letters_to_braille_dict[char]
            prev_number = False
        elif char.isdigit() and not is_number:
            converted += number_sign
            converted += digit_to_braille_dict[char]
            prev_number = True
        elif char.isdigit():
            converted += digit_to_braille_dict[char]
        else:
            converted += letters_to_braille_dict[char]
    return converted    

## braille_to_text(string)  converts given braille to text format
##  Example:  Input: `.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..`, Output: `Hello world`
##  Time: O(n)
def braille_to_text(braille): 
    converted = ""
    is_number = False
    is_capital = False
    
    for i in range(0, len(braille), 6):
        if i + 6 > len(braille):
            break
        word = braille[i:i+6]
        if word == capital_sign:
            is_capital = True
        elif word == number_sign:
            is_number = True
        elif is_number and word in braille_to_digit_dict:
            converted += braille_to_digit_dict[word]
        elif word in braille_to_letters_dict:
            char = braille_to_letters_dict[word]
            converted += char.upper() if is_capital else char
            is_capital = False
            is_number = False
        else:
            converted += word
            is_number = False
    
    return converted

def is_braille(text):
    return all(c in 'O.' for c in text) and len(text) % 6 == 0

##  main() takes in either text or braille and converts it to the other format and exits if not enough arguments are inputted
##  Example:  Input: `.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..`, Output: `Hello world`
##            Input: `Hello world`, Output: `.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..`
##  Time: O(n)
def main():
    if len(sys.argv) < 2:
        print("Usage: python Braille_Translator.py <input_string>")
        sys.exit(1)

    input_string = ' '.join(sys.argv[1:])

    if is_braille(input_string):
        result = braille_to_text(input_string)
        print(result)
    else:
        result = text_to_braille(input_string)
        print(result)

if __name__ == "__main__":
    main()