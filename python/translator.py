#Author: Yousef Hammad
#email: yousefhammad3@cmail.carleton.ca

# Define Braille translation dictionaries
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", "......": " "  # Space
}


english_to_braille = {} #dictionary used to store the english to braille translation

for key, value in braille_to_english.items():
    english_to_braille[value] = key

# Braille capitalization and number indicators
braille_capital = ".....O"
braille_number = ".O.OOO"

numbers = {
    "0": ".OOO..", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO..."
}

# Update English to Braille dictionary to include numbers
english_to_braille.update(numbers)


def is_braille(input_string):
    """
    Check if the input string is in Braille or English.
    Braille strings will have only O and .
    """
    return all(char in "O." for char in input_string)


def braille_to_text(braille_string):
    """
    Convert Braille to English.
    Handle capitalization and numbers as well.
    """
    english_result = []
    capital_mode = False
    number_mode = False

    # Break the Braille string into chunks of 6 characters (Braille cells)
    for i in range(0, len(braille_string), 6):
        braille_char = braille_string[i:i+6]

        if braille_char == braille_capital:
            number_mode = False
            capital_mode = True
            continue
        elif braille_char == braille_number:
            number_mode = True
            continue

        if number_mode:
            # Handle numbers
            for key, value in numbers.items():
                if braille_char == value:
                    english_result.append(key)
                    break

        else:
            number_mode = False
            char = braille_to_english.get(braille_char, "")
            if capital_mode:
                char = char.upper()
                capital_mode = False
            english_result.append(char)

    return "".join(english_result)



def text_to_braille(english_string):
    """
    Convert English to Braille.
    Handle capitalization and numbers as well.
    """
    braille_result = []
    numberMode = False
    
    for char in english_string:
        if char.isupper():
            numberMode = False
            # Add Braille capitalization symbol
            braille_result.append(braille_capital)
            char = char.lower()

        if char.isdigit():
            # Add Braille number symbol and convert the number
            if not(numberMode):
                braille_result.append(braille_number)
                numberMode = True
            braille_result.append(numbers[char])
        else:
            numberMode = False
            # Convert English character to Braille
            braille_result.append(english_to_braille.get(char, "......"))

    return "".join(braille_result)


def main(input_string):
    """
    function used to determine if the input is given in braille or in english, and convert accordingly
    """
    if is_braille(input_string):
        # Convert from Braille to English
        print(braille_to_text(input_string))
    else:
        # Convert from English to Braille
        print(text_to_braille(input_string))


#check this is the main file running
if __name__ == "__main__":
    import sys
    # Accept input from command-line argument
    input_string = sys.argv[1]
    main(input_string)
