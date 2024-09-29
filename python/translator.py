import sys
from constants import (
    ENGLISH_TO_BRAILLE_MISC,
    ENGLISH_TO_BRAILLE_LETTERS,
    ENGLISH_TO_BRAILLE_NUMBERS,
    BRAILLE_TO_ENGLISH_MISC,
    BRAILLE_TO_ENGLISH_LETTERS,
    BRAILLE_TO_ENGLISH_NUMBERS,
)

input_sequence = " ".join(sys.argv[1:])

# Determine if the input is Braille
is_input_language_braille = all(char in ['O', '.'] for char in input_sequence)

result = ""

if is_input_language_braille:
    # Translate to English
    i = 0
    while i < len(input_sequence):
        cur_section = input_sequence[i:i+6]
        if cur_section in BRAILLE_TO_ENGLISH_MISC:
            i += 6
            if BRAILLE_TO_ENGLISH_MISC[cur_section] == 'capital_follows':
                cur_section = input_sequence[i:i+6]
                result += BRAILLE_TO_ENGLISH_LETTERS[cur_section].upper()
            else:  # number(s) follow
                while i < len(input_sequence):
                    cur_section = input_sequence[i:i+6]
                    if cur_section == '......':
                        result += ' '
                        break
                    result += BRAILLE_TO_ENGLISH_NUMBERS[cur_section]
                    i += 6
        else:
            result += BRAILLE_TO_ENGLISH_LETTERS[cur_section]
        i += 6
else:
    # Translate to Braille
    i = 0
    while i < len(input_sequence):
        char = input_sequence[i]
        if char.isalpha():
            if char.isupper():
                result += ENGLISH_TO_BRAILLE_MISC['capital_follows'] + ENGLISH_TO_BRAILLE_LETTERS[char.lower()]
            else:
                result += ENGLISH_TO_BRAILLE_LETTERS[char]
        elif char == ' ':
            result += ENGLISH_TO_BRAILLE_LETTERS[char]
        else:  # number follows
            result += ENGLISH_TO_BRAILLE_MISC['number_follows']
            while i < len(input_sequence) and input_sequence[i] != ' ':
                result += ENGLISH_TO_BRAILLE_NUMBERS[input_sequence[i]]
                i += 1
            if i < len(input_sequence) and input_sequence[i] == ' ':
                result += '......'
        i += 1

print(result)
