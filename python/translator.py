import sys

# Criteria
# The input is Braille if and only if:
# 1. The number of unique characters (including spaces) is either 1 or 2
# 2. All characters are either a "." or a "O"
# Otherwise, the input is assumed to be English.

# We first store the input arguments as a concatenated string, in order inspect their content.
input_concatenated = ''.join(sys.argv[1:])
characters = set(input_concatenated)

# Edge case with empty input, in which case an empty line is printed.
if len(input_concatenated) == 0:
    print()
    sys.exit()

# As mentioned above, we inspect the content and apply criteria to determine the direction of translation.
# If the input arguments are braille, we will join the input arguments on "......", and otherwise we will join on " ".
to_braille = True
input = None
if (len(characters) == 2 and '.' in characters and 'O' in characters) or \
    len(characters) == 1 and ('.' in characters or 'O' in characters):
    to_braille = False
    input = '......'.join(sys.argv[1:])
else:
    input = ' '.join(sys.argv[1:])

# Now that the direction of translation has been established, we create the appropriate translation mapping.
# I would place this map in a separate file and import it, but the instructions specify to work in this file.
capitals = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

numbers = {'0':'.OOO..',
            '1':'O.....',
            '2':'O.O...',
            '3':'OO....',
            '4':'OO.O..',
            '5':'O..O..',
            '6':'OOO...',
            '7':'OOOO..',
            '8':'O.OO..',
            '9':'.OO...',}

letters = {'a':'O.....',
            'b':'O.O...',
            'c':'OO....',
            'd':'OO.O..',
            'e':'O..O..',
            'f':'OOO...',
            'g':'OOOO..',
            'h':'O.OO..',
            'i':'.OO...',
            'j':'.OOO..',
            'k':'O...O.',
            'l':'O.O.O.',
            'm':'OO..O.',
            'n':'OO.OO.',
            'o':'O..OO.',
            'p':'OOO.O.',
            'q':'OOOOO.',
            'r':'O.OOO.',
            's':'.OO.O.',
            't':'.OOOO.',
            'u':'O...OO',
            'v':'O.O.OO',
            'w':'.OOO.O',
            'x':'OO..OO',
            'y':'OO.OOO',
            'z':'O..OOO'}

logical = {'capital':'.....O',
            'decimal':'.O...O',
            'number':'.O.OOO'}


# Core translation logic
output = []

# case: English to Braille
if to_braille:

    mode = 'letters' # As we parse the input, we are either in number, decimal, or letters mode. Decimal mode implies number mode.

    for i in range(len(input)):

        c = input[i]

        if c == '.':

            # case: '.' is the last character, and is thus guaranteed to not be decimal.
            if i + 1 >= len(input):
                output.append('..OO.O')

            # case: '.' is not the last character and we are already in number mode but not yet decimal mode.

            elif mode == 'number':
                if input[i+1] in numbers:
                    output.append(logical['decimal'])
                    mode = 'decimal'
                else:
                    output.append('..OO.O')
                    mode = 'letters'

            # case: '.' is not the last character and we are already in decimal mode. Decimal mode must end here as we cannot have two decimal points.

            elif mode == 'decimal':
                mode = 'letters'
                output.append('..OO.O')

            # case: '.' is not the last character and we are still in letters mode
            else:
                if input[i+1] in numbers:
                    output.append(logical['number'])
                    output.append(logical['decimal'])
                    mode = 'decimal'
                else:
                    output.append('..OO.O')     
 
        elif c in letters:
            if mode != 'letters':
                mode = 'letters'
            output.append(letters[c])

        elif c in capitals:
            if mode != 'letters':
                mode = 'letters'
            output.append(logical['capital'])
            output.append(letters[c.lower()])

        elif c == ' ':
            if mode != 'letters':
                mode = 'letters'
            output.append('......')

        elif c in numbers:
            if mode == 'letters':
                mode = 'number'
                output.append(logical['number'])
            output.append(numbers[c])

# case: Braille to English
else:

    # Since we are translating to english instead, we flip the translation dictionaries.
    numbers = {v: k for k, v in numbers.items()}
    letters = {v: k for k, v in letters.items()}
    logical = {v: k for k, v in logical.items()}

    # In the Braille to English direction, there are three possible modes: letters, number, capital
    mode = 'letters'
    i = 0
    while i < len(input):
        token = input[i:i+6]

        if mode == 'letters':
            if token in letters:
                output.append(letters[token])
            elif token == '......':
                output.append(' ')
            elif token in logical:
                mode = logical[token] #this should only change to capital or number because decimal always occurs during number mode

        elif mode == 'number':
            if token == '.O...O':
                output.append('.')
            elif token == '......': #the technical requirements specify that number mode continues until a space is encountered (or, I assume, also the end of the string)
                mode = 'letters'
                output.append(' ')
            else:
                output.append(numbers[token])

        elif mode == 'capital':
            mode = 'letters'
            output.append(letters[token].upper())

        i += 6

# The output is now ready to print.
output = ''.join(output)
print(output)