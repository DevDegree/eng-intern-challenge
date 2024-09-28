import sys


DICT = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', 
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......',
    'capital': '.....O', 
    'number': '.O.OOO'
}


def translate_to(phrase):
    is_numeric = False
    translation = ""
    for letter in phrase:
        if letter == " ":
            translation += DICT[" "]
            continue
        if letter.isnumeric() and is_numeric == False:
            translation = translation + DICT["number"]
            is_numeric = True
        elif not letter.isnumeric():
            is_numeric = False
        if letter.isupper():
            translation = translation + DICT["capital"]
            letter = letter.lower()
        if letter in DICT:
            translation += DICT[letter]
    return translation


def translate_from(phrase):
    translation = ""
    is_capital = False
    is_numeric = False
    chars = [phrase[i:i+6] for i in range(0, len(phrase), 6)]
    for char in chars:
        if char == DICT[" "]:
            translation += " "
            is_numeric = False
            continue
        if char == DICT["number"]:
            is_numeric = True
            continue
        elif char == DICT["capital"]:
            is_capital = True
            continue
        for k, v in DICT.items():
            if char == v:
                if is_numeric and k.isdigit():
                    translation += k
                    break
                elif is_capital and k.isalpha():
                    translation += k.upper()
                    is_capital = False
                    break
                elif not is_numeric:
                    translation += k
                    is_numeric = False
                    break

    return translation

    
def main():
    if len(sys.argv) < 2:
        print("Enter a phrase")
        return
    input_str = ' '.join(sys.argv[1:])
    if all(c in ['.', 'O'] for c in input_str):
        print(translate_from(input_str))
    else:
        print(translate_to(input_str))
    
if __name__ == "__main__":
    main()
