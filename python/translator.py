import sys

BRAILLE_TO_ENG = {
  'O.....': 'a',
  'O.O...': 'b',
  'OO....': 'c',
  'OO.O..': 'd',
  'O..O..': 'e',
  'OOO...': 'f',
  'OOOO..': 'g',
  'O.OO..': 'h',
  '.OO...': 'i',
  '.OOO..': 'j',
  'O...O.': 'k',
  'O.O.O.': 'l',
  'OO..O.': 'm',
  'OO.OO.': 'n',
  'O..OO.': 'o',
  'OOO.O.': 'p',
  'OOOOO.': 'q',
  'O.OOO.': 'r',
  '.OO.O.': 's',
  '.OOOO.': 't',
  'O...OO': 'u',
  'O.O.OO': 'v',
  '.OOO.O': 'w',
  'OO..OO': 'x',
  'OO.OOO': 'y',
  'O..OOO': 'z',
  '.....O': 'capital follows',
  '.O.OOO': 'number follows',
  '......': ' '
  }

B2E_NUMS = {
  '.OOO..': '0',
  'O.....': '1',
  'O.O...': '2',
  'OO....': '3',
  'OO.O..': '4',
  'O..O..': '5',
  'OOO...': '6',
  'OOOO..': '7',
  'O.OO..': '8',
  '.OO...': '9',
  '......': ' '
  }

ENG_TO_BRAILLE = {v:k for k, v in BRAILLE_TO_ENG.items()}
ENG_TO_BRAILLE.update({v:k for k, v in B2E_NUMS.items()})

def input_lang(input: list) -> str:
  '''
  returns input language
  '''
  for s in input:
    for c in s:
      if c != 'O' or c != '.':
        return "ENGLISH"
  return "BRAILLE"

def is_letter(s: str) -> bool:
  '''
  check if an english character is a letter
  '''
  return ord(s) <= ord('z') and ord(s) >= ord('a') 

def to_braille(input: list) -> str:
  '''
  translate to braille
  '''
  translated = []
  prev_was_letter = True

  for s in input:
    for c in s:
      if c.lower() != c:
        # if c was uppercase
        translated.append(ENG_TO_BRAILLE['capital follows'])
        c = c.lower()

      if is_letter(c) and (not prev_was_letter):
        # was numbers and now writing letters
        # add a space
        translated.append(ENG_TO_BRAILLE[" "])
      elif (not is_letter(c)) and prev_was_letter:
        prev_was_letter = False
        translated.append(ENG_TO_BRAILLE['number follows'])
        # ASSUMPTION: NO DECIMALS
      translated.append(ENG_TO_BRAILLE[c])
    # after each word, add a space
    translated.append(ENG_TO_BRAILLE[' '])
      
  return "".join(translated[:-1]) 

def to_eng(input: list) -> str:
  # braille should just be list of length 1
  # check edge case where it's empty
  if len(list) == 0:
    return ""
  input = list[0]

  translated = []
  working_dict = BRAILLE_TO_ENG

  next_capital = False # if next char needs to be capitalized

  for i in range(0, len(input), 6):
    # if i % 6 == 0
    c = input[i:i+6]

    if working_dict[c] == 'number follows':
      # don't have to do anything to convert back to string
      working_dict = B2E_NUMS
      continue
    elif working_dict[c] == ' ':
      # if we get a space, we're now working with letters either way
      working_dict = BRAILLE_TO_ENG
    elif working_dict[c] == 'capital_follows':
      next_capital = True
    
    if next_capital:
      translated.append(working_dict[c].upper())
      next_capital = False
    else:
      translated.append(working_dict[c])

  return "".join(translated)
    
def main():
  input = sys.argv[1:]
  lang = input_lang(input)

  if lang == "BRAILLE":
    sys.stdout.write(to_eng(input))
  else: 
    sys.stdout.write(to_braille(input))
  
if __name__ == "__main__":
    main()

