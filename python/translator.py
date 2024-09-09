import sys

class BrailleTranslator:
    BRAILLE = [
        "O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO..",  # a-j
        "O...O.", "O.O.O.", "OO..O.", "OO.OO.", "O..OO.", "OOO.O.", "OOOOO.", "O.OOO.", ".OO.O.", ".OOOO.",  # k-t
        "O...OO", "O.O.OO", ".OOO.O", "OO..OO", "OO.OOO", "O..OOO",                                          # u-z and w
        "......",                                                                                             # space
        ".O.....", ".O.O...", ".OO....", ".OO.O..", ".O..O..", ".OOO...", ".OOOO..", ".O.OO..", "..OO...", "..OOO.."  # 1-0
    ]

    ENGLISH = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",  
        "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",  
        "u", "v", "w", "x", "y", "z",                      
        " ",                                                
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"   
    ]

    CAPITAL_BRAILLE = ".....O"
    NUMBER_BRAILLE = ".O.OOO"

    
    def translate_to_braille(input_string):
        result = []
        is_number = False

        for c in input_string:
            if c.isupper():
                result.append(BrailleTranslator.CAPITAL_BRAILLE)
                c = c.lower()

            if c.isdigit():
                if not is_number:
                    result.append(BrailleTranslator.NUMBER_BRAILLE)
                    is_number = True
                result.append(BrailleTranslator.BRAILLE[int(c) + 25])
            else:
                if c == ' ':
                    is_number = False
                result.append(BrailleTranslator.BRAILLE[BrailleTranslator.ENGLISH.index(c)])

        return ''.join(result)


    def translate_to_english(input_braille):
        result = []
        is_capital = False
        is_number = False

        for i in range(0, len(input_braille), 6):
            braille_char = input_braille[i:i+6]

            if braille_char == BrailleTranslator.CAPITAL_BRAILLE:
                is_capital = True
            elif braille_char == BrailleTranslator.NUMBER_BRAILLE:
                is_number = True
            else:
                index = BrailleTranslator.BRAILLE.index(braille_char)
                letter = BrailleTranslator.ENGLISH[index]

                if is_capital:
                    letter = letter.upper()
                    is_capital = False

                result.append(letter)
                if letter == ' ':
                    is_number = False

        return ''.join(result)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_text = ' '.join(sys.argv[1:])  
        if all(c in "O." for c in input_text):
            print(BrailleTranslator.translate_to_english(input_text))
        else:
            print(BrailleTranslator.translate_to_braille(input_text))
    else:
        print("No input provided. Usage: python xyz.py <Your input>")
