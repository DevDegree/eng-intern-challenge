# English to Braille dictionary
en_br_dict = {
  'a':'O.....', 'b':'O.O...', 'c':'OO....', 'd':'OO.O..', 
  'e':'O..O..', 'f':'OOO...', 'g':'OOOO..', 'h':'O.OO..', 
  'i':'.00...', 'j':'.OOO..', 'k':'O...O.', 'l':'O.O.O.', 
  'm':'OO..O.', 'n':'OO.OO.', 'o':'O..OO.', 'p':'OOO.O.',
  'q':'OOOOO.', 'r':'O.OOO.', 's':'.OO.O.', 't':'.OOOO.', 
  'u':'O...OO', 'v':'O.O.OO', 'w':'.OOO.O', 'x':'OO..OO',
  'y':'OO.OOO', 'z':'O..OOO', '1':'0.....', '2':'O.O...',
  '3':'OO....', '4':'OO.O..', '5':'O..O..', '6':'OOO...',
  '7':'OOOO..', '8':'O.OO..', '9':'.OO...', '0':'.OOO..',
  'cap':'.....O', 'dec':'.O...O', 'num':'.O.OOO', '.':'..OO.O',
  ',':'..O...', '?':'..O.OO', '!':'..OOO.', ':':'..OO..',
  ';':'..O.O.', '-':'....OO', '/':'.O..O.', '<':'.OO..O',
  '>':'O..OO.', '(':'O.O..O', ')':'.O.OO.', ' ':'......',  
} 

# Braille to English dictionary
br_en_dict = {v: k for k, v in en_br_dict.items()} # invert previous dictionary

# English to Braille function
def en_to_br(en_text):
  output = []
  for char in en_text:
    if char in en_br_dict:
      output.append(en_br_dict[char])
    elif char.isdigit():
      output.append(en_br_dict['num'])
      output.append(en_br_dict[char])
    elif char.isupper():
      output.append(en_br_dict['cap'])
      output.append(en_br_dict[char.lower()])
    else:
      output.append('')        
  return ''.join(output) # output characters as one string

def br_to_en(br_text):
  output = []
  cap = False
  num = False
  for i in range(0, len(br_text), 6):
    current = br_text[i:i+6] # substring of current 6 dot section from the input
    if current in br_en_dict:
      output.append(br_en_dict[current])
      if cap:
        char = char.upper()
        cap = False
      output.append(char)
    elif current == en_br_dict['cap']:
      cap = True
    elif current == en_br_dict['num']:
      num = True
  return ''.join(output) # output characters as one string

def main(inp_text):
  # list of Braille characters
  braille_chars = ['O', '.']
  # checking if the input is Braille or English
  if all(char in braille_chars for char in inp_text):
    return br_to_en(inp_text)
  else:
    return en_to_br(inp_text)

if __name__ == '__main__':
  main()
  
