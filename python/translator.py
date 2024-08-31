import sys

"""
SOLUTION WALKTHROUGH:
1. how to determine whether or not the input is in braille or english? ---------------------------------------------
    - of course, if it is braille, len(words) == 1 and len(characters) % 6 == 0, but that could also be an english input
        - ie: python3 translator.py jester
    - perhaps the user wanted to translate "O.O" (commonly used as an internet emoji) from english to braille
        - how can we know that this is not braille?

2. a solution to the above problem (more of a compromise) ---------------------------------------------
    - we know for sure that an input COULD BE in braille, if:
        - len(words) == 1,
        - len(characters) % 6 == 0
    - but also, that..
        - the only characters in the input are periods and O's.
    from this we can determine that the user's input is in braille and not english.

    HOWEVER!! someone might ask: "what if a user meant to say '.O.....O.O..' as an english sentence?"
        - ...said nobody ever. since launching the application does not require the user to declare whether the input is braille or english,
        an assumption has to be made that in input of the above sort is in braille and not english.

3. english -> braille ---------------------------------------------------------
    have a hard-coded dictionary with keys=character and values=brailleCounterpart.
    have to be wary of: capital letters, and numbers, as we have to print out the ____follows character first.
        
4. braille -> english ---------------------------------------------------------

    have a hard-coded dictionary with keys=brailleCharacter and values=englishCharacter

    have to be careful of the _____follows symbols.

    if we get a "number follows" character, we have to access a seperate dictionary with keys=brailleCharacter values=englishCharacter, as 
        the braille symbols for numbers and the first ten letters are the same, and we cannot have duplicate key values.

    if we get a capital follows...
        do not print, and remember that the next character is a capital character.

"""

def eng_to_braille(sentence: str) -> str:
    """
    Outputs a braille translation of the user's input.

    :param sentence: the input english sentence.
    :type sentence: str

    :return: the braille translation.
    :rtype: str
    """
    BRAILLE_DICT = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
        '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
        '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', ';': '..O.O.',
        '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.',
        ' ': '......'
    }
    CAPITAL_FOLLOWS = ".....O"
    NUMBER_FOLLOWS = ".O.OOO"
    out = ""
    index = 0
    while index < len(sentence):
        char = sentence[index]
        
        if char.isnumeric():
            """
            numeric case

            if there is a sequence of numbers, loop through the next characters until we hit a non-number,
            ONLY attaching the NUMBER_FOLLOWS before the sequence instead of before every number.
                ex. 321 to braille is ".O.OOO + 321", not ".O.OOO + 3 + .O.OOO + 2 + .O.OOO + 1".
            """
            out += NUMBER_FOLLOWS

            while index < len(sentence):
                num = sentence[index]
                if not num.isnumeric():
                    break
                out += BRAILLE_DICT[num]
                index += 1
            # for j in range(index, len(sentence)):
            #     num = sentence[j]
            #     if not num.isnumeric():
            #         break
            #     out += BRAILLE_DICT[num]
            #     index += 1
        else:
            """
            letter case.

            if it is uppercase, add the CAPITAL_FOLLOWS symbol to the output. 
            otherwise, treat it as a lowercase letter/space.
            """
            if char.isupper():
                out += CAPITAL_FOLLOWS
            out += BRAILLE_DICT[char.lower()]
            index += 1
    return out


def braille_to_eng(sentence: str) -> str:
    """
    Outputs an english translation of the user's input.

    :param sentence: the input braille sentence.
    :type sentence: str

    :return: the english translation.
    :rtype: str
    """
    ENG_DICT = {
        'O.....': 'a', 'O.O...': 'b', 'OO....': 'c',  'OO.O..': 'd',  'O..O..': 'e',
        'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h',  '.OO...': 'i',  '.OOO..': 'j',
        'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm',  'OO.OO.': 'n',  'O..OO.': 'o',
        'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r',  '.OO.O.': 's',  '.OOOO.': 't',
        'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w',  'OO..OO': 'x',  'OO.OOO': 'y', 'O..OOO': 'z',
        '......': ' '
    }
    NUMS_DICT = {
        'O.....': '1',  'O.O...': '2', 'OO....': '3',  'OO.O..': '4', 'O..O..': '5',
        'OOO...': '6',  'OOOO..': '7', 'O.OO..': '8',  '.OO...': '9', '.OOO..': '0',
    }
    CAPITAL_FOLLOWS = ".....O"
    NUMBER_FOLLOWS = ".O.OOO"

    print_capital, print_number = False, False
    out = ""
    index = 0
    
    while index < len(sentence):
        braille_char = sentence[index:index+6]

        if braille_char == CAPITAL_FOLLOWS:
            # do not print, and just remember that the next character is a capital/decimal character.
            print_capital = True
            index += 6
        elif braille_char == NUMBER_FOLLOWS:
            # do not print, and just remember that the next character is a capital/decimal character.
            print_number = True
            index += 6
        elif print_capital:
            # make this character an uppercase letter
            out += ENG_DICT[braille_char].upper()
            print_capital = False
            index += 6
        elif print_number:
            """
            we don't know how many numbers follow the "NUMBER_FOLLOWS" symbol.
            so, loop through the next characters until we hit a non-number.
            """
            print_number = False
            while index < len(sentence):
                new_braille_char = sentence[index:index+6]
                if new_braille_char not in NUMS_DICT.keys():
                    break
                out += NUMS_DICT[new_braille_char]
                index += 6
        else:
            # should just be a regular lower-case letter/space.
            out += ENG_DICT[braille_char]
            index += 6
    return out


def is_braille(words: list[str]) -> bool:
    """
    Determines if the user input  is in braille or english.

    :param words: the system arguments passed by the user. ie: for the user launching the app with "python3 translator.py hello world", words=['hello',
    'world'] 
    :type words: list[str]

    :return: returns true if len(characters) % 6 == 0, len(words) == 1, and every character in the list is either a "." or "O".
    :rtype: bool
    """
    if len(words) > 1 or len(words[0]) % 6 != 0:
        return False

    word = words[0]
    for char in word:
        if char != "." and char != "O":
            return False
    return True


if __name__ == "__main__":
    words: list[str] = sys.argv[1:]
    sentence: str = ' '.join(str(word) for word in words)

    if is_braille(words):
        res = braille_to_eng(sentence)
    else:
        res = eng_to_braille(sentence)
    print(res)



