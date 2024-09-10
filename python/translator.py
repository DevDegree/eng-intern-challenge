import sys
import re

# the translation dictionary: keys are braille codes, value is a 3-tuple of english characters
# (lowercase, uppercase, number) that correspond to the braille code in the key
alphabet = {
  "O.....": ("a", "A", "1"),
  "O.O...": ("b", "B", "2"),
  "OO....": ("c", "C", "3"),
  "OO.O..": ("d", "D", "4"),
  "O..O..": ("e", "E", "5"),
  "OOO...": ("f", "F", "6"),
  "OOOO..": ("g", "G", "7"),
  "O.OO..": ("h", "H", "8"),
  ".OO...": ("i", "I", "9"),
  ".OOO..": ("j", "J", "0"),
  "O...O.": ("k", "K"),
  "O.O.O.": ("l", "L"),
  "OO..O.": ("m", "M"),
  "OO.OO.": ("n", "N"),
  "O..OO.": ("o", "O"),
  "OOO.O.": ("p", "P"),
  "OOOOO.": ("q", "Q"),
  "O.OOO.": ("r", "R"),
  ".OO.O.": ("s", "S"),
  ".OOOO.": ("t", "T"),
  "O...OO": ("u", "U"),
  "O.O.OO": ("v", "V"),
  ".OOO.O": ("w", "W"),
  "OO..OO": ("x", "X"),
  "OO.OOO": ("y", "Y"),
  "O..OOO": ("z", "Z"),
  "......": (" ", " ", " ")
}

uppercase_code = ".....O" # braille code that indicats one uppercase letter follows
number_code = ".O.OOO" # braille code that indicates numbers follow until next space

# get braille string from english string
def braille_to_english(str):
  english = ""
  uppercase_flag = False
  number_flag = False
  char_list = re.findall("......", str) # split string into list with 6 symbols in each substring
  for char in char_list:
    if char == uppercase_code:
      uppercase_flag = True
    elif char == number_code:
      number_flag = True
    elif uppercase_flag:
      english += get_uppercase_english(char)
      uppercase_flag = False
    elif number_flag:
      if get_number(char) == " ":
        number_flag = False # reset the number flag if we get to a space
      english += get_number(char)
    else:
      english += get_lowercase_english(char)
  return english

# get english string from braille string
def english_to_braille(str):
  braille = ""
  number_flag = False
  for char in str:
    if char.isupper():
      braille += uppercase_code # insert uppercase code if following character is uppercase
    if char.isnumeric() and not number_flag:
      braille += number_code # insert number code if following character is the beginning of a number
      number_flag = True
    if char == " " and number_flag:
      number_flag = False # reset the number flag if a space is reached
    braille += get_braille_char(char)
  return braille

# get the braille of one character
def get_braille_char(english_char):
  for key, value in alphabet.items():
    for s in value: # iterate through the tuple of possible characters of this key
      if s == english_char:
        return key
  raise ValueError("No matching braille character found!") # raise exception if no matching braille character found

# get one lowercase english character from one braille character
def get_lowercase_english(braille_char):
  return alphabet[braille_char][0]

# get one uppercase english character from one braille character
def get_uppercase_english(braille_char):
  return alphabet[braille_char][1]

# get one english number from one braille character
def get_number(braille_char):
  return alphabet[braille_char][2]

# check if the input string is braille or not
def is_braille(str):
  braille_matching_regex = re.compile("[O.]+") # braille only contains O or .
  return re.fullmatch(braille_matching_regex, str) != None # if matched, then re returns a list which is not None

# main executable code starts here
input = ' '.join(sys.argv[1:]) # retrieve original command parameters

if is_braille(input):
  print(braille_to_english(input))
else:
  print(english_to_braille(input))
