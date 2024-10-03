import sys

# english characters to braille using O and . 
braille_chars = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 
    'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 
    'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO', '.': '..OO.O', 
    ',': '..O...', '?': '..O.OO', '!': '..OOO.', 
    ':': '..OO..', ';': '..O.O.', '-': '....OO', 
    '/': '.O..O.', '(': 'O.O..O', ')': '.O.OO.', 
    ' ': '......'
}

# reversing braille to english dictionary
reverse_braille_chars = {value: key for key, value in braille_chars.items()}

# english numbers to braille using O and . 
braille_nums = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', 
    '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', 
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    '0': '.OOO..'
}

# indicators
cap = '.....O'
num = '.O.OOO'
dec = '.O...O'

# reversing braille to english dictionary
reverse_braille_nums = {value: key for key, value in braille_nums.items()}

# convert english to braille
def eng_to_braille(input):

    output = ''
    is_num = False

    for char in input:
        # check if char is a capital letter to add indicator and make sure char is in lowercase when added to output
        if char.isupper():
            output += cap + braille_chars[char.lower()]
        # check if char is a number to add indicator
        elif char.isdigit() and not is_num:
            output += num + braille_nums[char]
            is_num = True
        elif char.isdigit() and is_num:
            output += braille_nums[char]
        # check if char is a decimal to add indicator
        elif char == '.':
            output += dec + braille_chars[char]
        # check if char is a space to set indicator as false for number 
        elif char == ' ':
            output += braille_chars[' ']
            is_num = False
        else:
            output += braille_chars[char]
    return output

# convert braille to english
def braille_to_eng(input):

    output = ''
    is_num = False
    is_cap = False

    for i in range(0,len(input), 6):
        char = input[i:i+6]
        if char == '.....O' and not is_cap:
            is_cap = True
        elif char in reverse_braille_chars and is_cap:
            output += reverse_braille_chars[char].upper()
            is_cap = False
        elif char == '.O.OOO' and not is_num:
            is_num = True
        elif char in reverse_braille_nums and is_num:
            output += reverse_braille_nums[char]
        elif char == '......':
            output += reverse_braille_chars[char]
            is_num = False
        elif char == '..OO.O':
            pass
        else:
            output += reverse_braille_chars[char]
    return output

# checking if input string is english or braille
def is_braille(input):

    # checking if the length of input is a multiple of 6
    if len(input) % 6 != 0:
        return False

    #checking if all characters in input is either O or .
    for char in input:
        if char not in "O.":
            return False

    return True


def main():
    # checking if valid number of arguments
    if len(sys.argv) <= 1:
        print("invalid number of arguments")
        return

    input = ' '.join(sys.argv[1:])

    # handling if input is braille or eng
    if is_braille(input):
        print(braille_to_eng(input))
    else:
        print(eng_to_braille(input))

if __name__ == "__main__":
    main()
