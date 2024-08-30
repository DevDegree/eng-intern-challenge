import sys

char_to_braille = {
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
} # as per intructions no need to focus on symbols and decimals

braille_to_char = {val: key for key, val in char_to_braille.items()}

instructions_to_braille = {
    '[C]': '.....O',
    '[N]': '.O.OOO'
}
braille_to_instructions = {val: key for key, val in instructions_to_braille.items()}

num_to_braille = {
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

braille_to_num = {val: key for key, val in num_to_braille.items()}

def sentence_to_braille(sentence, char_mapping=char_to_braille, num_map=num_to_braille, instruct_map=instructions_to_braille):
    output = ''
    numeric = False
    for char in sentence:
        if char.isupper(): # if it is upper then is cannot be a number
            output += instruct_map['[C]']
            output += char_mapping[char.lower()]
        elif char.isnumeric() and not numeric: #first numeric character in the sequence after a space
            output += instruct_map['[N]']
            numeric=True
            output += num_map[char]
        elif char.isnumeric() and numeric:
            #numeric character in a sequence of existing numeric values 
            # (having numeric the numeric condition is redunant since it was checked in previous condition however I add here for the sake of comprehension)
            output += num_map[char]
        elif char == ' ':
            numeric=False # the following characters may no longer numeric
            output += char_mapping[char]
        elif char.isalpha(): # just a-z (not captilizer)
            output += char_mapping[char]

    return output

    




def braille_to_sentece(braille, char_map=braille_to_char, num_map=braille_to_num, instruct_map=braille_to_instructions):
    pass

def is_braille(argument):
    '''
    function to figure out if the argument given is in the english language or Braille
    input char
    return bool
    '''
    chars= set()


    for char in argument:
        chars.add(char)
    
    return len(chars) == 2 and '.' in chars and 'O' in chars #make sure the only argument has two input



argument = ""
for i in range(1, len(sys.argv)):
    argument += sys.argv[i]
    argument += " "
argument = argument[:-1]

if is_braille(argument): #should be translated to English
    print("input is braille")
else: #should be translated to Braille
    print(sentence_to_braille(argument))






