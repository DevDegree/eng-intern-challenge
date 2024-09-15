import sys

# English to Braille Map
eng_alphabet_map = {'A': 'O.....', 'B': 'O.O...', 'C': 'OO....', 'D': 'OO.O..', 
               'E': 'O..O..', 'F': 'OOO...', 'G': 'OOOO..', 'H': 'O.OO..', 
               'I': '.OO...', 'J': '.OOO..', 'K': 'O...O.', 'L': 'O.O.O.', 
               'M': 'OO..O.', 'N': 'OO.OO.', 'O': 'O..OO.', 'P': 'OOO.O.', 
               'Q': 'OOOOO.', 'R': 'O.OOO.', 'S': '.OO.O.', 'T': '.OOOO.', 
               'U': 'O...OO', 'V': 'O.O.OO', 'W': '.OOO.O', 'X': 'OO..OO', 
               'Y': 'OO.OOO', 'Z': 'O..OOO'}

eng_number_map = {'1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
                 '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'}

#eng_symbol_map = {'.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', 
#                  ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', 
#                  '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.', 
#                  ' ': '......'}

# Reverse dictionary key/value pair
def reverse_dict(sample_map):
    reverse_map = {}
    for key, val in sample_map.items():
        reverse_map[val] = key

    return reverse_map

# Braille to English Map
br_alphabet_map = reverse_dict(eng_alphabet_map)
br_number_map = reverse_dict(eng_number_map)
#br_symbol_map = reverse_dict(eng_symbol_map)

# Non-Alphanumeric Braille Cells
space = '......'
capital_follow = '.....O'
number_follow = '.O.OOO'
#decimal_follow = '.O...O'

# If input given is Braille returns True and False otherwise (English)
def type_check(input_statement):
    for char in input_statement:
        if (char != 'O' and char != '.'):
            return False
    
    return True

# Converts from Braille to English
def braille_to_english(input_statement):
    output_statement = ""
    capital_follow_state = False # to check capital letter occurence
    number_follow_state = False # to check first number occurennce
    i = 0
    while i < len(input_statement):
        br_cell = input_statement[i:i + 6] # getting Braille cell
        if br_cell == capital_follow: # changes capital_follow_state for next iteration
            capital_follow_state = True

        elif br_cell == number_follow: # changes number_follow_state for next iteration
            number_follow_state = True

        elif br_cell == space: # changes number_follow_state for next iteration
            output_statement += ' '
            number_follow_state = False

        elif number_follow_state: # adding br_cell as number if number_follow_state
            output_statement += br_number_map[br_cell]

        elif capital_follow_state: # adding br_cell as capital letter if capital_follow_state
            output_statement += br_alphabet_map[br_cell]
            capital_follow_state = False

        else: # br_cell must be lowercase letter
            output_statement += br_alphabet_map[br_cell].lower()

        i += 6

    return output_statement

# Converts from English to Braille
def english_to_braille(input_statement):
    output_statement = ""
    number_follow_state = False # to check first number occurennce
    
    for char in input_statement:
        if char.isalpha(): # char is letter
            # adding capital_follow if letter is uppercase else only char
            if char.isupper(): 
                output_statement += capital_follow + eng_alphabet_map[char]
            else:
                output_statement += eng_alphabet_map[char.upper()]

        elif char.isdigit(): # char is number
            # adding number_follow if first number occurence else only char
            if not number_follow_state: 
                output_statement += number_follow + eng_number_map[char]
                number_follow_state = True
            else:
                output_statement += eng_number_map[char]
        
        else: # char must be space
            output_statement += space
            number_follow_state = False
    
    return output_statement

def main():
    # reading in the input
    input_statement = ' '.join(sys.argv[1:]) # joining arguments with space as string, excluding filename
    statement_type = type_check(input_statement) # True: Braille, False: English
    output_statement = braille_to_english(input_statement) if statement_type else english_to_braille(input_statement)
    print(output_statement)

if __name__ == '__main__':
    main()
