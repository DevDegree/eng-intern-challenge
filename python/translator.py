import sys

number_prefix = '.O.OOO'
capital_prefix = '.....O'
braille_dict = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
        'z': 'O..OOO', # letters a-z
        
        ' ': '......', # space symbol

        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
        '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..' # numbers 0-9
    }

# reverses dictionary and handles duplicate values with arrays
def reverse_dict(original_dict):
    reversed_dict = {}
    
    for key, value in original_dict.items():
        if value not in reversed_dict:
            reversed_dict[value] = [key]  # Initialize with a list
        else:
            reversed_dict[value].append(key)  # Append to the existing list

    return reversed_dict

def break_into_chunks(text):
        return [text[i:i+6] for i in range(0, len(text), 6)]

def is_braille(text):

    braille_set = set(braille_dict.values())
    chunks = break_into_chunks(text)

    for chunk in chunks:
        if chunk not in braille_set and chunk != number_prefix and chunk != capital_prefix:
            return False
        
    return True

def text_to_braille(text):
    
    result = []
    is_number = False

    for i, char in enumerate(text):
        # handle number
        if char.isdigit():
            if not is_number:
                result.append(number_prefix)
                is_number = True
            result.append(braille_dict[char])
        else:
            if is_number and char != ' ':
                result.append('......')  # Add space
            is_number = False
            
            # handle uppercase
            if char.isupper():
                result.append(capital_prefix)
                result.append(braille_dict[char.lower()])
            
            # handle lowercase
            else:
                result.append(braille_dict.get(char.lower(), char))

    return ''.join(result)


def braille_to_text(braille):
    brail_to_text_dict = reverse_dict(braille_dict)

    result = []
    is_number = False
    is_capital = False

    number_index = 1
    letter_index = 0

    chunks = break_into_chunks(braille)

    for chunk in chunks:

        # handle numbers
        if chunk == number_prefix:
            is_number = True
            continue 
        if is_number:
            if brail_to_text_dict[chunk][number_index].isdigit():
                result.append(brail_to_text_dict[chunk][number_index])
                continue
            else:
                is_number = False

        # handle capitals
        if chunk == capital_prefix:
            is_capital = True
            continue
        if is_capital:  
            result.append(brail_to_text_dict[chunk][letter_index].upper())
            is_capital = False
            continue
        
        # handle lowercase
        else:
            result.append(brail_to_text_dict[chunk][letter_index])

    return ''.join(result)

def translator(input_text):
    if is_braille(input_text):
        output_text = braille_to_text(input_text)
        print(output_text)
    else:
        output_text = text_to_braille(input_text)
        print(output_text)




if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please enter a string or braille as an argument")
        sys.exit(1)
    
    input_text = ' '.join(sys.argv[1:])

    translator(input_text)
