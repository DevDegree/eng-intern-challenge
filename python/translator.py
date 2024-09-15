import sys

braille_to_english_letters = {
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO.O..': 'd',
    'O..O..': 'e',
    'OOO...': 'f',
    'OOOO..': 'g',
    'O.OO..': 'h',
    '.OO...': 'i',
    '.OOO..': 'j',
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o',
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OOO.O': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z',
    
    }

braille_to_english_numbers = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0',
    }

def translate_braille_to_english(braille_text):
    reading_numbers = False
    reading_capital = False
    
    
    english_text = ""
    for i in range(0, len(braille_text), 6):
        braille_char = braille_text[i:i+6]
        if braille_char == ".....O":
            # reading capital letter
            reading_capital = True

        elif braille_char == ".O.OOO":
            # reading number(s)
            reading_numbers = True

        elif braille_char == "......":
            # ...... is a space
            reading_numbers = False
            english_text += " "
        
        else:
            if reading_capital:
                english_text += braille_to_english_letters[braille_char].upper()
            elif reading_numbers:
                english_text += braille_to_english_numbers[braille_char]
            else:
                english_text += braille_to_english_letters[braille_char]
            reading_capital = False
            
    return english_text

def translate_english_to_braille(english_text):
    last_read_number = False

    braille_text = ""
    for i in range(len(english_text)):
        if english_text[i].isalpha():

            if english_text[i].isupper():
                # reading capital letter
                braille_text += ".....O"
                braille_text += next(key for key, value in braille_to_english_letters.items() if value == english_text[i].lower())
            
            else:
                braille_text += next(key for key, value in braille_to_english_letters.items() if value == english_text[i])
            last_read_number = False

        elif english_text[i] == " ":
            braille_text += "......"
            last_read_number = False

        else:
            if last_read_number:
                braille_text += next(key for key, value in braille_to_english_numbers.items() if value == english_text[i])
            else:
                braille_text += ".O.OOO"
                braille_text += next(key for key, value in braille_to_english_numbers.items() if value == english_text[i])
            last_read_number = True

    return braille_text

def process_input(input_text):
    if input_text[0] == '.' or (input_text[0] == 'O' and input_text[1] == '.'):
        return translate_braille_to_english(input_text)
    else:
        return translate_english_to_braille(input_text)

def main():

    if len(sys.argv) < 2:
        print("Usage: python translator.py <input_text>")
        sys.exit(1)
    
    if len(sys.argv) > 2:
        input_text = " ".join(sys.argv[1:])
    else:
        input_text = sys.argv[1]
    result = process_input(input_text)
    print(result)

if __name__ == "__main__":
    main()
