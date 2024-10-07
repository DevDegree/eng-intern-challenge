import sys

def create_maps():
        char_to_braille_map = {
                'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
                'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
                'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
                'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
                'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
                'z': 'O..OOO', ' ': '......', 'CAPITAL FOLLOWS' : '.....O', 'NUMBER FOLLOWS' : '.O.OOO'
        }

        #Flip key:value pairs
        braille_to_char_map = {value: key for key, value in char_to_braille_map.items()}

        num_to_braille_map = {
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
        '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
        }

        #Flip key:value pairs
        braille_to_num_map = {value: key for key, value in num_to_braille_map.items()}

        return char_to_braille_map, braille_to_char_map, num_to_braille_map, braille_to_num_map

def translate_braille_to_english(braille_str, char_map, num_map):
        translated_str = ''
        capitalize = False
        number_mode = False
        braille_char_length = 6

        for i in range(0, len(braille_str), braille_char_length):
                braille_char = braille_str[i:i+6]

                #Check if number mode is on
                if number_mode:
                        translated_num = num_map[braille_char]
                        translated_str += translated_num
                else:
                        translated_char = char_map[braille_char]

                #Check other modifiers
                if translated_char == 'CAPITAL FOLLOWS':
                        capitalize = True
                        continue
                elif translated_char == 'NUMBER FOLLOWS':
                        number_mode = True
                        continue
                elif translated_char == ' ':
                        number_mode = False
                
                #Check if char needs to be capitalized
                if capitalize:
                        translated_str += translated_char.upper()
                        capitalize = False
                else:
                        translated_str += translated_char

        return translated_str

def translate_english_to_braille(english_str, char_map, num_map):
        translated_str = ''
        number_mode = False

        for char in english_str:
                
                #Check if char is a digit
                if char.isdigit():
                        if number_mode:
                                translated_str += num_map[char]
                        else:
                                number_mode = True
                                translated_str += char_map['NUMBER FOLLOWS'] + num_map[char]

                #Check if char is an upper case letter
                elif char.isupper():
                        translated_str += char_map['CAPITAL FOLLOWS'] + char_map[char.lower()]

                #Check if char is a space
                elif char == ' ':
                        number_mode = False
                        translated_str += char_map[char]
                        
                else:
                        translated_str += char_map[char]

        return translated_str

def is_braille(input_str):
        return all(c in ['O', '.'] for c in input_str)

def main():
        char_to_braille_map, braille_to_char_map, num_to_braille_map, braille_to_num_map = create_maps()
        
        input_str = ' '.join(sys.argv[1:])

        if is_braille(input_str):
                output_str = translate_braille_to_english(input_str, braille_to_char_map, braille_to_num_map)
        else:
                output_str = translate_english_to_braille(input_str, char_to_braille_map, num_to_braille_map)

        print(output_str)

if __name__ == "__main__":
        main()