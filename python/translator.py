import sys

# encode
english_to_braille_dict = {
  #letters
  'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
  'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
  'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
  'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
  'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
  'z': 'O..OOO',
  #others
  '.': '..O...', ',': '..OOO.', '?': '..OO.O', '!': '..O.OO', ':': '.O..OO',
  ';': '.O..O.', '-': '....O.', '/': '..OOOO', '<': '.O.O.O', '>': 'O...O.',
  '(': 'O.O..O', ')': '.O.OO.', ' ' : '......',
  
  'capital follows': '.....O', 
  'decimal follows': 'O..O.O',
  'number follows': '.O.OOO',
}

num_to_braille_dict = {
  '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
  '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

braille_to_english_dict = { v: k for k, v in english_to_braille_dict.items() }
braille_to_num_dict = { v: k for k, v in num_to_braille_dict.items() }


def is_braille_input(message):
  is_good_length = (len(message) % 6 == 0)
  is_valid_string = (set(message) == set(['O', '.']))
  return (is_good_length and is_valid_string)

def convert_braille_to_english(message):
  capital_flag = False
  num_flag = False
  final_message = ''
  
  braille_string = [message[i:i+6] for i in range(0, len(message), 6)]
  
  for braille_char in braille_string:
    if num_follows(braille_char):
      num_flag = True
    elif is_space(braille_char):
      final_message += braille_to_english_dict[braille_char]
      num_flag = False
    elif num_flag:
      final_message += braille_to_num_dict[braille_char]
    elif capital_follows(braille_char):
      capital_flag = True
    elif capital_flag:
      final_message += braille_to_english_dict[braille_char].capitalize()
      capital_flag = False
    else:
      final_message += braille_to_english_dict[braille_char]
  return final_message
  
def convert_english_to_braille(message):
  final_message = ''
  space_flag = True
  
  for char in message:
    if char.isupper():
      final_message += english_to_braille_dict['capital follows']
    elif char.isdigit():
      if space_flag:
        final_message += english_to_braille_dict['number follows']
        space_flag = False
      final_message += num_to_braille_dict[char]
      continue
    elif char == ' ':
      space_flag = True
    final_message += english_to_braille_dict[char.lower()]
  return final_message


def num_follows(braille_char):
  return braille_char == english_to_braille_dict['number follows']

def capital_follows(braille_char):
  return braille_char == english_to_braille_dict['capital follows']

def is_space(braille_char):
  return braille_char == english_to_braille_dict[' ']

if __name__ == '__main__':
  if len(sys.argv) <= 1:
    print("Invalid user input. Please enter either Braille or English sentence.")
  message = ' '.join(sys.argv[1:])
  if is_braille_input(message):
    print(convert_braille_to_english(message))
  else:
    print(convert_english_to_braille(message))
  
    
  

