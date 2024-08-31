import sys

# Function to invert dictionaries for simplicity
def invert_map(map):
  
  # Inverting dictionary using python syntax
  inverted = {v: k for k, v in map.items()}

  return inverted

class Translator:

  # Mapping for English letters to Braille letters
  LETTERS_ENG_TO_BRAILLE = {
    'A': 'O.....', 'B': 'O.O...', 'C': 'OO....', 'D': 'OO.O..', 'E': 'O..O..',
    'F': 'OOO...', 'G': 'OOOO..', 'H': 'O.OO..', 'I': '.OO...', 'J': '.OOO..',
    'K': 'O...O.', 'L': 'O.O.O.', 'M': 'OO..O.', 'N': 'OO.OO.', 'O': 'O..OO.',
    'P': 'OOO.O.', 'Q': 'OOOOO.', 'R': 'O.OOO.', 'S': '.OO.O.', 'T': '.OOOO.',
    'U': 'O...OO', 'V': 'O.O.OO', 'W': '.OOO.O', 'X': 'OO..OO', 'Y': 'OO.OOO',
    'Z': 'O..OOO'
  }

  # Mapping for numbers to letters 
  NUMBERS_TO_LETTERS = {
    '1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E',
    '6': 'F', '7': 'G', '8': 'H', '9': 'I', '0': 'J'
  }

  # Mapping for operations 
  OPERATIONS = {
    'SPACE': '......',
    'CAPITAL': '.....O',
    'NUMBER': '.O.OOO'
  }

  # Reversed mappings
  LETTERS_BRAILLE_TO_ENG = invert_map(LETTERS_ENG_TO_BRAILLE)
  LETTERS_TO_NUMBERS = invert_map(NUMBERS_TO_LETTERS)
  REVERSE_OPERATIONS = invert_map(OPERATIONS)

  def __init__(self, phrase = ""):
    self.phrase = phrase

  # def set_phrase(self, phrase):
  #   self.phrase = phrase


  def is_braille(self):
    ''' Determines whether the phrase is in braille or english '''

    braille_chars = set(["O", '.'])
    contains_only_braille = True

    for char in self.phrase:
      if char not in braille_chars:
        contains_only_braille = False

    # Phrase must be divisible by 6 and contain only 'O and '.
    return len(self.phrase) % 6 == 0 and contains_only_braille
    


  def translate_to_braille(self):
    ''' Function which translates an english phrase into braille'''

    res = ""
    numeric_toggle = False
    for char in self.phrase:
      
      # Check if given character is a-z / A-Z
      if char.isalpha():

        # If char is lowercase, just add its braille conversion to res
        if char.islower():
          res += self.LETTERS_ENG_TO_BRAILLE[char.upper()]
        
        # If char is uppercase, add the CAPITAL braille phrase and its braille conversion of char to res
        elif char.isupper():
          res += self.OPERATIONS['CAPITAL']
          res += self.LETTERS_ENG_TO_BRAILLE[char.upper()]

      # Check if given character is 0-9
      elif char.isnumeric():
        # First number in the sequence, include the number operation character
        if not numeric_toggle:
          numeric_toggle = True
          res += self.OPERATIONS['NUMBER']
        res += self.LETTERS_ENG_TO_BRAILLE[self.NUMBERS_TO_LETTERS[char]]
      
      elif char == " ":
        numeric_toggle = False
        res += self.OPERATIONS['SPACE']

    return res


  def translate_to_english(self):
    ''' Function which translates an braille phrase into english'''

    res = ""
    capital_toggle = False
    number_toggle = False

    # parse the entire string into an array of length 6 braille phrases
    braille_chars = [self.phrase[i: i + 6] for i in range(0, len(self.phrase), 6)]

    for char in braille_chars:
      # handle operational characters
      if char in self.REVERSE_OPERATIONS:
        if self.REVERSE_OPERATIONS[char] == 'SPACE':
          res += " "
          number_toggle = False
        elif self.REVERSE_OPERATIONS[char] == 'CAPITAL':
          capital_toggle = True
        else: 
          number_toggle = True
      
      # handle a-z A-Z cases
      elif char in self.LETTERS_BRAILLE_TO_ENG and not number_toggle:
        if capital_toggle:
          res += self.LETTERS_BRAILLE_TO_ENG[char].upper()
          capital_toggle = False
        else:
          res += self.LETTERS_BRAILLE_TO_ENG[char].lower()
      
      # handle 0-9 cases
      elif self.LETTERS_BRAILLE_TO_ENG[char] in self.LETTERS_TO_NUMBERS and number_toggle:
        res += self.LETTERS_TO_NUMBERS[self.LETTERS_BRAILLE_TO_ENG[char]]
    
    return res

  def translate(self):
    '''Function which translates the given phrase into the opposite language'''
    if self.is_braille():
      return self.translate_to_english()
    else:
      return self.translate_to_braille()


if __name__ == '__main__':
  
  # Creating a string representation of the CLI input
  cli_input = " ".join(sys.argv[1:])

  ## translate the CLI input and output to console
  translator = Translator(cli_input)
  ans = translator.translate()
  print(ans)

