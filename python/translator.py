import sys

LETTER_TO_BRAILLE_MOD = {'a': 'O.....','b': 'O.O...','c': 'OO....','d': 'OO.O..','e': 'O..O..', 'f': 'OOO...','g': 'OOOO..','h': 'O.OO..', 
                         'i': '.OO...','j': '.OOO..','k': 'O...O.','l': 'O.O.O.', 'm': 'OO..O.','n': 'OO.OO.','o': 'O..OO.', 'p': 'OOO.O.', 
                         'q': 'OOOOO.','r': 'O.OOO.','s': '.OO.O.','t': '.OOOO.','u': 'O...OO','v': 'O.O.OO','w': '.OOO.O','x': 'OO..OO', 
                         'y': 'OO.OOO','z': 'O..OOO'}

NUMBER_TO_BRAILLE_MOD = {'1': 'O.....', '2': 'O.O...','3': 'OO....','4': 'OO.O..','5': 'O..O..','6': 'OOO...','7': 'OOOO..','8': 'O.OO..', '9': '.OO...','0': '.OOO..', }

WHITESPACE_TO_BRAILLE_MOD = {' ': '......'}

BRAILLE_TO_LETTER_MOD = {braille: i for i, braille in LETTER_TO_BRAILLE_MOD.items()}
BRAILLE_TO_NUMBER_MOD = {braille: n for n, braille in NUMBER_TO_BRAILLE_MOD.items()}
BRAILLE_TO_WHITESPACE_MOD = {braille: ws for ws, braille in WHITESPACE_TO_BRAILLE_MOD.items()}

CAP_MARK_MOD = '.....O'
NUM_MARK_MOD = '.O.OOO'

def verify_braille(input_braille: str) -> bool:
    
    if len(input_braille) % 6 != 0:
        return False

    start, end = 0, 6
    while end <= len(input_braille):
        braille_chunk = input_braille[start:end]

        if braille_chunk not in BRAILLE_TO_LETTER_MOD and braille_chunk not in BRAILLE_TO_NUMBER_MOD and braille_chunk not in BRAILLE_TO_WHITESPACE_MOD and braille_chunk != CAP_MARK_MOD and braille_chunk != NUM_MARK_MOD:
            return False

        start = end
        end += 6

    return True

def verify_text(input_text: str) -> bool:
    for x in input_text.lower():
        if x not in LETTER_TO_BRAILLE_MOD and x not in NUMBER_TO_BRAILLE_MOD and x not in WHITESPACE_TO_BRAILLE_MOD:
            return False

    return True

def text_to_braille(input_text: str) -> str:
    output_braille = ''
    is_number_active = False

    for x in input_text:
        if x.lower() in LETTER_TO_BRAILLE_MOD:
            if x.isupper():
                output_braille += CAP_MARK_MOD
            output_braille += LETTER_TO_BRAILLE_MOD[x.lower()]
        elif x in NUMBER_TO_BRAILLE_MOD:
            if not is_number_active:
                is_number_active = True
                output_braille += NUM_MARK_MOD
            output_braille += NUMBER_TO_BRAILLE_MOD[x]
        elif x in WHITESPACE_TO_BRAILLE_MOD:
            output_braille += WHITESPACE_TO_BRAILLE_MOD[x]
            is_number_active = False

    return output_braille

def braille_to_text(input_braille: str) -> str:
    output_text = ''
    capitalize_flag = False
    number_flag = False

    start, end = 0, 6
    while end <= len(input_braille):
        current_braille = input_braille[start:end]

        if current_braille == CAP_MARK_MOD:
            capitalize_flag = True
        elif current_braille == NUM_MARK_MOD:
            number_flag = True
        elif current_braille in BRAILLE_TO_LETTER_MOD:
            if capitalize_flag:
                output_text += BRAILLE_TO_LETTER_MOD[current_braille].upper()
                capitalize_flag = False
            elif number_flag:
                output_text += BRAILLE_TO_NUMBER_MOD[current_braille]
            else:
                output_text += BRAILLE_TO_LETTER_MOD[current_braille]
        elif current_braille in BRAILLE_TO_WHITESPACE_MOD:
            output_text += BRAILLE_TO_WHITESPACE_MOD[current_braille]
            number_flag = False

        start = end
        end += 6

    return output_text

def main():
    if len(sys.argv) < 2:
        exit('Usage: python translator.py {YOUR STRING HERE}')

    user_input = " ".join(sys.argv[1:])

    if verify_text(user_input):
        print(text_to_braille(user_input))
    elif verify_braille(user_input):
        print(braille_to_text(user_input))

if __name__ == '__main__':
    main()
