import sys
# maps characters from english to braille
braille_map = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    "cap": ".....O",
    "dec": ".O...O",
    "num": ".O.OOO",
    " ": "......",
}
# reverses above mapping
reverse_braille_map = {value: key for key, value in braille_map.items()}
# maps numbers to braille
braille_num_map = {
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
}
# reverses number mapping
reverse_braille_num_map = {value: key for key, value in braille_num_map.items()}


# converts english characters to braille
def english_to_braille(input_str):
    # initializing empty string
    braille_output = ""
    # boolean to check if number prefix needs to be added
    num_mode = False

    for char in input_str:

        if char.isupper():
            braille_output += braille_map["cap"]
            char = char.lower()

        if char.isdigit() and num_mode == False:
            braille_output += braille_map["num"]
            num_mode = True

        if num_mode and char.isdigit():
            braille_output += braille_num_map[char]

        elif char == " ":
            num_mode = False
            braille_output += braille_map[char]

        else:
            braille_output += braille_map[char]

    print(braille_output)


# converts braille string to english
def braille_to_english(input_str):

    english_output = ""

    capitalize_next = False
    number_mode = False
    # splits string into groups of 6
    braille_chars = split_into_groups(input_str)
    # loops through each group of 6 characters
    for braille_char in braille_chars:
        # Checks if the character group matches the capitalization flag
        if braille_char == braille_map["cap"]:
            capitalize_next = True

        elif braille_char == braille_map["num"] or braille_char == braille_map["dec"]:
            number_mode = True
        # Adds the appropriate character to the string
        else:
            if number_mode:
                english_output += reverse_braille_num_map[braille_char]
            elif capitalize_next:
                english_output += reverse_braille_map[braille_char].upper()
                capitalize_next = False
            elif braille_char == braille_map[" "]:
                english_output += " "
                number_mode = False
            else:
                english_output += reverse_braille_map[braille_char]

    print(english_output)


# Splits input string into groups of 6 characters
def split_into_groups(s):
    return [s[i:i + 6] for i in range(0, len(s), 6)]


def identify_language(input_string):
    # Check if the string contains only 'O' and '.' with no spaces
    # if so convert braille to english, otherwise convert english to braille
    if all(char in "O." for char in input_string):
        braille_to_english(input_string)
    else:
        english_to_braille(input_string)


def main():
    # Check input langauge and convert text accordingly
    input_string = ' '.join(sys.argv[1:])
    identify_language(input_string)


if __name__ == "__main__":
    main()