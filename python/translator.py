import sys

# Dictionary for Braille to English conversion
braille_to_letters={
        'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 
        'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j', 
        'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 
        'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't', 
        'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 
        'O..OOO': 'z', '......': ' '}

braille_to_numbers={
        'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
        'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

letters_to_braille = {v: k for k, v in braille_to_letters.items()}
numbers_to_braille = {v: k for k, v in braille_to_numbers.items()}

# Special symbols for Braille
CAPITAL = '.....O'
NUMBER = '.O.OOO'
SPACE = '......' 

def is_braille(text):
    """Check if the input string is in Braille format."""
    return all(c in 'O.' for c in text) and len(text) % 6 == 0

def translate_to_braille(text):
    """Translate English text to Braille."""
    result = ''
    words = text.split()
    for word in words:
        braille =  ''
        if word.isdigit():
            braille = braille + NUMBER
            for digit in word:
                braille = braille + numbers_to_braille[digit]
        else:
            for char in word:
                if char.isupper():
                    braille = braille + CAPITAL
                    char = char.lower()
                braille = braille + letters_to_braille[char]

        result = result+ braille + SPACE
    result = result[0:-6]
    return result

def translate_to_english(braille_text):
    """Translate Braille text to English."""
    result = ''
    i = 0
    while i < len(braille_text):
        char = braille_text[i:i+6]
        if char == CAPITAL:
            i += 6
            next_char = braille_text[i:i+6]
            if next_char in braille_to_letters:
                result = result + braille_to_letters[next_char].upper()
            else:
                result = result + '?'
        elif char == NUMBER:
            i += 6
            number_mode = True
            while i < len(braille_text):
                digit = braille_text[i:i+6]
                if digit in braille_to_numbers:
                    result = result + braille_to_numbers[digit]
                    i += 6
                else:
                    i -= 6
                    break
        else:
            if char in braille_to_letters:
                result = result + braille_to_letters[char]
            else:
                result = result + '?'
        i += 6
    return result

def main():
    if len(sys.argv) < 2:
        text = input("Please provide a string to translate:")
    else:
        text = ' '.join(sys.argv[1:])

    if is_braille(text):
        print(translate_to_english(text))
    else:
        print(translate_to_braille(text))

if __name__ == "__main__":
    main()
