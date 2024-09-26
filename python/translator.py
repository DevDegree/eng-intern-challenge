import sys

# Braille to English dictionary (letters and numbers separated logically)
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", "O..OOO": "z",
    ".O.OOO": "NUMBER", " ": "......"
}

# Numbers are separate and prefixed with the number symbol
numbers_to_braille = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

# Punctuation to Braille mapping
punctuation_to_braille = {
    ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "OO....",
    ";": "..O.O.", "-": "....OO", "/": ".O..O.", "<": ".OO..O", ">": "O..OO.", "(": "O.O..O", ")": ".OOO.."
}

# Reverse punctuation mapping for Braille to English
braille_to_punctuation = {v: k for k, v in punctuation_to_braille.items()}

# English to Braille dictionary (reverse of the Braille to English for letters)
english_to_braille = {v: k for k, v in braille_to_english.items() if v not in ['NUMBER', ' ']}

# Add capital handling by prefixing with capital symbol
capital_symbol = ".....O"
for letter, braille in list(english_to_braille.items()):
    if letter.islower():
        english_to_braille[letter.upper()] = capital_symbol + braille

# Special symbols
number_symbol = ".O.OOO"
space_symbol = "......"

def translate_to_english(braille_str):
    braille_letters = [braille_str[i:i+6] for i in range(0, len(braille_str), 6)]
    translation = []
    is_capital = False
    is_number = False
    
    for symbol in braille_letters:
        if symbol == capital_symbol:
            is_capital = True
        elif symbol == number_symbol:
            is_number = True
        elif symbol == space_symbol:
            translation.append(" ")
            is_number = False
        else:
            letter = None
            if is_number:
                # Manually search for the number
                for num, braille in numbers_to_braille.items():
                    if braille == symbol:
                        letter = num
                        break
                if letter is None:
                    is_number = False
            else:
                letter = braille_to_english.get(symbol, braille_to_punctuation.get(symbol, None))
            
            if letter:
                if is_capital:
                    letter = letter.upper()
                    is_capital = False
                translation.append(letter)

    return "".join(translation)

def translate_to_braille(english_str):
    translation = []
    is_number_sequence = False

    for char in english_str:
        if char == " ":
            translation.append(space_symbol)
            is_number_sequence = False
        elif char.isdigit():
            if not is_number_sequence:
                translation.append(number_symbol)
                is_number_sequence = True
            translation.append(numbers_to_braille[char])
        elif char in punctuation_to_braille:
            translation.append(punctuation_to_braille[char])
        else:
            is_number_sequence = False
            if char.isupper():
                translation.append(capital_symbol)
                translation.append(english_to_braille[char.lower()])
            else:
                translation.append(english_to_braille[char])

    return "".join(translation)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_str = ' '.join(sys.argv[1:])
        if "O" in input_str or "." in input_str:
            print(translate_to_english(input_str))
        else:
            print(translate_to_braille(input_str))

