import sys

# Dictionaries for Braille letters and numbers
braille_to_letters = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z',
}

letters_to_braille = {v: k for k, v in braille_to_letters.items()}

braille_to_numbers = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0',
}

numbers_to_braille = {v: k for k, v in braille_to_numbers.items()}

# Braille indicators
capital_indicator = '.....O'
number_indicator = '.O.OOO'
space_indicator = '......'

def is_braille(input_str):
    return all(char in 'O.' for char in input_str) and len(input_str) % 6 == 0

def braille_to_english(braille):
    result = []
    is_number = False
    is_capital = False
    i = 0

    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol == capital_indicator:
            is_capital = True
            i += 6
        elif symbol == number_indicator:
            is_number = True
            i += 6
        elif symbol == space_indicator:
            result.append(' ')
            is_number = False
            i += 6
        else: 
            if is_number:
                result.append(braille_to_numbers[symbol])
            elif is_capital:
                result.append(braille_to_letters[symbol].upper())
                is_capital = False
            else:
                try:
                    result.append(braille_to_letters[symbol])
                except KeyError as e:
                    # unknown symbol, ignore and proceed
                    print("Unknown symbol: ", symbol)
                    pass
            i += 6

    return ''.join(result)

def english_to_braille(text):
    result = []
    is_number = False
    
    for char in text:
        if char.isdigit():
            if not is_number:
                result.append(number_indicator)
                is_number = True
            result.append(numbers_to_braille[char])
        elif char.isalpha():
            if is_number:
                # is_number = False
                # unexpected case! ignore and proceed
                pass
            
            if char.isupper():
                result.append(capital_indicator)
                char = char.lower()
            result.append(letters_to_braille[char])
        elif char == ' ':
            result.append(space_indicator)
            is_number = False

    return ''.join(result)

def translate(input_str):
    if is_braille(input_str):
        return braille_to_english(input_str)
    else:
        return english_to_braille(input_str)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python translate.py <string>")
        sys.exit(1)

    input_str = " ".join(sys.argv[1:])  # Join all arguments into one string
    output = translate(input_str)
    print(output)
