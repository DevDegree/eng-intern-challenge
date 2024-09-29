import sys

# Dictionary of English lower case letters to Baille
eng_to_brail_letters = {
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
    'z': 'O..OOO'
}

# Dictionary of English numbers to Baille
eng_to_brail_numbers = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'
}

# Creating dictionaries of Baille to English by swaping key and value from dictionaries of English to Braille
brail_to_eng_letters = {value: key for key, value in eng_to_brail_letters.items()}
brail_to_eng_numbers = {value: key for key, value in eng_to_brail_numbers.items()}

# Special Baille characters
capital_follows = '.....O'
number_follows = '.O.OOO'
space = '......'

# The function to translate English text to Braille
def eng_to_brail(input):
    is_number = False # If True, the next character should be either a number or space.
    output = '' # To store the translated text
    # Iterate over letters of the English text.
    for letter in input:
        # If the next letter is a lower case English alphabet and we don't expect a number,
        # then add its Braille symbol to the translation.
        if letter.islower() and (not is_number):
            output += eng_to_brail_letters[letter]
        # If the next letter is an upper case English alphabet and we don't expect a number,
        # then add a Braille capital follows symbol and its Braille symbol to the translation.
        elif letter.isupper() and (not is_number):
            output += capital_follows
            output += eng_to_brail_letters[letter.lower()]
        # If the next letter is a number and we don't expect a number,
        # then add a Braille number follows symbol,
        # mark that all the following letters should be a number until the next space symbol,
        # and add the Braille symbol of that digit to the translation.
        # If you already expect a number, only add its Braille symbol to the translation.
        elif letter.isdecimal():
            if not is_number:
                is_number = True
                output += number_follows
            output += eng_to_brail_numbers[letter]
        # If the next letter is a space, then add its Braille symbol to the translation,
        # and mark that you don't expect numbers anymore.
        elif letter == ' ':
            is_number = False
            output += space
        # In any other case, the input is invalid.
        else:
            print('Invalid input!')
            quit()
    print(output)
    return output

# The function to translate English text to Braille
def brail_to_eng(input):
    is_number = False # If True, the next character should be either a number or space.
    is_capital = False # If True, the next character should be a capital letter.
    output = '' # To store the translated text
    # If the length of the input is not a multiple of 6, it is invalid.
    if len(input) % 6 != 0:
        print('Invalid input!')
        quit()
    # Iterate over symbols of the Baille text.
    for i in range(0, len(input), 6):
        symbol = input[i:i+6] # The next Baille symbol
        # If the next symbol is a Baille symbol of an English alphabet and we don't expect a number,
        # then add its English alphabet to the translation in the expected upper or lower case format.
        if (not is_number) and (symbol in brail_to_eng_letters):
            if is_capital:
                is_capital = False # After adding one upper case letter, we don't expect upper case anymore.
                output += brail_to_eng_letters[symbol].upper()
            else:
                output += brail_to_eng_letters[symbol]
        # If we expect a number and the next symbol is a Baille symbol of a digit,
        # then add its English digit to the translation.
        elif is_number and (symbol in brail_to_eng_numbers):
            output += brail_to_eng_numbers[symbol]
        # If the next symbol is capital follows and we expect a number,
        # then the input is invalid. Otherwise, we mark that we expect an upper case letter next.
        elif symbol == capital_follows:
            if is_number:
                print('Invalid input!')
                quit()    
            is_capital = True
        # If the next symbol is number follows and we expect an upper case letter,
        # then the input is invalid. Otherwise, we mark that we expect numbers next.
        elif symbol == number_follows:
            if is_capital:
                print('Invalid input!')
                quit()
            is_number = True
        # If the next symbol is space and we expect an upper case letter,
        # then the input is invalid. Otherwise, we mark that we don't expect numbers anymore,
        # and we add a space to the translation.
        elif symbol == space:
            if is_capital:
                print('Invalid input!')
                quit()
            is_number = False
            output += ' '
        # In any other case, the input is invalid.
        else:
            print('Invalid input!')
            quit()
    print(output)
    return output

# The function to decide the text is in English or Braille and traslate correspondingly
def translate(input):
    # Since we don't accept '.' in an English text and all Baille symbols have at least
    # one '.' in it, any text with at least one '.' should be in Baille language.
    if '.' in input:
        brail_to_eng(input)
    else:
        eng_to_brail(input)

if __name__ == '__main__':
    # Join all arguments using space delimiter and call the translate function to translate the input.
    translate(' '.join(sys.argv[1:]))