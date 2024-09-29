import sys

# Create dictionaries for English and Braille characters
english_to_braille = {
    # Lowercase letters
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',

    # Capital letter indicator (used before capital letters)
    'CAPITAL': '.....O',

    # Numbers (with number indicator before numbers)
    'NUMBER': '..O.OO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',

    # Space
    ' ': ' '
}

braille_to_english = {
    # Lowercase letters
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 'O..OOO': 'z',

    # Numbers (numbers are preceded by the number indicator)
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0',

    # Space
    ' ': ' ',

    # Special indicators
    '.....O': 'CAPITAL',  # Capital letter indicator
    '..O.OO': 'NUMBER'    # Number indicator
}

# Function to convert English to Braille
def english_2_braille(english):
    translated_sentence = []
    for char in english:
        if char.isupper():
            # Add the capital letter indicator
            translated_sentence.append(english_to_braille['CAPITAL'])
            # Then add the symbol for the actual letter in lowercase
            translated_sentence.append(english_to_braille[char.lower()])
        elif char.isdigit():
            # Add number indicator before numbers
            if len(translated_sentence) == 0 or translated_sentence[-1] != english_to_braille['NUMBER']:
                translated_sentence.append(english_to_braille['NUMBER'])
            # Then add the number to the list
            translated_sentence.append(english_to_braille[char])
        elif char == ' ':
            # Only append a space, no other characters
            translated_sentence.append(' ')
        else:
            # Add letters without adding extra spaces or periods
            translated_sentence.append(english_to_braille[char])

    # Join the Braille symbols, removing any unwanted spaces
    return ''.join(translated_sentence).strip()


# Function to convert Braille to English
def braille_2_english(braille):
    translated_sentence = []
    capitalized = False
    numberized = False
    for char in range(0, len(braille), 6):
        # Extract the characters based on six characters for each alphabet letter in Braille
        braille_word = braille[char:char+6]

        # Check if the characters have a number or capital letter indicator
        if braille_word == '.....O':
            capitalized = True
            continue
        if braille_word == '..O.OO':
            numberized = True
            continue

        if braille_word in braille_to_english:
            if numberized:
                translated_sentence.append(braille_to_english[braille_word])
                numberized = False
            elif capitalized:
                translated_sentence.append(braille_to_english[braille_word].upper())
                capitalized = False
            else:
                translated_sentence.append(braille_to_english[braille_word])

    return ''.join(translated_sentence)

# Function to detect if the input is Braille or English
def is_braille(text):
    return all(c in ['O', '.'] for c in text)

# Function to handle command-line input and output
def main():
    if len(sys.argv) < 2:
        print("Please provide input text")
        return

    input_text = " ".join(sys.argv[1:])  # Join the command-line arguments into a single string

    # Determine whether to translate from Braille to English or English to Braille
    if is_braille(input_text):
        print(braille_2_english(input_text))
    else:
        print(english_2_braille(input_text))

if __name__ == "__main__":
    main()
