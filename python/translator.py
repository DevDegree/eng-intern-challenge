import sys

dict_braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z",
    "......": " ", ".....O": "cap", ".O.OOO": "#" 
}


dict_english_to_braille = {v: k for k, v in dict_braille_to_english.items()}

def is_braille(input_str):
    for c in input_str:
        if c not in ('O', '.', ' '):
            return False
    return True

def braille_to_english(braille_input):
    output = []
    i = 0
    number_mode = False

    while i < len(braille_input):
        symbol = braille_input[i:i+6]
        if symbol == ".....O":  
            i += 6
            output.append(dict_braille_to_english.get(braille_input[i:i+6], "[UNKNOWN]").upper())
            i += 6
        elif symbol == ".O.OOO": 
            i += 6
            number_mode = True  
        elif symbol == "......": 
            output.append(" ")
            number_mode = False
            i += 6
        else:
            if number_mode:
                numbers_map = {
                    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
                    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
                }
                output.append(numbers_map.get(symbol, "[UNKNOWN]"))
            else:
                output.append(dict_braille_to_english.get(symbol, "[UNKNOWN]"))
            i += 6
    return "".join(output)


def english_to_braille(english_input):
    output = []
    number_mode = False

    for char in english_input:
        if char == " ":
            output.append("......")
            number_mode = False
        elif char.isupper():
            output.append(dict_english_to_braille['cap'])
            output.append(dict_english_to_braille[char.lower()])
            number_mode = False
        elif char.isdigit(): 
            if not number_mode:
                output.append(dict_english_to_braille['#'])
                number_mode = True
            number_map = {
                "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
                "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
            }
            output.append(number_map[char])
        else:
            output.append(dict_english_to_braille[char])
            number_mode = False
    return "".join(output)




def main():
    input_str = ' '.join(sys.argv[1:])

    if is_braille(input_str):
        print(braille_to_english(input_str))
    else:
        print(english_to_braille(input_str))

if __name__ == "__main__":
    main()
