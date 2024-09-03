import sys
import AlphabetToBraille
import BrailleToAlphabet
import re

CAPITAL = '.....O'
DECIMAL = '.O...O'
NUMBER = '.O.OOO'
SPACER = '......'

argList = sys.argv[1:]

def alphabet_to_braille(input):
    
    result = ""
    for i in range(len(input)):

        if input[i] in AlphabetToBraille.numbers and not input[i-1] in AlphabetToBraille.numbers:
            result += SPACER + NUMBER + AlphabetToBraille.numbers.get(input[i])

        elif input[i] in AlphabetToBraille.numbers and input[i-1] in AlphabetToBraille.numbers:
            result += AlphabetToBraille.numbers.get(input[i])

        elif input[i].lower() in AlphabetToBraille.letters and input[i].isupper() and input[i-1] in AlphabetToBraille.numbers:
            result += SPACER + CAPITAL + AlphabetToBraille.letters.get(input[i].lower())

        elif input[i].lower() in AlphabetToBraille.letters and input[i].isupper():
            result += CAPITAL + AlphabetToBraille.letters.get(input[i].lower())

        elif input[i] in AlphabetToBraille.letters and input[i-1] in AlphabetToBraille.numbers:
            result += SPACER + AlphabetToBraille.letters.get(input[i])

        elif input[i] in AlphabetToBraille.letters:
            result += AlphabetToBraille.letters.get(input[i])

        elif input[i] in AlphabetToBraille.punctuation:

            if input[i] == '.' and input[i-1].isdigit() and input[i+1].isdigit():
                result += DECIMAL + AlphabetToBraille.punctuation.get(input[i])

            else:
                result += AlphabetToBraille.punctuation.get(input[i])

        else:
            continue

    return result
    
def braille_to_alphabet(input):

    nospace = input.replace(" ", "")
    trim = nospace.strip()
    braille = re.findall('......',trim)

    result = ""

    for i in range(len(braille)):
        if braille[i] == CAPITAL:
            continue
        elif braille[i] == NUMBER:
            continue
        elif braille[i] == DECIMAL:
            continue
        elif braille[i] in BrailleToAlphabet.letters and braille[i-1] == CAPITAL:
            result += BrailleToAlphabet.letters.get(braille[i]).upper() 
        elif braille[i] in BrailleToAlphabet.letters and braille[i-1] != NUMBER:
            result += BrailleToAlphabet.letters.get(braille[i])
        elif braille[i] in BrailleToAlphabet.numbers and braille[i-1] == NUMBER:
            result += BrailleToAlphabet.numbers.get(braille[i])
        elif braille[i] in BrailleToAlphabet.punctuation:
            result += BrailleToAlphabet.punctuation.get(braille[i])
        else:
            continue
    return result
        
def run(input):

    trim = input.strip()
    check = trim[:6]

    if check in BrailleToAlphabet.letters or check in BrailleToAlphabet.numbers or check in BrailleToAlphabet.punctuation or check == CAPITAL or check == NUMBER or check == DECIMAL:
        return braille_to_alphabet(input)
    else:
        return alphabet_to_braille(input)

if __name__ == '__main__':
    input = ''.join(argList)
    print(run(input))







