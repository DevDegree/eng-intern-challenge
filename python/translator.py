import sys

BRAILLE_CHARS = ['o','.']

ENGLISH_ALPHABET_TO_BRAILLE_MAP = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO',
    ' ': '......',
}

ENGLISH_DIGIT_TO_BRAILLE_MAP = { '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4':'OO.O..', '5': 'O..O..', 
                                 '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',}

ENGLISH_SPECIAL_CHAR_TO_BRAILLE_MAP = {
  'capital_follows': '.....O',
  'decimal_follows': '.O...O',
  'number_follows': '.O.OOO',
}
BRAILLE_TO_ENGLISH_DIGIT_MAP = {v: k for k, v in ENGLISH_DIGIT_TO_BRAILLE_MAP.items()}
BRAILLE_TO_ENGLISH_MAP = {v: k for k, v in ENGLISH_ALPHABET_TO_BRAILLE_MAP.items()}
BRAILLE_TO_ENGLISH_SPECIAL_CHAR_MAP = {v: k for k, v in ENGLISH_SPECIAL_CHAR_TO_BRAILLE_MAP.items()}


def main():
  input_string = ' '.join(sys.argv[1:])
  output_string = translate(input_string)
  print(output_string)

def translate(input_string):
  if all(c.lower() in BRAILLE_CHARS for c in input_string) and len(input_string)%6 == 0:
    return translate_to_english(input_string)
  else:
    return translate_to_braille(input_string)


def translate_to_braille(input_string):
  """
    Translates an input string from English to Braille.

    Args:
        input_string (str): The string to be translated.

    Returns:
        result (str): The translated string in Braille.
  """
  result = ""
  number_follows = False
  for char in input_string:
    if char.isupper():
      result += ENGLISH_SPECIAL_CHAR_TO_BRAILLE_MAP.get("capital_follows", "")
      result += ENGLISH_ALPHABET_TO_BRAILLE_MAP.get(char.lower(), "")
    elif char.isdigit():
      if not number_follows:
        result += ENGLISH_SPECIAL_CHAR_TO_BRAILLE_MAP.get("number_follows", "")
        number_follows = True
      result += ENGLISH_DIGIT_TO_BRAILLE_MAP.get(char, "")
    elif char == " ":
      number_follows = False
      result += ENGLISH_ALPHABET_TO_BRAILLE_MAP.get(" ")
    else:
      result += ENGLISH_ALPHABET_TO_BRAILLE_MAP.get(char, "")
  return result


def translate_to_english(input_string):
  """
    Translates an input string from Braille to English.

    Args:
        input_string (str): The string to be translated.

    Returns:
        result (str): The translated string in English. 
  """
  result = ""
  capital_follows = False
  number_follows = False

  for i in range(0, len(input_string), 6):
    braille_char = input_string[i:i+6]
    if  BRAILLE_TO_ENGLISH_SPECIAL_CHAR_MAP.get(braille_char, "") == "capital_follows":
      capital_follows = True
    elif BRAILLE_TO_ENGLISH_SPECIAL_CHAR_MAP.get(braille_char, "") == "number_follows":
      number_follows = True
    elif number_follows:
      result += BRAILLE_TO_ENGLISH_DIGIT_MAP.get(braille_char, "")
    elif BRAILLE_TO_ENGLISH_MAP.get(braille_char, "") == " ":
      result += " "
      number_follows = False
    elif capital_follows:
      result += BRAILLE_TO_ENGLISH_MAP.get(braille_char, "").upper()
      capital_follows = False
    else:
      result += BRAILLE_TO_ENGLISH_MAP.get(braille_char, "")
  return result


if __name__ == "__main__":
    main()
