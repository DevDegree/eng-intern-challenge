import sys

REVERSE_BRAILLE_MAP_LETTERS = {
  'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd','O..O..': 'e', 
  'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h','.OO...': 'i', '.OOO..': 'j', 
  'O...O.': 'k', 'O.O.O.': 'l','OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'O', 
  'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
  'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 
  'O..OOO': 'z',  '..OO.O' : '.', '..O...': ',', '..O.OO': '?' , '..OOO.': '!',
  '..OO..': ':' ,  '..O.O.': ';' , '....OO': '-' , '.O..O.': '/' ,'.OO..O': '<' ,
  'O..OO.': '>' ,'O.O..O': '(' ,  '.O.OO.': ')', '......': ' '

}

REVERSE_BRAILLE_MAP_NUMBERS = {
  'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4',
  'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8',
  '.OO...': '9', '.OOO..': '0', '..OO.O':'.'
}


BRAILLE_MAP_CHARS = {
  'a' : 'O.....', 'b' : 'O.O...', 'c' : 'OO....', 'd' : 'OO.O..', 'e' : 'O..O..',
  'f' : 'OOO...', 'g' : 'OOOO..', 'h' : 'O.OO..', 'i' : '.OO...', 'j' : '.OOO..',
  'k' : 'O...O.', 'l' : 'O.O.O.', 'm' : 'OO..O.', 'n' : 'OO.OO.', 'o' : 'O..OO.',
  'p' : 'OOO.O.', 'q' : 'OOOOO.', 'r' : 'O.OOO.', 's' : '.OO.O.', 't' : '.OOOO.',
  'u' : 'O...OO', 'v' : 'O.O.OO', 'w' : '.OOO.O', 'x' : 'OO..OO', 'y' : 'OO.OOO',
  'z' : 'O..OOO', '.': '..OO.O',  ',': '..O...', '?':'..O.OO' , '!':'..OOO.',
  ':':'..OO..', ';': '..O.O.', '-':'....OO', '/':'.O..O.', '<':'.OO..O',
  '>':'O..OO.', '(':'O.O..O', ')': '.O.OO.', ' ':'......', 
  '1':'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
  '5': 'O..O..', '6': 'OOO...', '7':  'OOOO..', '8': 'O.OO..',
  '9': '.OO...', '0': '.OOO..',
}

# Flags, kept seperate for clarity
CAPITAL_BRAILLE = '.....O'

NUMBER_BRAILLE = '.O.OOO'

DECIMAL_BRAILLE = '.O...O'

SPACE_BRAILLE = '......'


def translate_to_english(braille_text):
  # split up the braille text into each character
  braille_chars = [braille_text[i:i+6] for i in range(0, len(braille_text), 6)]
  result = []
  number_mode = False
  capital = False

  # Check for flags to minpulate text 
  for char in braille_chars:
    if char == NUMBER_BRAILLE:
      number_mode = True
      
    elif char == SPACE_BRAILLE:
      number_mode = False
      result.append(REVERSE_BRAILLE_MAP_LETTERS[char])
      
    elif char == CAPITAL_BRAILLE:
      capital = True
      
    elif char == DECIMAL_BRAILLE:
      number_mode = True
      
    else:
      # if number mode, check numbers map
      if number_mode:
        number = REVERSE_BRAILLE_MAP_NUMBERS[char]
        result.append(number)
      # else check letters
      else:
        letter = REVERSE_BRAILLE_MAP_LETTERS[char]
        if capital:
          result.append(letter.upper())
          capital = False
          
        else:
          result.append(letter)
          
  return ''.join(result)
  
def translate_to_braille(english_text):
  braille_text = []
  number_mode = False

  # iterate through each character
  for char in english_text:
    
    if char.isdigit():
      if not number_mode:
        braille_text.append(NUMBER_BRAILLE)
        number_mode = True
        
    elif char == '.':
      if number_mode:
        braille_text.append(DECIMAL_BRAILLE)
        
    else:
      if char.isupper():
        braille_text.append(CAPITAL_BRAILLE)
        char = char.lower()
      number_mode=False
      
    braille_text.append(BRAILLE_MAP_CHARS[char])
  return ''.join(braille_text)


def main():
  if len(sys.argv)>1:
    user_input = ' '.join(sys.argv[1:])
    
    # check if the user input is a multiple of 6 and contains only braille characters
    if len(user_input)%6 == 0 and all(char in 'O1.' for char in user_input):
      translated = translate_to_english(user_input)
      
    else:
      translated = translate_to_braille(user_input)
    print(translated)
  else:
    print("No input given")


if __name__=="__main__":
  main()
