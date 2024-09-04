import sys

# Braille and English translation maps
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z"
}

braille_to_number = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
}

# Markers
capital_marker = ".....O"
number_marker = ".O.OOO"
space_marker = "......"

# Reverse the dictionaries for English to Braille translation
english_to_braille = {v: k for k, v in braille_to_english.items()}
number_to_braille = {v: k for k, v in braille_to_number.items()}

def englishToBraille(input_string):
    if(len(input_string) == 0):
        raise ValueError("Empty input string")
  
    output = []
    is_number = False

    for char in input_string:
        if(char is not " " and not char.isalpha() and not char.isdigit()):
            raise ValueError("Invalid character in input string")

        if char.isupper():
            output.append(capital_marker)
            char = char.lower()

        if char.isdigit():
            if not is_number:
                output.append(number_marker)
                is_number = True
            output.append(number_to_braille[char])
            continue

        if char == " ":
            output.append(space_marker)
            is_number = False
            continue

        output.append(english_to_braille[char])

    return "".join(output)

def brailleToEnglish(input_string):
    output = []
    is_capital = False
    is_number = False

    if len(input_string) % 6 != 0:
        raise ValueError("Invalid Braille string length")

    if(len(input_string) == 0):
        raise ValueError("Empty input string")

    for i in range(0, len(input_string), 6):
        segment = input_string[i:i+6]

        if segment == space_marker:
            output.append(" ")
            is_number = False
            continue

        if segment == capital_marker:
            is_capital = True
            continue

        if segment == number_marker:
            is_number = True
            continue

        if is_number:
            output.append(braille_to_number[segment])
            continue

        if is_capital:
            output.append(braille_to_english[segment].upper())
            is_capital = False
        else:
            output.append(braille_to_english[segment])

    return "".join(output)

def translate(input_string):
    # Determine if the input is likely English or Braille
    if all(c in "O." for c in input_string):
        return brailleToEnglish(input_string)
    else:
        return englishToBraille(input_string)

if __name__ == "__main__":
    input_string = " ".join(sys.argv[1:])
    output = translate(input_string)
    print(output)
