import sys

# Dictionary mapping English characters to Braille codes
eng_to_braille = {
  "a": "O.....",
  "b": "O.O...",
  "c": "OO....",
  "d": "OO.O..",
  "e": "O..O..",
  "f": "OOO...",
  "g": "OOOO..",
  "h": "O.OO..",
  "i": ".OO...",
  "j": ".OOO..",
  "k": "O...O.",
  "l": "O.O.O.",
  "m": "OO..O.",
  "n": "OO.OO.",
  "o": "O..OO.",
  "p": "OOO.O.",
  "q": "OOOOO.",
  "r": "O.OOO.",
  "s": ".OO.O.",
  "t": ".OOOO.",
  "u": "O...OO",
  "v": "O.O.OO",
  "w": ".OOO.O",
  "x": "OO..OO",
  "y": "OO.OOO",
  "z": "O..OOO",
  ".": "..OO.O",
  ",": "..O...",
  "?": "..O.OO",
  "!": "..OOO.",
  ":": "..OO..",
  ";": "..O.O.",
  "-": "....OO",
  "/": ".O..O.",
  "(": "O.O..O",
  ")": ".O.OO.",
  " ": "......",
  "num": ".O.OOO",
  "cap": ".....O",
  "decimal": ".O...O"
}

# Dictionary mapping English digits and associated characters to Braille code
eng_to_braille_digits = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
    ">": "O..OO.",
    "<": ".OO..O"
}

# Reverse dictionaries for Braille to English translation
braille_to_eng = {v: k for k, v in eng_to_braille.items()}
braille_to_eng_digits = {v: k for k, v in eng_to_braille_digits.items()}

def trans_eng_to_braille(to_be_trans):
    """
    Translates English phrases to Braille.

    :param to_be_trans: the English phrase to be translated. Must be a string.
    :return: Translated phrase into Braille (one continuous string). 
    """
    translated = []
    i = 0
    num_mode = False
    while i in range (0,len(to_be_trans)):
        if num_mode and to_be_trans[i]==" ":
            num_mode = False
        cap_mode = False
        dec_mode = False
        if to_be_trans[i].isdigit() and not num_mode:
            translated.append(eng_to_braille["num"])
            num_mode = True
        elif to_be_trans[i] == "." and to_be_trans[i+1].isdigit():
            dec_mode = True
        elif to_be_trans[i].isupper():
            cap_mode = True

        if num_mode:
            translated.append(eng_to_braille_digits[to_be_trans[i]])
        elif cap_mode:
            translated.append(eng_to_braille["cap"])
            translated.append(eng_to_braille[to_be_trans[i].lower()])
        elif dec_mode:
            translated.append(eng_to_braille["decimal"])
        else:
            translated.append(eng_to_braille[to_be_trans[i]])
        
        i += 1

    return ''.join(translated)

def trans_braille_to_eng(to_be_trans):
    """
    Translates Braille phrases to English.

    :param to_be_trans: the Braille phrase to be translated. Must be a string.
    :return: Translated phrase into English as a string.
    """
    translated = []
    i = 0
    num_mode = False

    while i in range (0,len(to_be_trans)):
        cap_mode = False
        if to_be_trans[i:i+6] == ".O.OOO":
            num_mode = True
            i += 6
        elif to_be_trans[i:i+6] == ".....O":
            cap_mode = True
            i += 6
        elif to_be_trans[i:i+6] == "......":
            num_mode=False

        if num_mode:
            translated.append(braille_to_eng_digits[to_be_trans[i:i+6]])
        elif cap_mode:
            translated.append(braille_to_eng[to_be_trans[i:i+6]].upper())
        else:
            translated.append(braille_to_eng[to_be_trans[i:i+6]])
        
        i += 6

    return (''.join(translated))

def is_braille(to_be_trans):
    """
    Checks if the phrase is in Braille representation.

    :param to_be_trans: Phrase to be translated (either in English or Braille representation). Must be a string.
    :return" True if phrase is in Braille. False if phrase is in English
    """
    return all(char in ['O','.'] for char in to_be_trans)

def translate(to_be_trans):
    """
    Translates an English phrase into Braille represntation, or vice versa.

    :param to_be_trans: Phrase to be translated (either in English or Braille representation). Must be a string.
    :return: translated phrase as a string
    """
    if is_braille(to_be_trans):
        translated = trans_braille_to_eng(to_be_trans)
    else:
        translated = trans_eng_to_braille(to_be_trans)
    
    return translated

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py \"Your text here\"")
        sys.exit(1)
    
    input_text = ' '.join(sys.argv[1:])
    
    print(translate(input_text))

if __name__ == "__main__":
    main()
