import sys
from mappings import alphabets, numbers, puncuations, capital_follows, decimal_follows, number_follows

# Olocs = location of 'O's (bumps)
def olocs_to_braille(olocs):
    positions = ['.'] * 6
    for loc in olocs:
        positions[loc - 1] = 'O' # -1 to match indexes
    return ''.join(positions)

def braille_to_olocs(braille):
    return

def english_to_braille(input_string):
    output = ''
    number_mode = False
    # loop and catch case by case
    for char in input_string:
        if char == ' ':
            output += puncuations[' ']
            number_mode = False
        elif char.isdigit():
            if not number_mode:
                output += olocs_to_braille(number_follows)
                number_mode = True
            output += olocs_to_braille(numbers[char])
        else:
            if number_mode:
                number_mode = False
            if char.isupper():
                output += olocs_to_braille(capital_follows)
                char = char.lower()
            output += olocs_to_braille(alphabets[char])
    return output

def braille_to_english(input_string):
    return

def is_braille(input_string):
    input_string_no_spaces = input_string.replace(' ', '')
    # braille should only be in O and .
    for char in input_string_no_spaces:
        if char not in ('O', '.'):
            return False
    # it also should be in multiple of 6s
    if len(input_string_no_spaces) % 6 != 0:
        return False
    return True

def main():
    args = sys.argv[1:]
    if not args: # not accepting false runs
        return
    input_string = ' '.join(args)
    if is_braille(input_string):
        output = braille_to_english(input_string)
    else:
        output = english_to_braille(input_string)
    print(output)

if __name__ == "__main__":
    main()