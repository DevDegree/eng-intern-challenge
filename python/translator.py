import sys

braille_dict = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
    'f': "OO.O..", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
    'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
    'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
    'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
    'z': "O..OOO", ' ': "......", '.': "..OO.O", ',': "..O...", '?': "O..OO.",
    '!': "O.OO.O", ':': "OO..OO", ';': "O.O.O.", '-': "..O..O", '/': ".OO...",
    '(': "O.O.OO", ')': ".OOOOO",'capital':".....O",'number':".O.OOO"
}
braille_number_dict = {'1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..",
    '5': "O..O..", '6': "OO.O..", '7': "OOOO..", '8': "O.OO..", '9': ".OO...",
    '0': ".OOO.."}

english_dict = {value: key for key, value in braille_dict.items()}
english_number_dict = {value: key for key, value in braille_number_dict.items()}

def braille_to_english(braille):
    result = []
    number_mode = False
    i = 0
    while i < len(braille):
        # Get the current 6-character Braille symbol
        symbol = braille[i:i+6]
        
        if english_dict.get(symbol) == 'capital':
            i += 6
            next_symbol = braille[i:i+6]
            result.append(english_dict[next_symbol].upper())
        elif english_dict.get(symbol) == 'number':
            number_mode = True
        else:
            if number_mode and english_number_dict.get(symbol).isdigit():
                result.append(english_number_dict.get(symbol))
            else:
                if number_mode and english_number_dict.get(symbol) == ' ':
                    number_mode = False
                result.append(english_dict.get(symbol))
        i += 6
    return ''.join(result)


def english_to_braille(english):
    string = []
    numeric = False
    for char in english:
        if char.isupper():
            string.append(braille_dict.get('capital'))
            string.append(braille_dict.get(char.lower()))
        elif char.isdigit():
            if not numeric:
                numeric = True
                string.append(braille_dict.get('number'))
            string.append(braille_number_dict.get(char))
        else:
            string.append(braille_dict.get(char))
            if numeric and char == ' ':
                numeric = False
    return ''.join(string)

def verify(input_str):
    return all(c in 'O.' for c in input_str)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_str = ' '.join(sys.argv[1:])
        if verify(input_str):
            print(braille_to_english(input_str))
        else:
            print(english_to_braille(input_str))
    else:
        print("Input invalid, please provide a valid string")
