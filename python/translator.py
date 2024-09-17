import sys

# Create dictionary 
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......'
}

braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', 
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

braille_special = {
    'capital': '.....O',  # Capitalization symbol
    'number': '.O.OOO',   # Number follows symbol
}

reverse_braille_alphabet = {x: y for y, x in braille_alphabet.items()}

reverse_braille_numbers = {x: y for y, x in braille_numbers.items()}

# define a function that convert input_text to braille
def to_braille (input_text):
  # initialize a empty result
  result = []
  # create a variable called number_mode, false indicate the program should convert text into alphabet
  number_mode = False

  # create a for-loop handling each char of the input_text
  for char in input_text:
    # condition when char is a number
    if char.isdigit() and not number_mode:
      result.append(braille_special['number'])
      number_mode = True

    # condition when char is a alphabet
    if char.isalpha():
      if char.isupper():
        result.append(braille_special['capital'])
      result.append(braille_alphabet[char.lower()])  # char in upper is convert to lower case so it matches the dictionary
      number_mode = False
    
    # condition when char is digit and in number mode
    elif char.isdigit():
      result.append(braille_numbers[char])
    
    # handling space
    elif char == ' ':
      result.append(braille_alphabet[' '])
      number_mode = False # see space, turn off number_mode
  
  return ''.join(result) # return one string
  
  # define another function convert input_brallie to text
def to_text (input_braille):
  result = []
  # because we have 2 special brallie case we need 2 mode booleans
  capital_mode = False
  number_mode = False

  # split input_brallie into 6-character chunks and handling each chunk
  for i in range (0, len(input_braille), 6):
    chunk = input_braille [i:i+6]

    if chunk == braille_special['capital']:
      capital_mode = True
    elif chunk == braille_special['number']:
      number_mode = True
    else:
      if number_mode and chunk in reverse_braille_numbers:
        result.append(reverse_braille_numbers[chunk])
      elif chunk in reverse_braille_alphabet:
        number_mode = False
        letter = reverse_braille_alphabet[chunk]
        if capital_mode:
          result.append(letter.upper())
          capital_mode = False
        else:
          result.append(letter)
  
  return ''.join(result)
  
def translator(input_str):
    if all(c in 'O.' for c in input_str):
        # Input is Braille
        return to_text(input_str)
    else:
        # Input is English
        return to_braille(input_str)

# Main program to take input
if __name__ == "__main__":   
    # Get input string from command line arguments
    input_str = ' '.join(sys.argv[1:])
    
    # Run the translator and print the result
    output_str = translator(input_str)
    print(output_str)
    
          
      




