braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f",
    "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
    "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r",
    ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
    "OO.OOO": "y", "O..OOO": "z",
    "......": " ", ".....": ""
}

braille_numbers = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5", 
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
}

braille_special = {
    ".....O": "CAPITAL",   # Capital follows indicator
    ".O...O": "DECIMAL",   # Decimal follows indicator
    ".O.OOO": "NUMBER"     # Number follows indicator
}

braille_punctuation = {
    ".OO.O.": ".",    # Period
    "..O...": ".",    # Decimal point
    "..O.OO": "?",    # Question mark
    ".OOO..": "!",    # Exclamation mark
    ".OO...": ":",    # Colon
    "..OO..": ";",    # Semicolon
    "....OO": "-",    # Hyphen
    ".O..O.": "/",    # Slash
    ".OO..O": "<",    # Less than
    "O...OO": ">",    # Greater than
    "O.O..O": "(",    # Opening parenthesis
    ".O.OOO": ")"     # Closing parenthesis
}

# Combine all Braille to English mappings
braille_to_english.update(braille_numbers)
braille_to_english.update(braille_punctuation)

# English to Braille mapping, lowercase only
english_to_braille = {v: k for k, v in braille_to_english.items()}
# Add mappings for digits 1-0
english_to_braille.update({str(i): k for i, k in zip(range(1, 10), braille_numbers.values())})
english_to_braille.update({"0": braille_numbers[".OOO.."]})
# Add mappings for capitals
english_to_braille.update({chr(i).upper(): braille_special[".....O"] + english_to_braille[chr(i).lower()] for i in range(97, 123)})

def detect_input_type(input_string):
    # Check if input contains only Braille characters (O and .)
    if all(c in "O. " for c in input_string):
        return "braille"
    else:
        return "english"

def translate_braille_to_english(braille_string):
    words = braille_string.split(" ")
    translated = ""
    capitalize_next = False
    number_mode = False

    for word in words:
        i = 0
        while i < len(word):
            braille_char = word[i:i + 6]
            if braille_char in braille_special:
                if braille_special[braille_char] == "CAPITAL":
                    capitalize_next = True
                elif braille_special[braille_char] == "NUMBER":
                    number_mode = True
                elif braille_special[braille_char] == "DECIMAL":
                    # handle decimal point or future specific cases
                    translated += "."
                i += 6
                continue
            if number_mode and braille_char in braille_numbers:
                # Convert to the corresponding number
                char = braille_numbers[braille_char]
            elif braille_char in braille_to_english:
                char = braille_to_english[braille_char]
                if capitalize_next:
                    char = char.upper()
                    capitalize_next = False
                if number_mode and char.isalpha():
                    number_mode = False
            else:
                char = "?"  # unknown character
            translated += char
            i += 6
        translated += " "  # add space after each braille word
    return translated.strip()

def translate_english_to_braille(english_string):
    translated = ""
    number_mode = False
    for char in english_string:
        if char.isdigit() and not number_mode:
            # Switch to number mode
            translated += braille_special[".O.OOO"] + " "  # Number follows
            number_mode = True
        elif char.isalpha() and number_mode:
            # Exit number mode
            number_mode = False
        
        if char in english_to_braille:
            translated += english_to_braille[char] + " "
        else:
            translated += "......"  # unknown char in braille
    return translated.strip()

def main(input_string):
    input_type = detect_input_type(input_string)
    
    if input_type == "braille":
        result = translate_braille_to_english(input_string)
    else:
        result = translate_english_to_braille(input_string)
    
    return result
