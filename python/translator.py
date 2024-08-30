import sys

BRAILLE_TO_ENG = {
  "O....." : 'a',
  "O.O..." : 'b',
  "OO...." : 'c',
  "OO.O.." : 'd',
  "O..O.." : 'e',
  "OOO..." : 'f',
  "OOOO.." : 'g',
  "O.OO.." : 'h',
  ".OO..." : 'i',
  ".OOO.." : 'j',
  "O...O." : 'k',
  "O.O.O." : 'l',
  "OO..O." : 'm',
  "OO.OO." : 'n',
  "O..OO." : 'o',
  "OOO.O." : 'p',
  "OOOOO." : 'q',
  "O.OOO." : 'r',
  ".OO.O." : 's',
  ".OOOO." : 't',
  "O...OO" : 'u',
  "O.O.OO" : 'v',
  ".OOO.O" : 'w',
  "OO..OO" : 'x',
  "OO.OOO" : 'y',
  "O..OOO" : 'z',
  "..OO.O" : 'O',
  "..O..." : ',',
  "..O.OO" : 'O',
  "..OOO." : '!',
  "..OO.." : ':',
  "..O.O." : ';',
  "....OO" : '-',
  ".O..O." : '/',
  ".OO..O" : '<',
  "O..OO." : '>',
  "O.O..O" : '(',
  ".O.OO." : ')',
  "......" : ' '
}

ENG_TO_BRAILLE = {
  letter : braille for braille, letter in BRAILLE_TO_ENG.items()
}

def main():
  words = sys.argv[1:]
  print(translate(words))

def translate(words):
  if len(words) > 1 or not set(words[0]).issubset(set("O.")):
    translation = to_braille(words)
  else:
    translation = to_chars(words)
  
  return translation

def to_braille(words):
  sentence = " ".join(words)
  is_num = False
  translation = ""

  for c in sentence:
    if c.isupper():
      translation += ".....O"
      c = chr(ord(c) + ord('a') - ord('A'))
    
    if c.isnumeric():
      if not is_num:
        is_num = True
        translation += ".O.OOO"
      
      if c == '0':
        c = 'j'
      else:
        c = chr(ord(c) + ord('a') - ord('1'))
    else:
      is_num = False
    
    translation += ENG_TO_BRAILLE[c]
  
  return translation

def to_chars(words):
  sentence = words[0]
  is_upper = False
  is_num = False
  translation = ""

  for i in range(0, len(sentence), 6):
    if sentence[i : i + 6] == ".....O":
      is_upper = True
      continue
    
    if sentence[i : i + 6] == ".O.OOO":
      is_num = True
      continue
    
    if sentence[i : i + 6] == ".O...O":
      continue
    
    if sentence[i : i + 6] == "......":
      is_num = False

    translation += chr(ord(BRAILLE_TO_ENG[sentence[i : i + 6]]) 
                      + (ord('A') - ord('a')) * is_upper 
                      + (ord('1') - ord('a')) * is_num)
    
    is_upper = False
  
  return translation

if __name__ == "__main__":
  main()
