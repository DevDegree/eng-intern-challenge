import sys

# Braille dictionary for letters and punctuation
brailleDict = {
    "A": "O.....",
    "B": "O.O...",
    "C": "OO....",
    "D": "OO.O..",
    "E": "O..O..",
    "F": "OOO...",
    "G": "OOOO..",
    "H": "O.OO..",
    "I": ".OO...",
    "J": ".OOO..",
    "K": "O...O.",
    "L": "O.O.O.",
    "M": "OO..O.",
    "N": "OO.OO.",
    "O": "O..OO.",
    "P": "OOO.O.",
    "Q": "OOOOO.",
    "R": "O.OOO.",
    "S": ".OO.O.",
    "T": ".OOOO.",
    "U": "O...OO",
    "V": "O.O.OO",
    "W": ".OOO.O",
    "X": "OO..OO",
    "Y": "OO.OOO",
    "Z": "O..OOO",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
    ".": ".O...O",
    " ": "......",  # Space
    ".": "..OO.O", # Decimal point
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OO.O",
    "'": "....O.",
    ":": "O..OOO",
    ";": "O..OO.",
    "-": "....OO",
    "capital": ".....O",  # Capital letter indicator
    "number": ".O.OOO",   # Number indicator
}

# Braille map for numbers
numMap = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
    ".": ".O...O",
}

def translate(text):

    result = ""
    index = 0
    is_braille = True
    is_number = False

    # Determine if the input text is Braille or English
    for char in text:
        if char not in {'O', '.'}:
            is_braille = False

    # Translate from English to Braille
    if not is_braille:
        while index < len(text):
            char = text[index]

            if char.isupper():
                result += ".....O" + brailleDict[char]
            elif char.isdigit():
                if index > 0 and text[index - 1].isdigit():
                    result += brailleDict[char]
                else:
                    result += ".O.OOO" + brailleDict[char]
            elif char == ".":
                result += ".O...O"
            else:
                result += brailleDict[char.upper()]
            index += 1

    # Translate from Braille to English
    while index < len(text):
        braille_char = text[index:index + 6]
        index += 6

        if braille_char == "......" and is_number:
            is_number = False
            result += ' '

        elif braille_char == ".....O":  # Capital letter indicator
            braille_char = text[index:index + 6]
            index += 6
            for letter, braille in brailleDict.items():
                if braille == braille_char:
                    result += letter.upper()
                    is_number = False
                    break
        elif braille_char == ".O.OOO":  # Number indicator
            is_number = True
            braille_char = text[index:index + 6]
            index += 6
            for number, braille in numMap.items():
                if braille == braille_char:
                    result += number
                    break
        else:
            if is_number:
                for number, braille in numMap.items():
                    if braille == braille_char:
                        result += number
                        break
            else:
                for letter, braille in brailleDict.items():
                    if braille == braille_char:
                        if is_number:
                            result += letter
                        else:
                            result += letter.lower()
                        break

    return result

# Main program
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the program with a string to translate.")
        sys.exit(1)

    input_text = " ".join(sys.argv[1:])
    output_text = translate(input_text)
    print(output_text)