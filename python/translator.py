import sys
# Requirements:

# Characters are either O or .   ---- Read left to right, line by line, starting top left

# When Braille capital follows is read, next symbol should be capitalized

# When Braille number follows, assume all following symbols are numbers until the next space symbol

# BLACK DOTS ARE 0 ------ WHITE DOTS ARE .



BRAILLE_ALPHABET = {
  "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..",
  "e": "O..O..", "f": "OOO...", "g": "OOOO..", "h": "O.OO..",
  "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
  "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", 
  "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", 
  "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", 
  "y": "OO.OOO", "z": "O..OOO"
}

SPACE = "......"
CAPITAL_FOLLOWS = ".....O"
NUMBER_FOLLOWS = ".O.OOO"

BRAILLE_NUMS = {
  "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", 
  "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", 
  "9": ".OO...", "0": ".OOO.."
}

BRAILLE_DECIMALS = {
  ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.",
  ":": "..OO..", ";": "..O.O.", "-": "....OO", "/": ".O..O.",
  "<": ".OO..O", ">": "O..OO.", "(": "O.O..O", ")": ".O.OO."
}


# 1 - Check if the input is either Braille or English:

def translate_user_input(user_input):
  """
    checks wether the input is in Braille or in English.
    Once the user input is checked, the value is sent to the appropriate 
    function to do the translation.
  """
  if user_input.startswith((".", "O")) and len(user_input.replace(" ", "")) % 6 == 0:
    braille_to_english(user_input)
  else:
    english_to_braille(user_input)


# 2 - Braille to English
def braille_to_english(verified_text):
    english_text = ""
    cap_follows = False
    number_follows = False

    # Inverts the hashpmaps to get the key from the value
    INV_BRAILLE_ALPHABET = {v: k for k, v in BRAILLE_ALPHABET.items()}
    INV_BRAILLE_NUMS = {v: k for k, v in BRAILLE_NUMS.items()}


    for i in range(0, len(verified_text), 6):
        section = verified_text[i:i+6]

        if section == CAPITAL_FOLLOWS:
            cap_follows = True
        elif section == NUMBER_FOLLOWS:
            number_follows = True
        elif section == SPACE:
            english_text += " "
            number_follows = False
        else:
            if number_follows:
                english_text += INV_BRAILLE_NUMS.get(section, "")
            elif cap_follows:
                english_text += INV_BRAILLE_ALPHABET.get(section, "").upper()
                cap_follows = False
            else:
                english_text += INV_BRAILLE_ALPHABET.get(section, "")
    print(english_text)



# 3 - English to Braille
def english_to_braille(verified_text):
  braille_text = ""
  for char in verified_text:
    if char.isupper():
      braille_text += CAPITAL_FOLLOWS + BRAILLE_ALPHABET.get(char.lower(), "")
    elif char.isdigit():
      braille_text += NUMBER_FOLLOWS + BRAILLE_NUMS.get(char, "")
    elif char.isspace():
      braille_text += SPACE
    elif char in BRAILLE_DECIMALS:
      braille_text += BRAILLE_DECIMALS.get(char, "")
    else:
      braille_text += BRAILLE_ALPHABET.get(char, "")
  
  print(braille_text)
  
  """
  Was testing bug towards the end with the english to braille function...leaving it cuz why not :))
  """
  # Hello World
  # .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..
  # .....OO.OO.............O.OOO.O
  
  # ....[30 chars]OOO......O.OOOO.O....O.OOOOO..........OO..OO.....OOO.OOOO..OOO
 
  # ....[30 chars]OOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO 
def main():
  
  if len(sys.argv) < 2:
    print("Please provide a string to translate")
    sys.exit(1)
  else: 
    user_input = " ".join(sys.argv[1:])
    translate_user_input(user_input)

if __name__ == "__main__":
    main()
