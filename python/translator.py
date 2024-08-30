import sys

braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',

    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', 
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',

    'CAP': '.....O',
    'NUM': '.O.OOO',
    ' ': '......'
}

reversed_braille_letters = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z'
}

reversed_braille_numbers_indicators = {
    '.OOO..': '0', 'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4',
    'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9',

    '.....O': 'CAP', '.O.OOO': 'NUM', '......': ' '
}

def check_if_braille(text):
    """
      Verifies whether or not the text is Braille if and only if it only contains 'O's and '.'s.
    """
    return all(c in 'O.' for c in text)

def translate_to_braille(text):
    """
      Translates English text to Braille.
    """
    res = []
    num = False

    for c in text:
        if c.isdigit():
            if not num:
                res.append(braille_dict['NUM'])
                num = True
            res.append(braille_dict[c])
        elif c.isalpha():
            if c.isupper():
                res.append(braille_dict['CAP'])
            res.append(braille_dict[c.lower()])
            num = False
        elif c == ' ':
            res.append(braille_dict[' '])
            num = False

    return ''.join(res)

def translate_to_english(text):
    """
      Translates Braille text to English.
    """
    res = []
    num = False
    char = False
    
    for i in range(0, len(text), 6):
      c = text[i:i+6]
      if "NUM" == reversed_braille_numbers_indicators[c]:
          num = True
      elif "CAP" == reversed_braille_numbers_indicators[c]:
          char = True
      elif " " == reversed_braille_numbers_indicators[c]:
          res.append(' ')
          num = False
      else:
          if num:
              translated_char = reversed_braille_numbers_indicators[c]
              res.append(translated_char)
          else:
              translated_char = reversed_braille_letters[c]
              if char:
                  translated_char = translated_char.upper()
                  char = False
              res.append(translated_char)
    return ''.join(res)

def main():
    input = ' '.join(sys.argv[1:])
    print(translate_to_braille(input) if not check_if_braille(input) else translate_to_english(input))

if __name__ == "__main__":
    main()
