import sys

braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", "......": " ", "..OO.O": ".", "..O...": ",", "..O.OO": "?",
    "..OOO.": "!", "..OO..": ":", "..O.O.": ";", "....OO": "-", ".O..O.": "/",
    ".OO..O": "<", "O.O..O": "(", ".O.OO.": ")", ".....O": "Capital follows",
    ".O.OOO": "Number follows"
}

english_to_braille = {v: k for k, v in braille_to_english.items()}

number_to_braille = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

def translate_to_braille(text):
    result = []
    number_mode = False
    for char in text:
        if char.isdigit():
            if not number_mode:
                result.append(".O.OOO")
                number_mode = True
            result.append(number_to_braille[char])
        elif char.isalpha():
            if number_mode:
                result.append("......")
                number_mode = False
            if char.isupper():
                result.append(".....O")
            result.append(english_to_braille[char.lower()])
        else:
            if number_mode:
                number_mode = False
            result.append(english_to_braille[char])
    return ''.join(result)

def translate_to_english(braille):
    result = []
    i = 0
    while i < len(braille):
        chunk = braille[i:i+6]
        if chunk == ".....O":
            i += 6
            result.append(braille_to_english[braille[i:i+6]].upper())
        elif chunk == ".O.OOO":
            i += 6
            while i < len(braille) and braille[i:i+6] != "......":
                result.append(str(list(number_to_braille.values()).index(braille[i:i+6]) + 1))
                i += 6
            continue
        else:
            result.append(braille_to_english[chunk])
        i += 6
    return ''.join(result)

def main():
    input_text = ' '.join(sys.argv[1:])
    if all(char in 'O.' for char in input_text):
        print(translate_to_english(input_text))
    else:
        print(translate_to_braille(input_text))

if __name__ == "__main__":
    main()
