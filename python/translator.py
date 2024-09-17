import sys
from mappings import alphabets, numbers, puncuations, capital_follows, number_follows

# Olocs = location of 'O's (bumps)
def olocs_to_braille(olocs):
    positions = ['.'] * 6
    if len(olocs) > 0:
        for loc in olocs:
            positions[loc - 1] = 'O' # -1 to match index
    return ''.join(positions)

def braille_to_olocs(braille):
    positions = []
    for i, char in enumerate(braille):
        if char == 'O':
            positions.append(i + 1) # + 1 to add index
    return positions

def english_to_braille(input_string):
    output = ''
    number_mode = False
    # loop and catch case by case
    for char in input_string:
        if char == ' ':
            output += olocs_to_braille(puncuations[' '])
            number_mode = False
        elif char.isdigit():
            if not number_mode:
                output += olocs_to_braille(number_follows)
                number_mode = True
            output += olocs_to_braille(alphabets[numbers[char]])
        # im aware punctuations are not necessary, but still for fun :)
        elif char in {'.', ',', '?', '!', ':', ';', '(', ')', '-', '/', '<', '>'}: # use a set for that very minor time efficiency
            number_mode = False # if it was true, it was still true by accident. turn it off
            output += olocs_to_braille(puncuations[char])
        else:
            number_mode = False # if it was true, it was still true by accident. turn it off
            if char.isupper():
                output += olocs_to_braille(capital_follows)
                char = char.lower()
            output += olocs_to_braille(alphabets[char])
    return output

# just used to find char by olocs
def find_keys_by_value(dict, value):
    for key, val in dict.items():
        if val == value:
            return key
    return None

def braille_to_english(input_string):
    output = ''
    i = 0
    input_length = len(input_string)
    number_mode = False
    capital_mode = False
    prev_tri_bracket = False
    while i < input_length:
        if input_string[i] == ' ': # handling the weird case where braille would be inputed as two separate arguments
            i += 1
            continue
        braille_char = input_string[i:i+6]
        if len(braille_char) < 6: # shouldnt occur since its being caught at is_braille() but just in case
            break
        if braille_char == olocs_to_braille(puncuations[' ']):
            output += ' '
            number_mode = False
        elif braille_char == olocs_to_braille(capital_follows):
            capital_mode = True
        elif braille_char == olocs_to_braille(number_follows):
            number_mode = True
        else:
            if number_mode:
                output += find_keys_by_value(numbers, find_keys_by_value(alphabets, braille_to_olocs(braille_char)))
            else:
                result_punct = find_keys_by_value(puncuations, braille_to_olocs(braille_char))
                # there arent any empty strings or False or 0, so its okay to just use if result_punct
                # assume the closing triangular bracket '>' will only come after a opening one '<'
                # if the bracket was not opened previously, consider it the alphabet 'o'
                if (result_punct and result_punct != '>') or (result_punct and result_punct == '>' and prev_tri_bracket):
                    if (result_punct == '<'):
                        prev_tri_bracket = True
                    if (result_punct == '>'):
                        prev_tri_bracket = False
                    output += result_punct
                else:
                    result_alphabet = find_keys_by_value(alphabets, braille_to_olocs(braille_char))
                    if capital_mode:
                        result_alphabet = result_alphabet.upper()
                        capital_mode = False
                    output += result_alphabet
        i += 6
    return output

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

if __name__ == '__main__':
    main()