import sys

english_to_braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", " ": "......", ".": "..OO.O", ",": "..O...", "?": "..O.OO",
    "!": "..OOO.", ":": "..OO..", ";": "..O.O.", "-": "....OO", "/": ".O..O.",
    "<": ".OO..O", "(": "O.O..O", ")": ".O.OO.",
    "Capital follows": ".....O", "Number follows": ".O.OOO", "Decimal follows": ".O...O"
}
braille_to_english = {v: k for k, v in english_to_braille.items()}

number_to_braille = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

braille_to_number = {v: k for k, v in number_to_braille.items()}

def translate_to_braille(english):
    output = []
    number_state = False

    for char in english:
        if char.lower() not in english_to_braille and char not in number_to_braille:
            continue

        elif char.isupper():
            output.append(english_to_braille["Capital follows"])
            output.append(english_to_braille[char.lower()])
            number_state = False
        elif char.isdigit():
            if not number_state:
                output.append(english_to_braille["Number follows"])
                number_state = True
            output.append(number_to_braille[char])
        elif char == ' ':
            output.append(english_to_braille[char])
            number_state = False
        else:
            output.append(english_to_braille[char])

    return ''.join(output)

def translate_to_english(braille):
    output = []
    number_state = False
    capital_next = False
    
    if (len(braille) % 6) != 0:
        return ""
    
    for i in range(0, len(braille), 6):
        braille_unit = braille[i:i+6]

        if braille_unit not in braille_to_english and braille_unit not in braille_to_number:
            continue

        elif braille_to_english[braille_unit] == "Capital follows":
            capital_next = True
        elif braille_to_english[braille_unit] == "Number follows":
            number_state = True
        elif braille_to_english[braille_unit] == " ":
            output.append(" ")
            number_state = False  
        else:
            if number_state:
                output.append(braille_to_number[braille_unit])
            else:
                char = braille_to_english[braille_unit]
                if capital_next:
                    char = char.upper()
                    capital_next = False
                output.append(char)
    
    return ''.join(output)

def main():
    if len(sys.argv) < 2:
        print("No input detected")
        return
    
    input_string = ' '.join(sys.argv[1:])

    if all(char in 'O.' for char in input_string):
        print(translate_to_english(input_string))
    else:
        print(translate_to_braille(input_string))


if __name__ == "__main__":
    main()
