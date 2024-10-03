import sys

# dictionaries
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", "......": " ", ".O.OOO": "#", ".....O": "capital"
}

english_to_braille = {v: k for k, v in braille_to_english.items()}

numbers = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

# reverse mapping for braille to numbers
braille_numbers = {v: k for k, v in numbers.items()}

english_to_braille.update(numbers)

# determine whether the input is braille or English
def is_braille(input_text):
    # Braille strings consist of only 'O' and '.' characters
    return all(c in 'O.' for c in input_text)

# Braille to English
def braille_to_text(braille_input):
    result = []
    i = 0
    number_mode = False
    capital_mode = False
    
    while i < len(braille_input):
        # Braille symbols as a 6 character string reading left to right as stated in the instruction
        braille_char = braille_input[i:i+6]
        i += 6
        
        if braille_char == ".....O":
            capital_mode = True
        elif braille_char == ".O.OOO":
            number_mode = True
        else:
            if number_mode:
                result.append(braille_numbers.get(braille_char, ''))
            elif capital_mode:
                result.append(braille_to_english.get(braille_char, '').upper())
                capital_mode = False
            else:
                result.append(braille_to_english.get(braille_char, ''))
    
    return ''.join(result)

# English to Braille
def text_to_braille(text_input):
    result = []
    number_mode = False
    
    for char in text_input:
        if char.isdigit():
            if not number_mode:
                result.append(".O.OOO")  # number mode with the number sign
                number_mode = True
            result.append(english_to_braille[char])
        elif char.isupper():
            result.append(".....O")  # capital letter sign
            result.append(english_to_braille[char.lower()])
            number_mode = False  # reset number mode after capital letter
        elif char == " ":
            result.append(english_to_braille[char])
            number_mode = False  # reset number mode on space
        else:
            result.append(english_to_braille[char])
            number_mode = False  # reset number mode after a non-number

    return ''.join(result)

def main():
    # combine the inputs into one string to support white space
    input_text = ' '.join(sys.argv[1:])

    # determine if input is Braille or English
    if is_braille(input_text):
        print(braille_to_text(input_text))
    else:
        print(text_to_braille(input_text))

if __name__ == "__main__":
    main()
