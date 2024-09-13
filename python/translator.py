import sys
import yaml
import os


braille_data = '''
eng_to_braille:
  # Letters
  a: "O....."
  b: "O.O..."
  c: "OO...."
  d: "OO.O.."
  e: "O..O.."
  f: "OOO..."
  g: "OOOO.."
  h: "O.OO.."
  i: ".OO..."
  j: ".OOO.."
  k: "O...O."
  l: "O.O.O."
  m: "OO..O."
  n: "OO.OO."
  o: "O..OO."
  p: "OOO.O."
  q: "OOOOO."
  r: "O.OOO."
  s: ".OO.O."
  t: ".OOOO."
  u: "O...OO"
  v: "O.O.OO"
  w: ".OOO.O"
  x: "OO..OO"
  y: "OO.OOO"
  z: "O..OOO"

  # Numbers (with number follows indicator required)
  "1": "O....."
  "2": "O.O..."
  "3": "OO...."
  "4": "OO.O.."
  "5": "O..O.."
  "6": "OOO..."
  "7": "OOOO.."
  "8": "O.OO.."
  "9": ".OO..."
  "0": ".OOO.."

  # Symbols
  ".": "..OO.O"
  ",": "..O..."
  "?": "..O.OO"
  "!": "..OOO."
  ":": "..OO.."
  ";": "..O.O."
  "-": "....OO"
  "/": ".O..O."
  "<": ".OO..O"
  ">": "O..OO."
  "(": "O.O..O"
  ")": ".O.OO."

  # Special control characters
  CAPITAL: ".....O"   # Capital follows
  DECIMAL: ".O...O"   # Decimal follows
  NUMBER: ".O.OOO"    # Number follows
  SPACE: "......"     # Space

braille_to_eng:
  # Letters
  "O.....": "a"
  "O.O...": "b"
  "OO....": "c"
  "OO.O..": "d"
  "O..O..": "e"
  "OOO...": "f"
  "OOOO..": "g"
  "O.OO..": "h"
  ".OO...": "i"
  ".OOO..": "j"
  "O...O.": "k"
  "O.O.O.": "l"
  "OO..O.": "m"
  "OO.OO.": "n"
  "O..OO.": "o"
  "OOO.O.": "p"
  "OOOOO.": "q"
  "O.OOO.": "r"
  ".OO.O.": "s"
  ".OOOO.": "t"
  "O...OO": "u"
  "O.O.OO": "v"
  ".OOO.O": "w"
  "OO..OO": "x"
  "OO.OOO": "y"
  "O..OOO": "z"

  # Numbers (with number follows indicator)
  "numbers":
    "O.....": "1"
    "O.O...": "2"
    "OO....": "3"
    "OO.O..": "4"
    "O..O..": "5"
    "OOO...": "6"
    "OOOO..": "7"
    "O.OO..": "8"
    ".OO...": "9"
    ".OOO..": "0"

  # Symbols

  "..OO.O": "."
  "..O...": ","
  "..O.OO": "?"
  "..OOO.": "!"
  "..OO..": ":"
  "..O.O.": ";"
  "....OO": "-"
  ".O..O.": "/"
  ".O..O.": "<"
  "O..OO.": ">"
  "O.O..O": "("
  ".O.OO.": ")"

  # Special control characters
  ".....O": "CAPITAL"   # Capital follows
  ".O.OOO": "NUMBER"    # Number follows
  "......": "SPACE"     # Space
  ".O...O": "DECIMAL"
'''

def load_yaml_data():
    """Loads the YAML data from the embedded string."""
    return yaml.safe_load(braille_data)
    
def find_input_type(input_string):
    """Determines if the input string is in English or Braille."""
    return 'braille' if all(c in ['O', '.'] for c in input_string) else 'english'

def english_to_braille(english_string, braille_map):
    """Translates from English to Braille."""
    result = ""
    is_number = False
    for char in english_string:
        if char.isupper():
            result += braille_map["CAPITAL"]
            char = char.lower()
            is_number = False
        if char.isdigit():
            if not(is_number):
                result += braille_map["NUMBER"]
            is_number = True

        # if char == '.' and is_number:
        #     result += braille_map["DECIMAL"]
        #     is_number = True # Continue number mode after a decimal point
        #     continue

        if char == ' ':
            char = "SPACE"
            is_number = False
        result += braille_map.get(char, '') 
    return result

def braille_to_english(braille_string, braille_map, reverse_braille_map):
    """Translates from Braille to English."""
    result = ""
    is_capital = False
    is_number = False

    # Split the Braille input into chunks of 6 characters (each Braille character)
    for i in range(0, len(braille_string), 6):
        braille_char = braille_string[i:i+6]

        # Check for control characters
        if braille_char == braille_map["CAPITAL"]:
            is_capital = True
            continue
        if braille_char == braille_map["NUMBER"]:
            is_number = True
            continue
        if braille_char == braille_map["SPACE"]:
            result += " "
            is_number = False  # Reset number state after space
            continue

        # if is_number and braille_char==braille_map["DECIMAL"]:
        #     result += "."
        #     is_number = True
        #     continue

        # Normal Braille characters
        if is_number:
            char = reverse_braille_map.get('numbers', {}).get(braille_char)
        else:
            char = reverse_braille_map.get(braille_char, '')
        if is_capital:
            char = char.upper()
            is_capital = False
        result += char
    return result


def main():
    # Load the mappings from YAML files
    yaml_data = load_yaml_data()
    braille_map = yaml_data['eng_to_braille']
    reverse_braille_map = yaml_data['braille_to_eng']

    # Read the input from the command line arguments
    input_string = ' '.join(sys.argv[1:]) if len(sys.argv) > 1 else ''

    # Determine input type and translate accordingly
    if find_input_type(input_string) == 'english':
        print(english_to_braille(input_string, braille_map))
    else:
        print(braille_to_english(input_string, braille_map, reverse_braille_map))

if __name__ == "__main__":
    main()