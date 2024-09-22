import sys


braille_map = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO",
    " ": "......",
    "1": "O.....#", "2": "O.O...#", "3": "OO....#", "4": "OO.O..#", "5": "O..O..#",
    "6": "OOO...#", "7": "OOOO..#", "8": "O.OO..#", "9": ".OO...#", "0": ".OOO..#"
}


CAPITAL_SYMBOL = ".....O"
NUMBER_SYMBOL = ".O.OOO"

reverse_braille_map = {v: k for k, v in braille_map.items()}


def english_to_braille(text):
    result = []
    number_mode = False 

    for char in text:
        if char.isupper():
            result.append(CAPITAL_SYMBOL)
            char = char.lower()

        if char.isdigit():
            if not number_mode:
                result.append(NUMBER_SYMBOL)
                number_mode = True
        else:
            number_mode = False  

        if char in braille_map:
            if number_mode:
                result.append(braille_map[char].rstrip('#'))
            else:
                result.append(braille_map[char])

    return ''.join(result)


def braille_to_english(braille):
    result = []
    index = 0
    capitalize_next = False
    number_mode = False

    while index < len(braille):
        braille_char = braille[index:index+6]
        index += 6

        if braille_char == CAPITAL_SYMBOL:
            capitalize_next = True
        elif braille_char == NUMBER_SYMBOL:
            number_mode = True
        elif braille_char == "......":
            result.append(" ")
            number_mode = False  
        elif braille_char in reverse_braille_map:
            char_to_add = reverse_braille_map[braille_char]

            if number_mode:
                if char_to_add in "abcdefghi":
                    char_to_add = str("abcdefghij".index(char_to_add) + 1)
                elif char_to_add == 'j':
                    char_to_add = '0'

            if capitalize_next:
                char_to_add = char_to_add.upper()
                capitalize_next = False

            result.append(char_to_add)

    return ''.join(result)


def is_braille(text):
    return all(c in 'O.' for c in text)

def main():
    if len(sys.argv) < 2:
        return
    
    input_text = ' '.join(sys.argv[1:])

    if is_braille(input_text):
        return braille_to_english(input_text)
    else:
        return english_to_braille(input_text)

if __name__ == "__main__":
    output = main()
    print(output)