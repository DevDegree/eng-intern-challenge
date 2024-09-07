class Translate:
    def __init__(self) -> None:
        self.braille_to_english = {
    # Letters (Lowercase)
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OO...": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
    
    # Numbers
    ".O.OOOO.....": "1",
    ".O.OOOO.O...": "2",
    ".O.OOOOO....": "3",
    ".O.OOOOO.O..": "4",
    ".O.OOOO..O..": "5",
    ".O.OOOOOO...": "6",
    ".O.OOOOOOO..": "7",
    ".O.OOOO.OO..": "8",
    ".O.OOO.OO...": "9",
    ".O.OOO.OO...": "0",
    
    # Punctuation and special symbols
    "..O...": ".",
    "..OO..": ",",
    "..OOOO": "?",
    "..O.O.": "!",
    "..OO.O": ":",
    "..OOO.": ";",
    "..OOO..": "-",
    "..OOOOO": "/",
    ".OO.OO": "<",
    ".OO.OOO": ">",
    ".OO..O.": "(",
    ".OOOOOO": ")",
    "......": " ", 
    "capital follows" : ".....O",
    "number follows": ".O.OOO"
}

        self.english_to_braille = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'j': '.OO...',
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
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '0': '.OO...', 
    '.': '..O...', 
    ',': '..OO..', 
    '?': '..OOOO', 
    '!': '..O.O.', 
    ':': '..OO.O', 
    ';': '..OOO.', 
    '-': '..OOO..', 
    '/': '..OOOOO', 
    '<': '.OO.OO', 
    '>': '.OO.OOO', 
    '(': '.OO..O.', 
    ')': '.OOOOOO', 
    ' ': '......', 
    'capital_follows' : '.....O', 
    'number_follows' : '.O.OOO'}




    def translate_braille_to_english(self, strings):
        res = []
        char_ptr = 0
        capital_follows = False
        number_follows = False
        while (char_ptr+6) <= len(strings):
            cur_char = str(strings[char_ptr:char_ptr+6])
            if capital_follows:
                res.append(self.braille_to_english[cur_char].upper())
                capital_follows = False
                char_ptr+=6
            elif number_follows:
                res.append(self.braille_to_english[".O.OOO" + cur_char])
                char_ptr+=6
            else:
                if cur_char == ".O.OOO":
                    number_follows = True
                    char_ptr+=6
                    continue
                elif cur_char == ".....O":
                    capital_follows = True
                    char_ptr+=6
                    continue
                else:
                    if cur_char == "OOOOOO":
                        number_follows = False
                    res.append(self.braille_to_english[cur_char])
                    char_ptr+=6
        return ''.join(res)

    def translate_english_to_braille(self, strings):
        res = []

        numberFollows = False
        for char in strings:
            temp_res = ""
            if char.isnumeric():
                if numberFollows == False:
                    temp_res += (self.english_to_braille["number_follows"])
                    numberFollows = True
            elif char.isalpha():
                if char.isupper():
                    temp_res += (self.english_to_braille["capital_follows"])
                    char = char.lower()
            
            if  not char.isnumeric() and numberFollows:
                numberFollows = False
            temp_res += (self.english_to_braille[char])
            res.append(temp_res)
        return ''.join(res)
            


    