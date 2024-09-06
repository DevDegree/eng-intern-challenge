braille_to_english_dict = {
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
    '......': ' '
}


def translate_braille(text):

    # approach is similar to eng_to_braille
    # we 

    result = '' # result value initialized to empty string

    i = 0 # index pointer

    # boolean flags for capital letters and number follows
    next_capital = False
    next_num = False

    while i < len(text):
        char = text[i:i+6] # take in 6 characters that represent a single braille character/flag
        
        # note that the variable 'i' is incremented by 6, since it takes 6
        # '.' and 'O' characters to represent a single braille character/flag

        # process the character/flag
        match char:

            case '.....O': # capital follows
                next_capital = True
                i = i + 6 

            case '.O.OOO': # number follows
                next_num = True
                i = i + 6

            case '......': # space
                if result[-1].isdigit(): # only set next_num flag to false if you encounter a space character
                    next_num = False
                result = result + ' '
                i = i + 6
            
            case _: # default case to handle character input
                # if the next capital flag is raised then add the uppercase letter from the alphabet
                if next_capital:
                    val = braille_to_english_dict[char]
                    result = result + val.upper()
                    next_capital = False

                # process the numbers
                elif next_num:
                    val = (ord(braille_to_english_dict[char])-ord('a') + 1) % 10 # mod 10 to account for j == 0
                    result = result + str(val)
                
                # process all other characters and append them to the result
                else:
                    val = braille_to_english_dict[char]
                    result = result + val
                
                i = i + 6

    return result
