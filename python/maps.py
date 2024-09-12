import collections
# Mapping from English letters/numbers/symbols to Braille
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
    # Continue for other letters, numbers, and symbols
    'capital_follows': '.....O',  # Capital follows indicator
    'number_follows': '.O.OOO',
    'space': '......',
    # Numbers (e.g., '1' -> 'O.....', following number follows symbol)
    '1': 'O.....',  
    '2': 'O.O...',  
    '3': 'OO....',  
    '4': 'OO.O..',  
    '5': 'O..O..',  
    '6': 'OOO...',  
    '7': 'OOOO..',  
    '8': 'O.OO..',  
    '9': '.OO...',  
    '0': '.OOO..',  
}
braille_to_english_map = collections.defaultdict(list)
for k, v in english_to_braille_map.items():
    braille_to_english_map[v].append(k) ## since '1' and 'a' map to same braille 