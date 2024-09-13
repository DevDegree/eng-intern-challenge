# Diccionarios de Braille a Inglés
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f",
    "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O..O.": "k", "O.O.O.": "l",
    "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r",
    ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
    "OO.OOO": "y", "O..OOO": "z", ".....O": "CAPS", ".O.OOO": "NUM", "......": " ", ".O...O": "."
}

# Diccionario de Braille para números
braille_to_number = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5", "OOO...": "6",
    "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0", "..OO.O": ".", "..O...": ","
}

# Diccionario de Inglés a Braille
english_to_braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...",
    "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O..O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.",
    "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO", "CAPS": ".....O", "NUM": ".O.OOO", ".": "..OO.O", " ": "......"
}


# Traducción de inglés a Braille
def english_to_braille_translator(text):
    result = ""
    num_state = False

    for char in text:
        if char.isdigit():
            if not num_state:
                result += english_to_braille["NUM"]
                num_state = True
            result += english_to_braille[char]
        else:
            if num_state:
                num_state = False
            if char.isupper():
                result += english_to_braille["CAPS"]
            result += english_to_braille[char.lower()]

    return result


# Traducción de Braille a inglés
def braille_to_english_translator(braille_text):
    result = ""
    capital_state = False
    num_state = False

    for i in range(0, len(braille_text), 6):
        symbol = braille_text[i:i + 6]

        if symbol == english_to_braille["CAPS"]:
            capital_state = True
            continue
        elif symbol == english_to_braille["NUM"]:
            num_state = True
            continue

        if num_state:
            result += braille_to_number.get(symbol, "?")
            if symbol == " ":
                num_state = False
        else:
            if capital_state:
                result += braille_to_english.get(symbol, "?").upper()
                capital_state = False
            else:
                result += braille_to_english.get(symbol, "?")

    return result


# Función de traducción según el input
def translate(text):
    if all(c in "O." for c in text):
        return braille_to_english_translator(text)
    else:
        return english_to_braille_translator(text)
