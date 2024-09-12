import argparse

# Braille Dictionary
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......','capital': '.....O', 'number': '.O.OOO',


    " ": "......",".": "..OO.O",  ",": "..O...",  "?": "..O.OO",  "!": "..OOO.",  ":": "..OO..",  ";": "..O.O.",
    "-": "....OO", "/": ".O..O.",  "<": ".OO..O",  ">": "O..OO.", "(": "O.O..O",  ")": ".O.OO.",

    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",

}


#dictionary containing only letters
braille_dict_letters = {k: v for k, v in braille_dict.items() if not k.isdigit() and k != 'number'}
#dictionary containing only numbers
braille_dict_numbers = {k: v for k, v in braille_dict.items() if k.isdigit()}

# reverse dictionary for Braille to English translation
english_dict = {v: k for k, v in braille_dict_letters.items()}
numbers_dict={v: k for k, v in braille_dict_numbers.items()}


# Function checking if the input is Braille or English
def is_braille(input_string):
    return all(c in 'O.' for c in input_string)

# Function translating English to Braille
def english_to_braille(input_string):
    output = []

    is_number = False

    for char in input_string:
        if char.isdigit():
            if not is_number:
                output.append(braille_dict['number'])
                is_number = True
            output.append(braille_dict[char])  #  Braille representation of the digit
        elif char.isalpha():
            if is_number:
                is_number = False  # Reset the number boolean
            if char.isupper():
                output.append(braille_dict['capital'])
                char = char.lower()
            output.append(braille_dict[char])  # Braille representation of the letter
        else:
            if is_number:
                is_number = False
            output.append(braille_dict[' '])  # space representation

    return ''.join(output)


# Function to translate Braille to English
def braille_to_english(input_string):
    output = []
    i = 0
    is_number = False
    while i < len(input_string):
        segment = input_string[i:i+6]
        if segment == braille_dict['capital']:
            i += 6
            segment = input_string[i:i+6]
            if segment in english_dict and english_dict[segment].isalpha():
                # Capitalize the letter that follows
                output.append(english_dict[segment].upper())
        elif segment == braille_dict['number']:
            is_number = True
            i = i + 6
            continue
        else:
            if is_number:
                output.append(str(numbers_dict[segment]))
                if segment == braille_dict[' ']:
                    is_number = False
            else:
                output.append(english_dict[segment])
        i += 6
    return ''.join(output)


# Function that decides whether the input should be translated to English or Braille
def translate(input_string):
    if is_braille(input_string):
        return braille_to_english(input_string)
    else:
        return english_to_braille(input_string)




# A main function for cmd inputs
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs='+')  # Accepts multiple words
    args = parser.parse_args()

    input_string = ' '.join(args.input)

    translation_result = translate(input_string)
    print(translation_result)

if __name__ == "__main__":
    main()