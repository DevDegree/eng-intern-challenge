import sys

braille_to_english_map = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t", 
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", 
    "O..OOO": "z", "......": " ",
}

braille_to_number_map = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0",
}

braille_to_escape_characters = {
    "......": " ",
    ".....O": "cap",
    ".O.OOO": "num"

}

# Create reverse maps
english_to_braille_map = {val: key for key, val in braille_to_english_map.items()}
number_to_braille_map = {val: key for key, val in braille_to_number_map.items()}
escape_characters_to_braille = {val: key for key, val in braille_to_escape_characters.items()}  

def translate_braille_to_english(input_str: str) -> str:
    """
    Translates a string of Braille characters to English text.

    Args:
        input_str (str): A string of Braille characters where each character is represented by a 6-dot pattern.

    Returns:
        str: The translated English text.
    """
    output = []
    brailles = [input_str[i:i+6] for i in range(0, len(input_str), 6)]
    in_number_mode = False
    is_capital = False # Flag to check if the next character is capital, its not a mode because we only need to capitalize the next character

    for braille in brailles:
        if braille in braille_to_escape_characters:
            escape_char = braille_to_escape_characters[braille]
            if escape_char == "num":
                in_number_mode = True
            elif escape_char == "cap":
                is_capital = True
            elif escape_char == " ":
                output.append(' ')
            continue
        
        if braille == "......":   
            in_number_mode = False
            output.append(' ')
            continue


        # very ugly code but i have only a few hours left to submit 
        if braille in braille_to_number_map and in_number_mode:
            char = braille_to_english_map[braille]
            if is_capital:
                output.append(char.upper())
                is_capital = False
                continue
            output.append(braille_to_number_map[braille])
        else:
            char = braille_to_english_map[braille]
            if is_capital:
                char = char.upper()
                is_capital = False
            output.append(char)

    return ''.join(output)

def translate_english_to_braille(input_str: str) -> str:
    """
    Translates a string of English text to Braille characters.

    Args:
        input_str (str): A string of English text.

    Returns:
        str: The translated Braille characters as a string where each character is represented by a 6-dot pattern.
    """
    output = []
    in_number_mode = False # Flag to check if we are in number mode

    for char in input_str:
        if char.isdigit():
            if not in_number_mode:
                output.append(escape_characters_to_braille['num'])
                in_number_mode = True
            output.append(number_to_braille_map[char])
        else:
            if char == ' ':
                in_number_mode = False # Turn off number mode if there is a space
                output.append(escape_characters_to_braille[' '])
            else:
                if char.isalpha():
                    if char.isupper():
                        output.append(escape_characters_to_braille['cap'])
                        char = char.lower()
                    output.append(english_to_braille_map[char])
                elif char in english_to_braille_map:
                    output.append(english_to_braille_map[char])

    return ''.join(output)



def is_braille(input_str: str) -> bool:
    """
    Checks if a given string is a valid Braille string.

    Args:
        input_str (str): A string to check.

    Returns:
        bool: True if the string is a valid Braille string, False otherwise.
    """
    # I am assuming that even when an user inputs a braille looking string 
    # that is not a multiple of 6, it will be a valid english string. 
    # -> 0.... will be english while 0..... will be braille
    return all(character in {'.', 'O'} for character in input_str) and len(input_str) % 6 == 0


def main():
    input_str = ' '.join(sys.argv[1:])
    if is_braille(input_str):
        output = translate_braille_to_english(input_str)
    else:
        output = translate_english_to_braille(input_str)

    print(output)


if __name__ == '__main__':
    main()