import sys

alphabet_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO'
}

numbers_to_braille = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

special_chars = {
    'capital': '.....O', 
    'number': '.O.OOO', 
    'space': '......'
}

def main():
    input_string = ' '.join(sys.argv[1:])
    if '.' in input_string:
        print(braille_to_english(input_string))
    else:
        print(english_to_braille(input_string))


def braille_to_english(input):
    text = []
    i = 0
    capital_next = False
    number_next = False
    while i < len(input):
        symbol = input[i:i+6]
        if symbol == special_chars['capital']:
            capital_next = True
        elif symbol == special_chars['number']:
            number_next = True
        elif symbol == special_chars['space']:
            text.append(' ')
            number_next = False
        else:
            for k, v in (numbers_to_braille if number_next else alphabet_to_braille).items(): #loop through k:v pairs of the dicts
                if v == symbol:
                    if capital_next:
                        text.append(k.upper())
                        capital_next = False
                    else:
                        text.append(k)
                    break
        i += 6
    return ''.join(text)


def english_to_braille(input):
    braille = []
    number = False
    for char in input:
        if char.isupper():
            braille.append(special_chars['capital'])
            char = char.lower() #lower so it can be found in the dict

        if char.isdigit():
            if(not number):
                number = True
                braille.append(special_chars['number'])
            braille.append(numbers_to_braille[char])
            continue
        elif not char.isdigit() and number:
            number = False

        if char == ' ':
            braille.append(special_chars['space'])
            number = False
        else:
            braille.append(alphabet_to_braille[char]) #handle both upper and lowercase

    return ''.join(braille)
        


if __name__ == "__main__":
    main()
