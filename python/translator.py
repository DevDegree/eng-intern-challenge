import sys

Braille_to_English = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OOO.O.": "n", "O..OOO": "o",
    "OOOOOO": "p", "OOOOOO": "q", "O..OOO": "r", ".OOOO.": "s", ".OOOOO": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OOO.OO": "y",
    "O..OOO": "z", "......": " ", ".....O": "#", ".....O": "^"
}

English_to_Braille = {v: k for k, v in Braille_to_English.items()}
English_to_Braille.update({
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOOO..", "7": "OOOOO.", "8": "O..OO.", "9": ".OO...", "0": ".OOO..",
    "^": ".....O", "#": ".....O"
})

def translate(input_str):
    if all(c in "O." for c in input_str):  # Braille to English
        result = []
        i = 0
        while i < len(input_str):
            char = input_str[i:i+6]
            if char == ".....O":  # Capital or Number indicator
                next_char = input_str[i+6:i+12]
                if next_char in English_to_Braille.values():  # Number indicator
                    result.append(Braille_to_English.get(next_char, ' '))
                    i += 12
                else:  # Capital indicator
                    result.append(Braille_to_English.get(next_char, ' ').upper())
                    i += 12
            else:
                result.append(Braille_to_English.get(char, ' '))
                i += 6
        return ''.join(result)
    else:  # English to Braille
        result = []
        number_mode = False
        for char in input_str:
            if char.isdigit():
                if not number_mode:
                    result.append(".O.OOO")  # Number indicator
                    number_mode = True
                result.append(English_to_Braille[char])
            elif char.isupper():
                result.append(".....O")  # Capital indicator
                result.append(English_to_Braille[char.lower()])
                number_mode = False
            elif char == ' ':
                result.append('......')  # Braille for space
                number_mode = False
            else:
                result.append(English_to_Braille.get(char, '......'))
                number_mode = False
        return ''.join(result)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python translator.py <string>")
        sys.exit(1)

    input = sys.argv[1]
    output = translate(input)
    print(output)
