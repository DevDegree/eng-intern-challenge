import sys

d = {
    'A': 'O.....',
    'B': 'O.O...',
    'C': 'OO....',
    'D': 'OO.O..',
    'E': 'O..O..',
    'F': 'OOO...',
    'G': 'OOOO..',
    'H': 'O.OO..',
    'I': '.OO...',
    'J': '.OOO..',
    'K': 'O...O.',
    'L': 'O.O.O.',
    'M': 'OO..O.',
    'N': 'OO.OO.',
    'O': 'O..OO.',
    'P': 'OOO.O.',
    'Q': 'OOOOO.',
    'R': 'O.OOO.',
    'S': '.OO.O.',
    'T': '.OOOO.',
    'U': 'O...OO',
    'V': 'O.O.OO',
    'W': '.OOO.O',
    'X': 'OO..OO',
    'Y': 'OO.OOO',
    'Z': 'O..OOO',
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
    ' ': '......',
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': 'O..OO.',
    '>': '.OO..O',
    '(': '.O.OO.',
    ')': 'O.O..O',
}

nums_d = {
    '.OOO..': '0',
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
}

def translate(message):
    output = ''
    if '.' not in message:
        # It's english
        inNumber = False
        for letter in message:
            if letter == ' ':
                # Flags the end of a number
                inNumber = False
            elif letter.isalpha() and letter.isupper():
                # It's a capital letter
                output += '.....O'
            elif letter.isdigit() and not inNumber:
                output += ".O.OOO"
                inNumber = True
            output += d[letter.upper()]
    else:
        # It's braille
        keys = list(d.keys())
        values = list(d.values())
        
        #split the message into sequences of 6 characters
        sequences = [message[i:i+6] for i in range(0, len(message), 6)]

        capitalizeNext = False
        inNumber = False

        for sequence in sequences:
            if sequence == '.....O':
                # The next letter is a capital letter
                capitalizeNext = True
            elif sequence == '.O.OOO':
                # Start of a number
                inNumber = True
            elif sequence == '......':
                output += ' '
                # End of a number
                inNumber = False
            elif inNumber and sequence in nums_d:
                output += nums_d[sequence]
            elif not inNumber and sequence in values:
                if keys[values.index(sequence)].isalpha():
                    # It's a letter
                    if capitalizeNext:
                        # It should be capitalized
                        output += keys[values.index(sequence)]
                        capitalizeNext = False
                    else:
                        output += keys[values.index(sequence)].lower()
                else:
                    # It's not a letter
                    output += keys[values.index(sequence)]
    return output

if __name__ == '__main__':
    input = ' '.join(sys.argv[1:]) # grab the command line arguments and join them into a single string
    translated = translate(input)
    print(translated)