import sys

CAPITALIZE = "CAP"
NUMBER = "NUM"

# The map representing Braille characters to English characters
braille_to_english = {
    "O.....": "a1", "O.O...": "b2", "OO....": "c3", "OO.O..": "d4", "O..O..": "e5",
    "OOO...": "f6", "OOOO..": "g7", "O.OO..": "h8", ".OO...": "i9", ".OOO..": "j0",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", ".....O": CAPITALIZE, ".O.OOO": NUMBER, "......": " ",
}

# The reverse map representing English characters to Braille characters
english_to_braille = {}
for k, v in braille_to_english.items():
    if len(v) == 2:
        english_to_braille[v[0]] = k
        english_to_braille[v[1]] = k
    else:
        english_to_braille[v] = k

def translate_to_braille(text):
    """
    Translate the given text to Braille.
    """
    braille_text = ""
    is_number = False
    
    for char in text:
        if char.isupper():
            if is_number:
                raise ValueError("Numbers must be followed by a space or be at the end of the text")
            is_number = False
            braille_text += english_to_braille[CAPITALIZE]
            braille_text += english_to_braille[char.lower()]
        elif char.isdigit():
            if not is_number:
                braille_text += english_to_braille[NUMBER]
                is_number = True
            braille_text += english_to_braille[char]
        else:
            if is_number and char != ' ':
                raise ValueError("Numbers must be followed by a space or be at the end of the text")
            is_number = False
            assert char in english_to_braille, f"Character {char} not found in translation dictionary"
            braille_text += english_to_braille[char]
    
    return braille_text

def translate_to_english(braille_text):
    """
    Translate the given Braille text to English.
    """
    english_text = ""
    capitalize_next = False
    number_mode = False
    
    for i in range(0, len(braille_text), 6):
        char = braille_text[i:i+6]
        assert char in braille_to_english, f"Invalid Braille character: {char}"
        value = braille_to_english[char]
        if value == CAPITALIZE:
            capitalize_next = True
        elif value == NUMBER:
            number_mode = True
        elif value == " ":
            english_text += " "
            number_mode = False
        else:
            if number_mode:
                english_text += value[1] if len(value) == 2 else value
            elif capitalize_next:
                english_text += value[0].upper() if len(value) == 2 else value.upper()
                capitalize_next = False
            else:
                english_text += value[0] if len(value) == 2 else value
    
    return english_text

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text>")
        sys.exit(1)

    text = ' '.join(sys.argv[1:])

    # Detect if the input is Braille or English
    is_braille = all(char in "O." for char in text) && len(text) % 6 == 0

    if is_braille:
        result = translate_to_english(text)
        print(result)
    else:
        result = translate_to_braille(text)
        print(result)

if __name__ == "__main__":
    main()
