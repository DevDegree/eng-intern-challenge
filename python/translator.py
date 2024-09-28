import sys

# Maps for braille character and it's corresponding English character or number
# Only considering inputs with characters from a-z, A-Z, 0-9 and space
braille_to_english = {
  'O.....' : 'a', 'O.O...' : 'b', 'OO....' : 'c', 'OO.O..' : 'd', 'O..O..' : 'e', 'OOO...' : 'f', 'OOOO..': 'g', 
  'O.OO..' : 'h', '.OO...' : 'i', '.OOO..' : 'j', 'O...O.' : 'k', 'O.O.O.' : 'l', 'OO..O.' : 'm', 'OO.OO.': 'n',
  'O..OO.' : 'o', 'OOO.O.' : 'p', 'OOOOO.' : 'q', 'O.OOO.' : 'r', '.OO.O.' : 's', '.OOOO.' : 't', 'O...OO': 'u',
  'O.O.OO' : 'v', '.OOO.O' : 'w', 'OO..OO' : 'x', 'OO.OOO' : 'y', 'O..OOO' : 'z', '..OO.O' : '.', '......' : ' ',
  '.....O' : 'CAPITAL', '.O...O' : 'DECIMAL', '.O.OOO' : 'NUMBER'
}

braille_to_numbers = {
  'O.....' : '1', 'O.O...' : '2', 'OO....' : '3', 'OO.O..' : '4', 'O..O..' : '5',
  'OOO...' : '6', 'OOOO..' : '7', 'O.OO..' : '8', '.OO...' : '9', '.OOO..' : '0' 
}

# Reverse the maps for English -> braille / number -> braille translation
english_to_braille = { english : braille for braille, english in braille_to_english.items() }
numbers_to_braille = { number : braille for braille, number in braille_to_numbers.items() }

def translate_braille_to_english(braille: str) -> str:

  """ Translate braille text to English characters """

  # Split the braille text at each 6th character and put it into an array
  braille_chars = [ braille[i : i + 6] for i in range(0, len(braille), 6) ]

  # Flags to raise when encountering special characters
  add_nums = False
  add_capitals = False

  # Translated English text
  result = ''

  for char in braille_chars:
    if char == '.....O': # CAPITAL 
      add_capitals = True
    elif char == '.O.OOO': # NUMBER
      add_nums = True
    elif char == '......': # SPACE
      result += ' '
      add_nums = False
    elif add_nums:
      # Add a number instead of a character
      result += braille_to_numbers[char]
    elif add_capitals:
      # Add the capital of a character
      result += braille_to_english[char].upper()
      add_capitals = False
    else:
      # Add all other characters
      result += braille_to_english[char]

  return result

def translate_english_to_braille(english: str) -> str:

  """ Translate English text to braille characters """

  # Flag to see if we have already added a the number flag (don't want to add multiple times)
  added_number_flag = False

  # Translated braille text
  result = ''

  for char in english:
    if char.isupper():
      # Add the "Capital Follows" braille character and the corresponding english character, converted to braille
      result += (english_to_braille['CAPITAL'] + english_to_braille[char.lower()])
    elif char.isnumeric():
      if not added_number_flag: 
        # Add the "Number Follows" braille character, if it hasn't been added before
        result += english_to_braille['NUMBER']
        added_number_flag = True

      # If the "Number Follows" character was already added, don't add it again
      result += numbers_to_braille[char]
    elif char == ' ':
      # Reset the number flag if space is encountered
      result += english_to_braille[char]
      added_number_flag = False
    else:
      # Add all other characters
      result += english_to_braille[char]
  
  return result

def translate(text: str):

  """ Determine if the text is braille or english and translates to the other one """

  # If every character in the input is either "O" or .
  # Consider it as braille and translate to english
  if all(char in 'O.' for char in text):
    print(translate_braille_to_english(text))
  else:
    print(translate_english_to_braille(text))

def main():
  # Join all the arguments together with spaces
  text = ' '.join(sys.argv[1:])
  translate(text)

if __name__ == '__main__':
  main()