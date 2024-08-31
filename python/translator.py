import sys, re

# Mapping from Braille patterns to English alphabet characters
BRAILLE_TO_ENGLISH = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd',
    'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h',
    '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l',
    'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p',
    'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x',
    'OO.OOO': 'y', 'O..OOO': 'z'
}

# Reverse mapping from English alphabet characters to Braille patterns
ENGLISH_TO_BRAILLE = {char: pattern for pattern, char in BRAILLE_TO_ENGLISH.items()}

# Mapping from Braille patterns to numerical digits
BRAILLE_TO_DIGIT = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 
    'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8',
    '.OO...': '9', '.OOO..': '0'
}

# Reverse mapping from numerical digits to Braille patterns
DIGIT_TO_BRAILLE = {digit: pattern for pattern, digit in BRAILLE_TO_DIGIT.items()}

# Mapping for special Braille characters
BRAILLE_SPECIALS = {
    '.....O': 'CAP', '.O.OOO' : 'NUM', '......' : 'SPACE'
}

# Reverse mapping for special Braille characters
SPECIALS_TO_BRAILLE = {meaning: pattern for pattern, meaning in BRAILLE_SPECIALS.items()}

def convert_english_to_braille(text):
    '''
    Converts English text to Braille representation.
    '''
    result = []
    in_number_mode = False

    for char in text:
        # Handle uppercase letters by adding the capital indicator
        if char.isupper():
            result.append(SPECIALS_TO_BRAILLE['CAP'])
            char = char.lower()
        # Handle digits by adding the number indicator if not already in number mode
        elif char.isdigit() and not in_number_mode:
            result.append(SPECIALS_TO_BRAILLE['NUM'])
            in_number_mode = True
        # Handle spaces by adding the space indicator and resetting number mode
        elif char == ' ':
            result.append(SPECIALS_TO_BRAILLE['SPACE'])
            in_number_mode = False
            continue

        # Append the corresponding Braille pattern based on the character type
        if char in ENGLISH_TO_BRAILLE and not in_number_mode:
            result.append(ENGLISH_TO_BRAILLE[char])
        elif char in DIGIT_TO_BRAILLE:
            result.append(DIGIT_TO_BRAILLE[char])
        else:
            # Handle any unexpected characters
            print(f"Invalid character encountered: {char}")
            sys.exit(1)

    return "".join(result)

def convert_braille_to_english(text):
    '''
    Converts Braille patterns back to English text.
    '''
    result = []
    in_number_mode = False
    in_capital_mode = False

    # Process each Braille character group of 6 characters at a time
    for i in range(0, len(text), 6):
        braille_pattern = text[i:i+6]
        
        # Check for special Braille indicators
        if braille_pattern in BRAILLE_SPECIALS:
            if BRAILLE_SPECIALS[braille_pattern] == 'CAP':
                in_capital_mode = True
                continue
            elif BRAILLE_SPECIALS[braille_pattern] == 'NUM':
                in_number_mode = True
                continue
            else:
                result.append(' ')
                in_number_mode = False
                continue

        # Convert Braille patterns to the corresponding English characters or digits
        if in_number_mode and braille_pattern in BRAILLE_TO_DIGIT:
            result.append(BRAILLE_TO_DIGIT[braille_pattern])
        elif braille_pattern in BRAILLE_TO_ENGLISH:
            char = BRAILLE_TO_ENGLISH[braille_pattern]
            if in_capital_mode:
                result.append(char.upper())
                in_capital_mode = False
            else:
                result.append(char)
        else:
            # Handle any unexpected Braille patterns
            print(f"Invalid Braille pattern encountered: {braille_pattern}")
            sys.exit(1)

    return "".join(result)

def main():
    # Ensure correct input format
    if len(sys.argv) < 2:
        print("Usage: python translator.py <input_text>")
        sys.exit(1)

    # Collect the input text
    input_text = " ".join(sys.argv[1:])

    # Use regex to check if the input is in Braille format (consisting only of '.' and 'O')
    braille_pattern = r'^[.O]+$'
    if len(input_text) % 6 == 0 and re.match(braille_pattern, input_text):
        print(convert_braille_to_english(input_text))
    else:
        print(convert_english_to_braille(input_text))

if __name__ == "__main__":
    main()
