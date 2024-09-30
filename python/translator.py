import sys

# English to Braille mapping
ENGLISH_TO_BRAILLE = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    ' ': '......',
    'capital_follows': '.....O',
    'decimal_follows': '.O...O',
    'number_follows': '.O.OOO',
}

# Braille to English mapping
BRAILLE_TO_ENGLISH = {value: key for key, value in ENGLISH_TO_BRAILLE.items()}

# Numbers to Braille mapping
NUMBERS_TO_BRAILLE = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
}

# Braille to Numbers mapping
BRAILLE_TO_NUMBERS = {value: key for key, value in NUMBERS_TO_BRAILLE.items()}

# Convert string of '.' and 'O' into Braille blocks of 6 character strings
def get_braille_symbols(braille_input: str) -> str:
    return [braille_input[i:i+6] for i in range(0, len(braille_input), 6)]

# Translate Braille text into English text
def braille_to_english(braille_input: str) -> str:
    braille_blocks = get_braille_symbols(braille_input)
    english = ""

    capital_follows = False
    number_follows = False

    for symbol in braille_blocks:
        if symbol not in BRAILLE_TO_ENGLISH:
            return f"Unknown braille symbol {symbol} encountered. Please try again with valid symbols."
        
        char = BRAILLE_TO_ENGLISH[symbol]
        
        if char == "capital_follows":
            capital_follows = True
        elif char == "number_follows":
            number_follows = True
        elif char == "decimal_follows":
            english += "."
        elif char == " ":
            # All numbers ended by a space
            number_follows = False
            english += char
        else:
            if number_follows:
                # All following symbols after number_follows symbol are numbers until the next space symbol
                english += BRAILLE_TO_NUMBERS[symbol]
            elif capital_follows:
                # Only one letter capitalized per capital_follows symbol read
                capital_follows = False
                english += char.upper()
            else:
                # Lowercase letters
                english += char
    
    return english

# Translate English text into Braille text
def english_to_braille(english_input: str) -> str:
    braille = ""

    number_follows = False

    for char in english_input:
        if char == " ":
            # All numbers ended by a space
            number_follows = False
            braille += ENGLISH_TO_BRAILLE[char]
        elif char.isdigit():
            # Numbers case
            if not number_follows:
                number_follows = True
                braille += ENGLISH_TO_BRAILLE['number_follows']
            braille += NUMBERS_TO_BRAILLE[char]
        elif char == ".":
            # Decimal case
            braille += ENGLISH_TO_BRAILLE['decimal_follows']
        else:
            # Letters case
            if char.isupper():
                braille += ENGLISH_TO_BRAILLE['capital_follows']
                braille += ENGLISH_TO_BRAILLE[char.lower()]
            else:
                braille += ENGLISH_TO_BRAILLE[char]
    
    return braille
        
# Verify if a string is in Braille
def check_if_braille(input_str: str) -> bool:
    # Braille strings are in blocks of 6 characters and only contain '.' and 'O'
    return len(input_str) % 6 == 0 and set(input_str).issubset({'.', 'O'})

# Translate the input string from Braille to English text, and vice versa
def translate(input_str: str) -> str:
    is_braille = check_if_braille(input_str)

    if is_braille:
        return braille_to_english(input_str)
    else:
        return english_to_braille(input_str)

def main():
    if len(sys.argv) < 2:
        print("No string provided.")
    else:
        input_str = ' '.join(sys.argv[1:])
        translated_text = translate(input_str)
        print(translated_text)

if __name__ == "__main__":
    main()
