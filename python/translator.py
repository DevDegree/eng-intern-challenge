# Hello, my name is Kush Patel.

# For my solution, I tried to keep it simple, considering only the cases
# mentioned and limited error checking by implied assumption that user
# inputs would be valid.

# In the case I have misinterpreted the instructions, I would add further
# error checking in function detect_and_translate rather than a blanket
# try-except block.


import sys

alp_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
}

braille_to_alp = {y: x for x, y in alp_to_braille.items()}

num_to_braille = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.O.OOO'
}
braille_to_num = {y: x for x, y in num_to_braille.items()}

cmds = {'capital': '.....O', 'number': '.O.OOO'}


def braille_to_eng(s: str):

    i = 0  # tracks how much of string is converted
    rtn = ''  # variable to return
    nums = False  # tracks if converting to numbers or not

    while i < len(s):
        curr = s[i:i + 6]

        if curr == cmds['capital']:
            rtn += braille_to_alp[s[i + 6: i + 12]].upper()
            i += 12  # iterate over two braille character as one was a command

        elif curr == cmds['number']:
            rtn += braille_to_num[s[i + 6: i + 12]]
            nums = True  # now read inputs as numbers not letters
            i += 12  # iterate over two braille character as one was a command

        else:

            if braille_to_alp[curr] == ' ':
                rtn += braille_to_alp[curr]
                nums = False  # translate from alphabet again

            elif nums:
                rtn += braille_to_num[curr]

            else:
                rtn += braille_to_alp[curr]

            i += 6  # iterate to next braille character

    return rtn


def eng_to_braille(s: str):

    rtn = ''  # variable to return
    nums = False  # tracks if converting numbers or not

    for char in s:

        if char.isnumeric():

            if not nums:
                rtn += cmds['number'] + num_to_braille[char]
                nums = True

            else:
                rtn += num_to_braille[char]

        elif char.isspace():
            rtn += alp_to_braille[' ']
            nums = False

        else:
            if char.isupper():
                rtn += cmds['capital'] + alp_to_braille[char.lower()]

            else:
                rtn += alp_to_braille[char]

    return rtn


def detect_and_translate(text: str):

    # blanket try-except so program does not crash for any unconsidered inputs
    # left unconsidered inputs based on assumptions of the challenge
    try:
        # determine if text is in braille and translate
        if all(char in 'O.' for char in text) and len(text) % 6 == 0:
            return braille_to_eng(text)

        else:  # text is not in braille and translate
            return eng_to_braille(text)

    except Exception as e:
        return ''


if __name__ == '__main__':

    # get user input from terminal
    user_input = ' '.join(sys.argv[1:])
    # print translation
    print(detect_and_translate(user_input))

