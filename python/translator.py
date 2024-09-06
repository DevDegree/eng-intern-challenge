# Define the Braille mappings
translate_from_braille = {
    "O.....": "a", "O.O...": "b", "OO....": "c",
    "OO.O..": "d", "O..O..": "e", "OOO...": "f",
    "OOOO..": "g", "O.OO..": "h", ".OO...": "i",
    ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
    "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r",
    ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u",
    "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
    "OO.OOO": "y", "O..OOO": "z", ".....O": "cap",
    ".O.OOO": "num", "......": " "
}

translate_from_english = {v: k for k, v in translate_from_braille.items()}
numbers_braille = {
    "1": "O.....", "2": "O.O...", "3": "OO....",
    "4": "OO.O..", "5": "O..O..", "6": "OOO...",
    "7": "OOOO..", "8": "O.OO..", "9": ".OO...",
    "0": ".OOO.."
}

def braille_to_english_translate(braille):
    final_strng = []
    capitalize_next = False
    digits_str = False
    individual_char = [braille[i:i+6] for i in range(0, len(braille), 6)]

    for char in individual_char:
        if char == ".....O":
            capitalize_next = True
        elif char == ".O.OOO":
            digits_str = True
        elif char == "......":
            final_strng.append(" ")
            digits_str = False
        else:
            if digits_str:
                number = translate_from_braille[char]
                final_strng.append(str(list(numbers_braille.values()).index(char) + 1))
            else:
                letter = translate_from_braille[char]
                if capitalize_next:
                    letter = letter.upper()
                    capitalize_next = False
                final_strng.append(letter)

    return ''.join(final_strng)

def english_to_braille_translate(english):
    final_strng = []
    for char in english:
        if char.isdigit():
            final_strng.append(".O.OOO")
            final_strng.append(numbers_braille[char])
        elif char.isupper():
            final_strng.append(".....O")
            final_strng.append(translate_from_english[char.lower()])
        elif char == " ":
            final_strng.append("......")
        else:
            final_strng.append(translate_from_english[char])
    return ''.join(final_strng)

def translate(input_string):
    if set(input_string).issubset({"O", "."}):
        return braille_to_english_translate(input_string)
    else:
        return english_to_braille_translate(input_string)

if __name__ == "__main__":
    input_string = input("Enter the text to translate: ")
    print(translate(input_string))
