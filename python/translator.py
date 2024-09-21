import sys

# eniglish to braille hashmap
brailleMap = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......','capital': '.....O', 'number': '.O.OOO',
    '0': '.OOOO.', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..','5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
}

# reverse mapping from Braille back to letters
brailleToCharMap = {x: y for y, x in brailleMap.items() if y not in ['capital', 'number']}

def englishToBraille(plain_text):
    brailleText = ''
    number_flag = False

    for char in plain_text:
        if char.isupper():
            brailleText += brailleMap['capital']
            brailleText += brailleMap[char.lower()]
        elif char.isdigit():
            if not number_flag:
                brailleText += brailleMap['number']
                number_flag = True
            brailleText += brailleMap[char]
        else:
            if number_flag:
                number_flag = False
            brailleText += brailleMap.get(char, '')
    return brailleText


def brailleToEnglish(inputBraille):
    chars = brailleLetters(inputBraille)
    englishText = ''
    index = 0
    captial_flag = False
    number_flag = False

    while index < len(chars):
        brailleChar = chars[index]
        if brailleChar == brailleMap['capital']:
            captial_flag = True
            index += 1
            continue
        elif brailleChar == brailleMap['number']:
            number_flag = True
            index += 1
            continue

        char = brailleToCharMap.get(brailleChar, '')
        if number_flag:
            if char.isdigit():
                englishText += char
            else:
                number_flag = False
                englishText += char
        else:
            if captial_flag:
                englishText += char.upper()
                captial_flag = False
            else:
                englishText += char
        index += 1
    return englishText

def brailleOrEnglish(z): #if braille this returns true
    return all(w in 'O.' for w in z)

def brailleLetters(j):#splits up braille 
    return [j[i:i + 6] for i in range(0, len(j), 6)]

def main():
    inputText = ' '.join(sys.argv[1:])
    if brailleOrEnglish(input.replace(' ', '')):
        print(brailleToEnglish(inputText))
    else:
        print(englishToBraille(inputText))

if __name__ == '__main__':
    main()
