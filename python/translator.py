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
    1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E',
    6: 'F', 7: 'G', 8: 'H', 9: 'I', 0: 'J'
  }

  OPERATIONS = {
    'SPACE': '......',
    'CAPITAL': '.....0',
    'NUMBER': '.0.000'
  }

  LETTERS_BRAILLE_TO_ENG = invert_map(LETTERS_ENG_TO_BRAILLE)
  LETTERS_TO_NUMBERS = invert_map(NUMBERS_TO_LETTERS)

  def __init__(self, phrase):
    self.phrase = phrase

  def is_braille(self):
    pass

  def english_to_braille(self):
    pass

  def braille_to_english(self):
    pass

  def translate(self):
    pass


if __name__ == '__main__':
  
  # Creating a string representation of the CLI input
  cli_input = " ".join(sys.argv[1:])

  translator = Translator(cli_input)
  # ans: string = translator.translate()
  # print(ans)
