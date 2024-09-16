import sys

# Braille to English Dictionary
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z",
    ".....O": "capital", ".O.OOO": "number",
    "......": " ", ".O..O.": ".", ".O.O..": ",", "O.OOO.": "?", "O..O.O": "!",
    "OO.O..": ":", "O..OO.": ";", "O....O": "-", "O..OOO": "/", "OOO.O.": "<",
    "OOOO.O": ">", "OO.OO.": "(", "OOO.OO": ")"
}

# English to Braille Dictionary
english_to_braille = {v: k for k, v in braille_to_english.items() if v not in ["capital", "number", " "]}

# Convert English to Braille
def english_to_braille_translation(english_text):
    result = []
    for char in english_text:
        if char.isupper():
            result.append(braille_to_english[".....O"])  # Capital prefix
            result.append(english_to_braille[char.lower()])
        elif char.isdigit():
            result.append(braille_to_english[".O.OOO"])  # Number prefix
            result.append(english_to_braille[char])
        elif char in english_to_braille:
            result.append(english_to_braille[char])  # Normal translation (directly mapped using dictionary)
        elif char == " ":
            result.append(braille_to_english["......"])  # Space
    return ''.join(result)

# Function to convert Braille to English
def braille_to_english_translation(braille_text):
    result = []
    i = 0
    while i < len(braille_text):
        symbol = braille_text[i:i + 6]  # Translates Braille symbols 6 characters at a time
        if symbol == braille_to_english[".....O"]:  # Capital prefix
            i += 6  # Skip the prefix
            symbol = braille_text[i:i + 6]
            result.append(braille_to_english[symbol].upper())  # Convert it to English (CAP)
        elif symbol == braille_to_english[".O.OOO"]:  # Number prefix
            i += 6  # Skip the prefix
            symbol = braille_text[i:i + 6]
            result.append(braille_to_english[symbol])  # Number translation
        else:
            result.append(braille_to_english[symbol])  # Normal translation (directly mapped using dictionary)
        i += 6
    return ''.join(result)

# Determine the type of input and translate accordingly
def translate(input_text):
    if input_text.startswith("O") or input_text.startswith("."):
        return braille_to_english_translation(input_text)
    else:
        return english_to_braille_translation(input_text)

# Main function to get the input and output the translated text
if __name__ == "__main__":
    input_text = sys.argv[1]
    print(translate(input_text))