import sys

# Unified Braille to English and English to Braille mappings
brailleToEnglish = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 
    'O..OOO': 'z', '..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!',
    '..OO..': ':', '..O.O.': ';', '....OO': '-', '.O..O.': '/', 'O.O..O': '(',
    '.O.OO.': ')'
}

# dictionary for both conversions
englishToBraille = {v: k for k, v in brailleToEnglish.items()}

# Numbers and their Braille equivalents
brailleNumbers = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}
englishNumbers = {v: k for k, v in brailleNumbers.items()}

# Special signs
number_sign = '.O.OOO'  # Number sign
capital_sign = '.....O'  # Capitalization sign
space_sign = '......'  # Braille space

# Check if input is Braille (all O and . characters)
def is_braille(input_text):
    return all(c in 'O.' for c in input_text.replace(' ', ''))

# Convert Braille to English with number and capitalization handling
def convert_braille_to_english(input_text):
    translation = []
    numbers = False
    capitalize = False
    input_text = input_text.strip()

    while input_text:
        braille_char = input_text[:6]
        input_text = input_text[6:]

        if braille_char == space_sign:
            translation.append(' ')
            numbers = False  # Reset number mode after space
        elif braille_char == number_sign:
            numbers = True
        elif braille_char == capital_sign:
            capitalize = True
        elif numbers:
            translation.append(brailleNumbers.get(braille_char, '?'))
        else:
            char = brailleToEnglish.get(braille_char, '?')
            if capitalize:
                translation.append(char.upper())
                capitalize = False
            else:
                translation.append(char)
    
    return ''.join(translation)

# Convert English to Braille with number and capitalization handling
def convert_english_to_braille(input_text):
    translation = []
    numbers = False

    for char in input_text:
        if char == ' ':
            translation.append(space_sign)
            numbers = False  # Reset number mode after space
        elif char.isdigit():
            if not numbers:
                translation.append(number_sign)  # Add number sign only once
                numbers = True
            translation.append(englishNumbers[char])
        elif char.isupper():
            translation.append(capital_sign + englishToBraille[char.lower()])
            numbers = False
        else:
            translation.append(englishToBraille[char])
            numbers = False

    return ''.join(translation)

# added some manual test cases, to just check before running the unit test
def main():
    if len(sys.argv) < 2:
        print("No input detected. Running manual tests...")

        # Manual test cases
        test_cases = [
            {"input": "Hello world", "expected": ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."},
            {"input": "42", "expected": ".O.OOOOO.O..O.O..."},
            {"input": ".....OO.....O.O...OO...........O.OOOO.....O.O...OO....", "expected": "Abc 123"},
            {"input": "xYz", "expected": "OO..OO.....OO.OOOO..OOO"}  # Corrected expected output
        ]

        # Run manual test cases
        for case in test_cases:
            input_text = case["input"]
            expected = case["expected"]

            # Detect if input is Braille or English
            if is_braille(input_text):
                result = convert_braille_to_english(input_text)
            else:
                result = convert_english_to_braille(input_text)

            print(f"Input: {input_text}")
            print(f"Expected: {expected}")
            print(f"Result: {result}")
            print(f"Test {'Passed' if result == expected else 'Failed'}")
            print("-" * 40)

    else:
        input_text = ' '.join(sys.argv[1:])
        
        # Detect whether input is Braille or English and convert accordingly
        if is_braille(input_text):
            print(convert_braille_to_english(input_text))
        else:
            print(convert_english_to_braille(input_text))

if __name__ == "__main__":
    main()
