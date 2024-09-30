
import sys, re

BRAILLE_TO_ENG_MAP =   {
                'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd',
                'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h',
                '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l',
                'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p',
                'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
                'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x',
                'OO.OOO': 'y', 'O..OOO': 'z'
                }
ENG_TO_BRAILLE_MAP = {value: key for key, value in BRAILLE_TO_ENG_MAP.items()}

BRAILLE_TO_NUM_MAP =    {
                'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 
                'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8',
                '.OO...': '9', '.OOO..': '0'
                }
NUM_TO_BRAILLE_MAP = {value: key for key, value in BRAILLE_TO_NUM_MAP.items()}

BRAILLE_TO_SPEC_MAP = {'.....O': 'CAP', '.O.OOO' : 'NUM', '......' : 'SPACE'}
SPEC_TO_BRAILLE_MAP = {value: key for key, value in BRAILLE_TO_SPEC_MAP.items()}

def english_to_braille(text):
    '''
    Function to convert English text to Braille
    '''
    output = []
    # flag to see if we're currently reading numbers
    numFlag = False

    for char in text:
        # if char is uppercase, add the CAP braille character and convert to lowercase
        if char.isupper():
            output.append(SPEC_TO_BRAILLE_MAP['CAP'])
            char = char.lower()
        # if char is a digit and we're not currently reading numbers, add the NUM braille character & set numFlag to True
        elif char.isdigit() and not numFlag:
            output.append(SPEC_TO_BRAILLE_MAP['NUM'])
            numFlag = True
        # if char is a space, add the SPACE braille character and set numFlag to False
        elif char == ' ':
            output.append(SPEC_TO_BRAILLE_MAP['SPACE'])
            numFlag = False
            continue

        # if we're not reading numbers, add the braille character for the char
        if char in ENG_TO_BRAILLE_MAP and not numFlag:
            output.append(ENG_TO_BRAILLE_MAP[char])
        # if we're reading numbers, add the braille character for the digit
        elif char in NUM_TO_BRAILLE_MAP:
            output.append(NUM_TO_BRAILLE_MAP[char])
        else:
            # if char not in any map, throw error
            print(f"Invalid character: {char}")
            sys.exit(1)

    return "".join(output)

def braille_to_english(text):
    output = []
    # flags to see if we're currently reading numbers or uppercase characters
    numFlag = False
    capFlag = False

    # read 6 characters at a time as our mapping of braille characters to english characters is 6:1
    for i in range(0, len(text), 6):
        # get the current 6 characters
        char = text[i:i+6]
        # if the current 6 characters are in the special map
        if char in BRAILLE_TO_SPEC_MAP:
            # if the current 6 characters are CAP, set capFlag to True
            if BRAILLE_TO_SPEC_MAP[char] == 'CAP':
                capFlag = True
                continue
            # if the current 6 characters are NUM, set numFlag to True
            elif BRAILLE_TO_SPEC_MAP[char] == 'NUM':
                numFlag = True
                continue
            # else, add a space and set numFlag to False
            else:
                output.append(' ')
                numFlag = False
                continue
            
        # if we're reading numbers and the current 6 characters are in the number map, add the corresponding number
        if numFlag and char in BRAILLE_TO_NUM_MAP:
            output.append(BRAILLE_TO_NUM_MAP[char])
        # if the current 6 characters are in the english map, add the corresponding character
        elif char in BRAILLE_TO_ENG_MAP:
            # if capFlag is True, add the uppercase character and set capFlag to False
            if capFlag:
                output.append(BRAILLE_TO_ENG_MAP[char].upper())
                capFlag = False
            # else, add the lowercase character
            else:
                output.append(BRAILLE_TO_ENG_MAP[char])
        else:
            # if the current 6 characters are not in any map, throw error
            print(f"Invalid character: {char}")
            sys.exit(1)

    return "".join(output)


def main():
    # check if input is provided correctly
    if len(sys.argv) < 2:
        print("Invalid Input. Usage: python translator.py <input>")
        sys.exit(1)

    # get the input text
    input_text = " ".join(sys.argv[1:])
    
    # regex to check if the input is in braille format (only has . & O characters)
    pattern = r'^[.O]+$'
    if len(input_text) % 6 == 0 and re.match(pattern, input_text):
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))


if __name__ == "__main__":
    main()