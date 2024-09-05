import sys

# get the text from the command line arguments
text_list = sys.argv[1:]
# join the text list to form a single string
text = ' '.join(text_list)
# set of characters in the text to check if it is braille or english
text_set = set(text)

character_map = {
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO.O..': 'd',
    'O..O..': 'e',
    'OOO...': 'f',
    'OOOO..': 'g',
    'O.OO..': 'h',
    '.OO...': 'i',
    '.OOO..': 'j',
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o',
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OOO.O': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z',
}

number_map = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0',
}

# character following rules
rules = {
    '.....O': 'capital',
    '.O...O': 'decimal',
    '.O.OOO': 'number',
}

special_characters = {
    '..OO.O': '.',
    '..O...': ',',
    '..O.OO': '?',
    '..OOO.': '!',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '-',
    '.0..0.': '/',
    '.O.O.O': '<',
    'O.O.O.': '>',
    'O.O..O': '(',
    '.O.OO.': ')',
    '......': ' ',
}


def Translate_to_English(braille):
    # split text at every 6 characters
    braille_symbols = [braille[i:i + 6] for i in range(0, len(braille), 6)]
    # initialize translation, capitalize and translation_map
    translation = ''
    capitalize = False
    translation_map = number_map if braille_symbols[0] == '.O.OOO' else character_map

    # iterate through braille symbols
    for char in braille_symbols:
        # check if char is in translation_map
        if char in translation_map:
            # if capitalize is true, then add the uppercase of the char to translation
            # and set capitalize back to false
            if capitalize:
                translation += translation_map[char].upper()
                capitalize = False
            else:
                translation += translation_map[char]

        # check if char is in rules and apply the rule
        elif char in rules:
            if rules[char] == 'capital':
                capitalize = True
            elif rules[char] == 'decimal':
                translation += '.'
            elif rules[char] == 'number':
                translation_map = number_map

        # check if char is a special character
        elif char in special_characters:
            # if special character is a space and the current map is the number map, then
            # change the map to the character map
            if special_characters[char] == ' ' and translation_map == number_map:
                translation_map = character_map

            # add special character to translation
            translation += special_characters[char]


    return translation


def Translate_to_Braille(english):
    # initialize translation, number_list, special_list, character_list and translation_list
    translation = ''
    number_list = list(number_map.keys())
    special_list = list(special_characters.keys())
    character_list = list(character_map.keys())
    translation_list = character_list if english[0].isalpha() else number_list

    # if the first character is a number then add number rule braille character to translation
    if english[0].isnumeric():
        translation += '.O.OOO'

    # iterate through english characters
    for char in english:
        if char in special_characters.values():
            # if the character is a space and numbers were being translated
            # switch back to letters
            if char.isspace() and translation_list == number_list:
                translation_list = character_list

            # if char is a decimal then put decimal rule braille in translation
            if char == '.':
                translation += '.O...O'
            translation += special_list[list(special_characters.values()).index(char)]

        elif char in number_map.values():
            # if number is detected add number rule braille character and switch
            # translation_list to number_list
            if translation_list == character_list:
                translation += '.O.OOO'
                translation_list = number_list
            translation += translation_list[list(number_map.values()).index(char)]

        elif char.lower() in character_map.values():
            # if character is an uppercase letter then add capital rule braille character
            if char.isupper():
                translation += '.....O'
            translation += translation_list[list(character_map.values()).index(char.lower())]

    return translation


# if the set has length 2, and it only contains 'O' and '.' which means it is braille
if len(text_set) == 2 and 'O' in text_set and '.' in text_set:
    english_translation = Translate_to_English(text)
    print(english_translation)
else:
    braille_translation = Translate_to_Braille(text)
    print(braille_translation)
