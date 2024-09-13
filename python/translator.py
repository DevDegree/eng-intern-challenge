# Description: This script will take a message and convert it to braille from plaintext or vice versa.
#               Supports A-Z, a-z 0-9 (not mixed with alphabetical chars), and spaces

# Braille mapping. LUT is the most efficient runtime (O(1)) for this problem.
BRAILLE_TO_CHAR = {
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
    '.....O': 'CAPITAL',  # special chars, "follows"
    '.O.OOO': 'NUMBER',  # map to A->J respectively
    '......': ' ',  # ' '
    # not required
    # '.O...O': 'DECIMAL',
    # '.OO..O': '>',
    # 'O..OO.': '<',  # collides
    # '..O...': ',',
    # '..O.OO': '?',
    # '..OOO.': '!',
    # '..OO.O': '.',
    # '..OO..': ':',
    # '..O.O.': ';',
    # '....OO': '-',
    # '.O..O.': '/',
    # 'O.O..O': '(',
    # '.O.OO.': ')'
}
CHAR_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_CHAR.items()}
BRAILLE_LEN = len(next(iter(BRAILLE_TO_CHAR.keys())))


# Name:         chunks
# Purpose:      Yield chunks of n size from l
# Parameters:   l - a list
#               n - an integer
# Returns:      a generator object of n number of striped chunks from l
def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]


# Name:         decode
# Purpose:      Decodes a message from braille to plaintext
# Parameters:   i - a string containing the braille message
# Returns:      a string containing the decoded message
def decode(i: str):
    decoded_msg = str()
    chars = chunks(i, BRAILLE_LEN)
    # flags for capital chars/number words
    isCapital = False
    isNumber = False
    for c in chars:
        decoded_c = BRAILLE_TO_CHAR[c]
        if decoded_c == 'CAPITAL':
            isCapital = True
            continue
        if decoded_c == 'NUMBER':
            isNumber = True
            continue
        # if decoded_c == 'DECIMAL':
        #     continue

        if isCapital:
            decoded_c = decoded_c.upper()
            isCapital = False
        if isNumber:  # iterate thru chars until space is found
            isNumber = False
            while BRAILLE_TO_CHAR[c] != ' ':
                decoded_c = BRAILLE_TO_CHAR[c]
                # map a->j to 1-0
                if decoded_c == 'j':
                    decoded_c = '0'
                else:
                    decoded_c = str(ord(decoded_c) - ord('a') + 1)
                decoded_msg += decoded_c
                c = next(chars)
            if BRAILLE_TO_CHAR[c] == ' ':
                decoded_msg += ' '
                continue
        decoded_msg += decoded_c
    return decoded_msg


# Name:         encode
# Purpose:      Encodes a message from plaintext to braille
# Parameters:   i - a string containing the plaintext message
# Returns:      a string containing the encoded message
def encode(i: str):
    encoded_msg = str()
    # break the input into words
    words = i.split(' ')
    for idx, word in enumerate(words):
        if word.isdigit():  # number case
            encoded_msg += CHAR_TO_BRAILLE['NUMBER']
            for c in word:
                if c == '0':
                    c = 'j'
                else:
                    c = chr(ord('a') + int(c) - 1)
                encoded_msg += CHAR_TO_BRAILLE[c]
            encoded_msg += CHAR_TO_BRAILLE[' ']
            continue
        for c in word:
            if c.isupper():  # uppercase case
                encoded_msg += CHAR_TO_BRAILLE['CAPITAL']
                c = c.lower()
            encoded_msg += CHAR_TO_BRAILLE[c]
        if idx < len(words) - 1:
            encoded_msg += CHAR_TO_BRAILLE[' '] # space between words except last word
    return encoded_msg


if __name__ == '__main__':
    import sys

    # parse input from first arg and store to msg
    if len(sys.argv) < 2:
        print('Please provide a message to convert to/from braille into plaintext. Usage: python translator.py <msg>')
        exit(1)
    if len(sys.argv) > 2:
        msg: str = ' '.join(sys.argv[1:])
    else:
        msg: str = sys.argv[1]
    # Check if the message contains only O and/or .
    if not all(c in 'O.' for c in msg):
        # message is a plaintext message
        print(encode(msg))
    else:
        # message is a braille message
        print(decode(msg))
