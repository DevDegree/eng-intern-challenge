import sys 

ENGLISH_TO_BRAILLE_DICT = {
  'A': "O.....",
  'B': "O.O...",
  'C': "OO....",
  'D': "OO.O..",
  'E': "O..O..",
  'F': "OOO...",
  'G': "OOOO..",
  'H': "O.OO..",
  'I': ".OO...",
  'J': ".OOO..",
  'K': "O...O.",
  'L': "O.O.O.",
  'M': "OO..O.",
  'N': "OO.OO.",
  'O': "O..OO.",
  'P': "OOO.O.",
  'Q': "OOOOO.",
  'R': "O.OOO.",
  'S': ".OO.O.",
  'T': ".OOOO.",
  'U': "O...OO",
  'V': "O.O.OO",
  'W': ".OOO.O",
  'X': "OO..OO",
  'Y': "OO.OOO",
  'Z': "O..OOO",
  ' ': "......",
}

NUMBERS_TO_BRAILLE_DICT = {
  '0': ".OOO..",
  '1': "O.....",
  '2': "O.O...",
  '3': "OO....",
  '4': "OO.O..",
  '5': "O..O..",
  '6': "OOO...",
  '7': "OOOO..",
  '8': "O.OO..",
  '9': ".OO...",
}

DECIMALS_TO_BRAILLE_DICT = {
  '.': "..OO.O",
  ',': "..O...",
  '?': "..O.OO",
  '!': "..OOO.",
  ':': "..OO..",
  ';': "..O.O.",
  '-': "....OO",
  '/': ".O..O.",
  '<': ".O.O.O",
  '>': "O..OO.",
  '(': "O.O..O",
  ')': ".O.OO.",
}

BRAILLE_TO_ENGLISH_DICT = {v: k for k, v in ENGLISH_TO_BRAILLE_DICT.items()}
BRAILLE_TO_DECIMALS_DICT = {v: k for k, v in DECIMALS_TO_BRAILLE_DICT.items()}
BRAILLE_TO_NUMBERS_DICT = {v: k for k, v in NUMBERS_TO_BRAILLE_DICT.items()}

SPACE_SYMBOL = "......"
CAPITAL_SYMBOL = '.....O'
NUMBER_SYMBOL = '.O.OOO'
DECIMAL_SYMBOL = '.O...O'

def main():
  input_text = " ".join(sys.argv[1:])

  if is_braille(input_text):
    print(braille_to_english(input_text))
  else:
    print(english_to_braille(input_text))


def is_braille(string_input):
  str_len = len(string_input)

  if (str_len % 6 != 0):
    return False

  # Check to see if there are any non "O" and "." characters
  for i in range(str_len):
    if string_input[i] not in ["O", "."]:
      return False
  
  return True


def english_to_braille(string_input):
  result = []
  digit_mode = False
  
  for character in string_input:
    if character.isdigit():
      if not digit_mode:
        digit_mode = True
        result.append(NUMBER_SYMBOL)
      
      result.append(NUMBERS_TO_BRAILLE_DICT[character])

    else:
      if character.isupper():
        result.append(CAPITAL_SYMBOL)
      
      if digit_mode:
        digit_mode = False
      
      result.append(ENGLISH_TO_BRAILLE_DICT[character.upper()])
    
  return "".join(result)


def braille_to_english(string_input):
  result = []
  braille_text_chunks = [string_input[i:i+6] for i in range(0, len(string_input), 6)]

  capital = False
  digit_mode = False
  decimal_mode = False

  for chunk in braille_text_chunks:
    if chunk == CAPITAL_SYMBOL:
      capital = True

    elif chunk == NUMBER_SYMBOL:
      digit_mode = True

    elif chunk == DECIMAL_SYMBOL:
      decimal_mode = True

    elif chunk == SPACE_SYMBOL:
      digit_mode = False
      decimal_mode = False
      result.append(" ")

    else:
      if capital:
        result.append(BRAILLE_TO_ENGLISH_DICT[chunk].upper())
        capital = False
      
      elif digit_mode:
        result.append(BRAILLE_TO_NUMBERS_DICT[chunk])

      elif decimal_mode:
        result.append(BRAILLE_TO_DECIMALS_DICT[chunk])
      
      else:
        result.append(BRAILLE_TO_ENGLISH_DICT[chunk].lower())
    
  
  return "".join(result)

  
if __name__ == "__main__":
  main()