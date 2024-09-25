import sys 

braille_mapping_chars = {
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
    'capital': '.....O',
    'number': '.O.OOO'
}

braille_mapping_nums = {
    '0': '.OOO..',  
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
}

english_mapping_chars = dict((reversed(item) for item in braille_mapping_chars.items()))
english_mapping_nums = dict((reversed(item) for item in braille_mapping_nums.items()))

def is_english(s: str) -> bool:

    return any(char not in {"O", "."} for char in s)

def translate_to_braille(s: str) -> str:
    
    translation = ""
    lst = list(s)
    
    all_numbers = False

    for i in lst:

        if i.isdigit():
            
            if not all_numbers:
                all_numbers = True
                translation += braille_mapping_chars["number"]

            translation += braille_mapping_nums[i]

        elif i == ' ':
            all_numbers = False
            translation += braille_mapping_chars[' ']

        else:

            if i.isupper(): 
                translation += braille_mapping_chars["capital"] + braille_mapping_chars[i.lower()]

            else:
                translation += braille_mapping_chars[i]

    return translation

def translate_to_english(s: str) -> str:
    
    translation = ""
    lst = list(s)

    all_numbers = False
    make_upper = False

    for i in range(0, len(lst), 6):
        
        chunk = "".join(lst[i : i + 6])

        if chunk == '......':
            all_numbers = False
            translation += english_mapping_chars[chunk]

        elif english_mapping_chars[chunk] == "number" or all_numbers:

            if not all_numbers:
                all_numbers = True
                continue

            translation += english_mapping_nums[chunk]

        else:
            if chunk == braille_mapping_chars["capital"]:
                make_upper = True
                continue

            translation += english_mapping_chars[chunk].upper() if make_upper else english_mapping_chars[chunk]
            make_upper = False

    return translation



def translator():
    s = " ".join(sys.argv[1:])

    to_braille = is_english(s)
    
    if to_braille: return translate_to_braille(s)

    return translate_to_english(s)


print(translator())
