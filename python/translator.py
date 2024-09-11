
import sys

alphabet_to_braille = {
          "a" : "O.....",
          "b" : "O.O...",
          "c" : "OO....",
          "d" : "OO.O..",
          "e" : "O..O..",
          "f" : "OOO...",
          "g" : "OOOO..",
          "h" : "O.OO..",
          "i" : ".OO...",
          "j" : ".OOO..",
          "k" : "O...O.",
          "l" : "O.O.O.",
          "m" : "OO..O.",
          "n" : "OO.OO.",
          "o" : "O..OO.",
          "p" : "OOO.O.",
          "q" : "OOOOO.",
          "r" : "O.OOO.",
          "s" : ".OO.O.",
          "t" : ".OOOO.",
          "u" : "O...OO",
          "v" : "O.O.OO",
          "w" : ".OOO.O",
          "x" : "OO..OO",
          "y" : "OO.OOO",
          "z" : "O..OOO",
          " " : "......",
          "capital_follows" : ".....O",
          "decimal_follows" : ".O...O",
          "number_follows" : ".O.OOO"
     }
number_to_braille = {
          "1" : "O.....",
          "2" : "O.O...",
          "3" : "OO....",
          "4" : "OO.O..",
          "5" : "O..O..",
          "6" : "OOO...",
          "7" : "OOOO..",
          "8" : "O.OO..",
          "9" : ".OO...",
          "0" : ".OOO.."
     }


def braille_to_english(string_input):
    firstletter = 0
    pointer1 = 6
    english_output = []
    is_capital = False
    is_number = False

    # Reverse dictionary for Braille to English translation
    braille_to_letter = {v: k for k, v in alphabet_to_braille.items()}
    braille_to_number = {v: k for k, v in number_to_braille.items()}

    while pointer1 <= len(string_input):
        braille_char = string_input[firstletter:pointer1]

        # Check for control characters (capital and number mode)
        if braille_char == alphabet_to_braille["capital_follows"]:
            is_capital = True
        elif braille_char == alphabet_to_braille["number_follows"]:
            is_number = True
        elif braille_char == alphabet_to_braille[" "]:
            english_output.append(" ")
            is_capital = False
            is_number = False
        else:
            # Translate Braille to English character
            if is_number:
                english_char = braille_to_number.get(braille_char, "")
            else:
                english_char = braille_to_letter.get(braille_char, "")

            # Capitalize if necessary
            if is_capital:
                english_char = english_char.upper()
                is_capital = False

            english_output.append(english_char)

        # Move to the next set of 6 characters
        firstletter += 6
        pointer1 += 6

    return "".join(english_output)

     
def english_to_braille(string_input):
    braille_output = []
    in_number_mode = False  # Keeps track of whether we're in number mode
    
    for char in string_input:
        if char.isdigit():
            if not in_number_mode:
                # Enter number mode and prepend the number follows indicator
                braille_output.append(alphabet_to_braille["number_follows"])
                in_number_mode = True
            braille_output.append(number_to_braille[char])
        elif char == " ":
            braille_output.append(alphabet_to_braille[" "])
            in_number_mode = False  # Exit number mode on space
        elif char.isupper():
            # Handle uppercase letters
            braille_output.append(alphabet_to_braille["capital_follows"])
            braille_output.append(alphabet_to_braille[char.lower()])
            in_number_mode = False  # Exit number mode if a letter appears
        else:
            # Handle lowercase letters and other characters
            braille_output.append(alphabet_to_braille.get(char, alphabet_to_braille[" "]))
            in_number_mode = False  # Exit number mode if a letter appears
    
    return "".join(braille_output)


if __name__ == '__main__':
    input_args = sys.argv[1:]
    input_value = " ".join(input_args)
    
    braille_chars = {"O", "."}
    
    # Check if it's Braille input (only contains 'O' and '.' and is divisible by 6)
    if set(input_value).issubset(braille_chars) and len(input_value) % 6 == 0:
        print(braille_to_english(input_value))
    else:
        print(english_to_braille(input_value))