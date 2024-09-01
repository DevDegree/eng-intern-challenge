import sys

# Note: > and o have the same braille code, and there is no online documentation about how this is dealt with. Thus, > and < were removed from the character deck
BRAILLE_ALPHABET = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j':'.OOO..', 'k': 'O...O.',
    'l':'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.',
    'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O',
    'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO', '.': '..OO.O', ',':'..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', 
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '(': 'O.O..O', ')':'.O.OO.', ' ': '......'
}

ENGLISH_ALPHABET = {v: k for k,v in BRAILLE_ALPHABET.items()}

BRAILLE_NUMS = {
    1: 'O.....', 2: 'O.O...', 3: 'OO....', 4: 'OO.O..', 5: 'O..O..',
    6: 'OOO...', 7: 'OOOO..', 8: 'O.OO...', 9: '.OO...', 0: '.OOO..'
}

ENGLISH_NUMS = {v: k for k,v in BRAILLE_NUMS.items()}

BRAILLE_COMMANDS = {
    'capital': '.....O', 'decimal': '.O...O', 'number': '.O.OOO'
}

ENGLISH_COMMANDS = {v: k for k,v in BRAILLE_COMMANDS.items()}


def isBraille(input):
    isBraille = False
    if len(input) % 6 == 0:
        for x in input:
            if x != 'O' and x != '.':
                # end early if one character found that isn't the right composition for braille
                return False
        isBraille = True
    return isBraille


def convertToEnglish(braille) :
    result = ""
    start = 0
    end = 6

    while end <= len(braille):
        # substring of 6 characters representing 1 braille character
        letter = braille[start:end]

        # Assume input is command, if not command then assume letter unless not found, for efficiency of search
        if letter in ENGLISH_COMMANDS:
            command = ENGLISH_COMMANDS[letter]

            start += 6
            end += 6
            letter = braille[start:end]
            if command == 'capital': 
                result += ENGLISH_ALPHABET[letter].upper()
            elif command == 'decimal':
                result += '.'
            elif command == 'number':
                # number requirements specify continue with number command until a space is reached
                while letter != '......' and end <= len(braille):
                    result += str(ENGLISH_NUMS[letter])
                    start += 6
                    end += 6
                    letter = braille[start:end]
        
        elif letter in ENGLISH_ALPHABET:
            result += ENGLISH_ALPHABET[letter]

        start += 6
        end += 6

    return result


def convertToBraille(english) :
    result = ""
    pos = 0

    while pos < len(english):
        letter = english[pos]

        # add capital braille letter to result
        if letter.isupper():
            result += BRAILLE_COMMANDS['capital'] + BRAILLE_ALPHABET[letter.lower()]

        # add number braille letter to result
        elif letter.isnumeric():
            result += BRAILLE_COMMANDS['number'] + BRAILLE_NUMS[int(letter)]
            pos += 1
            letter = english[pos]
            while letter != ' ' and pos < len(english):
                result += BRAILLE_NUMS[int(letter)]
                pos +=1
                letter = english[pos]
            if letter == ' ':
                result += BRAILLE_ALPHABET[' ']

        else:
            result += BRAILLE_ALPHABET[letter]

        pos += 1

    return result
    
def main():
    if len(sys.argv) < 2:
        print("Please provide an input string to be translated.")
        sys.exit(1)

    input_text = ' '.join(sys.argv[1:])
    
    if isBraille(input_text):
        print(convertToEnglish(input_text))
    else:
        print(convertToBraille(input_text))


if __name__ == '__main__':
    main()
