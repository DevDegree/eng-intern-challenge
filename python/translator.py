import sys
import re

class Translator:
    """
    Translator class for converting between English text and Braille.
    Pre-definde constants:
      ENG_BRAILLE (dict): Mapping of English characters and punctuation to Braille.
      SPECIAL_MAPPINGS (dict): Special Braille sequences for indicating capital letters and numbers.
      BRAILLE_ENG (dict): Reverse mapping of Braille to English characters.
    Methods:
      is_braille(string: str) -> bool:
        Determines if a string is in Braille using a regex pattern.
      braille_to_english(braille_str: str) -> str:
        Converts a Braille string to English text.
      ENG_BRAILLE(english_str: str) -> str:
        Converts English text to a Braille string.
      translate(input_str: str) -> str:
        Determines the input type (Braille or English) and translates it to the other form.
    """
    # English characters to Braille mapping
    ENG_BRAILLE = {
        **{ch: braille for ch, braille in zip("abcdefghijklmnopqrstuvwxyz", [
            "O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..",
            "O.OO..", ".OO...", ".OOO..", "O...O.", "O.O.O.", "OO..O.", "OO.OO.",
            "O..OO.", "OOO.O.", "OOOOO.", "O.OOO.", ".OO.O.", ".OOOO.", "O...OO",
            "O.O.OO", ".OOO.O", "OO..OO", "OO.OOO", "O..OOO"
        ])},
        **{ch: braille for ch, braille in zip("0123456789", [
          ".OOO..", "O.....", "O.O...", "OO....", "OO.O..", "O..O..","OOO...", "OOOO..", "O.OO..", ".OO..."
        ])},
        **{ch: braille for ch, braille in zip(".,?!:;-/<>() ", [
            "..OO.O", "..O...", "..O.OO", "..OOO.", "..OO..", "..O.O.", "....OO",
            ".O..O.", ".OO..O", "O..OO.", "O.O..O", ".O.OO.", "......"
        ])}
    }
    
    SPECIAL_MAPPINGS = {
        "CAPITAL_FOLLOWS": ".....O",
        "NUMBER_FOLLOWS": ".O.OOO"
    }
    
    BRAILLE_ENG = {v: k for k, v in ENG_BRAILLE.items()}

    def is_braille(string: str) -> bool:
        """Determines if a string is in braille using a regex pattern"""
        return re.fullmatch(r'[O\.]+', string) and len(string) % 6 == 0
    
    def braille_to_english(braille_str: str) -> str:
        result = []
        capital = False
        isNumber = False
        for i in range(0, len(braille_str), 6):
            substr = braille_str[i:i+6]
            if substr == Translator.SPECIAL_MAPPINGS["CAPITAL_FOLLOWS"]:
                capital = True
            elif substr == Translator.SPECIAL_MAPPINGS["NUMBER_FOLLOWS"]:
                isNumber = True
            else:
                char = Translator.BRAILLE_ENG.get(substr, "?")
                if isNumber:
                    char = str(ord(char) - ord('a') + 1)  # Convert 'a' to '1', 'b' to '2', etc.
                    isNumber = False
                result.append(char.upper() if capital else char)
                capital = False
        return ''.join(result)
      
    def english_to_braille(english_str: str) -> str:
      result = []
      isNumber = False
      for ch in english_str:
          if ch.isupper():
              # If we are in a number sequence, exit the number sequence by appending a space
              if isNumber:
                  result.append(Translator.ENG_BRAILLE[" "])
                  isNumber = False
              # Add capital letter indication
              result.append(Translator.SPECIAL_MAPPINGS["CAPITAL_FOLLOWS"])
              result.append(Translator.ENG_BRAILLE[ch.lower()])
          elif ch.isnumeric():
              # If not in a number sequence, start number sequence
              if not isNumber:
                  result.append(Translator.SPECIAL_MAPPINGS["NUMBER_FOLLOWS"])
                  isNumber = True
              result.append(Translator.ENG_BRAILLE[ch])
          else:
              # If we encounter a non-numeric character, exit the number sequence
              if isNumber:
                  isNumber = False 
              result.append(Translator.ENG_BRAILLE[ch])
      return ''.join(result)
    
    def translate(input_str: str) -> str:
        if Translator.is_braille(input_str):
            return Translator.braille_to_english(input_str)
        return Translator.english_to_braille(input_str)
      

if __name__ == "__main__":
  argv = sys.argv[1:]
  if argv:
    print(Translator.translate(" ".join(argv)))
  else:
    sys.exit(1)