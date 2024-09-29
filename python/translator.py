import sys

english_to_braille_map = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    ' ': '......',
    'capital_follows': '.....O',
    'number_follows': '.O.OOO',
}

braille_to_english_map = {v: k for k, v in english_to_braille_map.items()}
assert len(english_to_braille_map) == len(braille_to_english_map)

valid_braille_characters = set('O.')

# Read input
text = " ".join(sys.argv[1:])
n = len(text)

# Verify input
if n == 0:
    sys.exit()

# Determine if the string is a valid Braille string
braille_to_english = False
if n % 6 == 0:
    character_set = set(text)
    if character_set == valid_braille_characters:
        braille_to_english = True

# Translate
result = ""
capital_mode = False
number_mode = False

if braille_to_english:
    # Braille to English
    
    for index in range(0, n, 6):
        braille = text[index:index+6]

        if braille == english_to_braille_map['capital_follows']:
            capital_mode = True
        elif braille == english_to_braille_map['number_follows']:
            number_mode = True
        else:
            character = braille_to_english_map[braille]
            if character == ' ':
                number_mode = False
            elif number_mode:
                if character == 'j':
                    character = '0'
                else:
                    number = ord(character) - 96
                    assert 1 <= number and number <= 9
                    character = str(number)
            elif capital_mode:
                character = character.capitalize()
                capital_mode = False
            
            
            result += character
else:
    # English to Braille
    for character in text:
        if character.isnumeric():
            if not number_mode:
                result += english_to_braille_map['number_follows']
                number_mode = True
            
            number = int(character)
            if number == 0:
                result += english_to_braille_map['j']
            else:
                result += english_to_braille_map[chr(96 + number)]
        else:
            if number_mode:
                if character != " ":
                    raise NotImplementedError
                number_mode = False
            
            if character.isupper():
                lowercase_character = character.lower()
                result += english_to_braille_map['capital_follows']
                result += english_to_braille_map[lowercase_character]
            else:
                result += english_to_braille_map[character]

# Fin
print(result)