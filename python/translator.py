import sys

ENG_TO_BRAILLE_CHARS = {
  'a': "O.....", 'b': "O.O...", 'c': "OO....",
  'd': "OO.O..", 'e': "O..O..", 'f': "OOO...",
  'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...",
  'j': ".OOO..", 'k': "O...O.", 'l': "O.O.O.",
  'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
  'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.",
  's': ".OO.O.", 't': ".OOOO.", 'u': "O...OO",
  'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO",
  'y': "OO.OOO", 'z': "O..OOO", ' ': "......",
}
ENG_TO_BRAILLE_NUMS = {
  '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", 
  '5': "O..O..", '6': "OOO...", '7': "OOOO..", '8': "O.OO..",
  '9': ".OO...", '0': ".OOO.."
}
CAPITAL_BRAILLE = ".....O"
NUMBER_BRAILLE = ".O.OOO"


def swap_keys_and_values(dictionary: dict) -> dict:
  return {value: key for key, value in dictionary.items()}


def check_is_braille(value: str) -> bool:
  if '.' in value:
    return True
  return False


def translate_braille_to_eng(value: str) -> str:
  BRAILLE_TO_ENG_CHARS = swap_keys_and_values(ENG_TO_BRAILLE_CHARS)
  BRAILLE_TO_ENG_NUMS = swap_keys_and_values(ENG_TO_BRAILLE_NUMS)
  NUM_CHARS_IN_SYMBOL = 6

  curr_symbol = ""
  translated_str = ""
  is_next_capital = False
  is_next_number = False

  if len(value) % NUM_CHARS_IN_SYMBOL != 0:
    raise ValueError
  
  for i in range(len(value)):
    curr_symbol += value[i]

    if len(curr_symbol) == NUM_CHARS_IN_SYMBOL:
      if curr_symbol == CAPITAL_BRAILLE:
        is_next_capital = True
      elif curr_symbol == NUMBER_BRAILLE:
        is_next_number = True
      elif is_next_capital and curr_symbol in BRAILLE_TO_ENG_CHARS:
        translated_str += BRAILLE_TO_ENG_CHARS[curr_symbol].upper()
        is_next_capital = False
      elif is_next_number and curr_symbol in BRAILLE_TO_ENG_NUMS:
        translated_str += BRAILLE_TO_ENG_NUMS[curr_symbol]
      elif (curr_symbol in BRAILLE_TO_ENG_CHARS and not is_next_number) or (is_next_number and curr_symbol == ENG_TO_BRAILLE_CHARS[' ']):
        translated_str += BRAILLE_TO_ENG_CHARS[curr_symbol]
        is_next_number = False
      else:
        raise ValueError
      
      curr_symbol = ""

  return translated_str


def translate_eng_to_braille(value: str) -> str:
  translated_str = ""

  for i in range(len(value)):
    if value[i] in ENG_TO_BRAILLE_CHARS:
      translated_str += ENG_TO_BRAILLE_CHARS[value[i]]
    elif value[i].lower() in ENG_TO_BRAILLE_CHARS:
      translated_str += CAPITAL_BRAILLE + ENG_TO_BRAILLE_CHARS[value[i].lower()]
    elif value[i] in ENG_TO_BRAILLE_NUMS:
      if i > 0 and value[i-1] not in ENG_TO_BRAILLE_NUMS:
          translated_str += NUMBER_BRAILLE
      translated_str += ENG_TO_BRAILLE_NUMS[value[i]]
    else:
      raise ValueError
      
  return translated_str


def main():
  if len(sys.argv) < 2:
    sys.exit("Need to provide at least one argument")

  input_value = ' '.join(sys.argv[1:])

  try:
    if check_is_braille(input_value):
      print(translate_braille_to_eng(input_value))
    else:
      print(translate_eng_to_braille(input_value))
  except ValueError:
    sys.exit("Input is invalid.")
  except:
    sys.exit("Something went wrong.")


if __name__ == "__main__":
  main()