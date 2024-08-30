import sys

braille_chars = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
}

braille_unique = {'capital': '.....O', 'number': '.O.OOO'}

braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

def is_string_braille(string):
  if len(string) % 6 != 0:
    return False

  return all(char == 'O' or char == '.' for char in string)

def braille_to_english(string):
  english_chars = {v: k for k,v in braille_chars.items()}
  english_unique = {v: k for k,v in braille_unique.items()}
  english_numbers = {v: k for k,v in braille_numbers.items()}

  result = ''
  is_upper = False
  is_number = False

  # Loop through the string, processing 6 characters at a time
  for i in range(0, len(string), 6):
    braille_char = string[i: i+6]

    if braille_char in english_unique:
      if english_unique[braille_char] == 'capital':
        is_upper = True
      else:
        is_number = True
      continue
      
    if is_number:
      if english_numbers[braille_char]:
        result += english_numbers[braille_char]
      else:
        # If english_numbers[braille_char] is false, the only explanation is that the character is a space
        result += ' '
        is_number = False
    else:
      letter = english_chars[braille_char]

      if is_upper:
        result += letter.upper()
        is_upper = False
      else: 
        result += letter

  return result

def english_to_braille(string):
  result = ''

  # Determines if there will be a sequence of numbers
  is_number = False

  for char in string:
    if char.isdigit():
      if not is_number:
        is_number = True
        result += braille_unique['number']
      result += braille_numbers[char]
    elif char == ' ':
      is_number = False
      result += braille_chars[' ']
    elif char.isalpha():
      if char == char.upper():
        result += braille_unique['capital'] 
      result += braille_chars[char.lower()]
  
  return result

def main():
  message = ' '.join(sys.argv[1:])
  is_braille_string = is_string_braille(message)

  if is_braille_string:
    print(braille_to_english(message))
  else:
    print(english_to_braille(message))
  
if __name__ == "__main__":
    main()