import sys
brailleAlphaNum = {'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
                    'e': 'O..O..', 'f': 'OOO...','g': 'OOOO..', 'h': 'O.OO..',
                    'i': '.OO...','j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
                    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.','p': 'OOO.O.',
                    'q': 'OOOOO.', 'r': 'O.OOO.','s': '.OO.O.', 't': '.OOOO.',
                    'u': 'O...OO','v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
                    'y': 'OO.OOO', 'z': 'O..OOO', '1': 'O.....', '2': 'O.O...',
                    '3': 'OO....','4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
                    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
                    'capitalFollows': '.....O','numberFollows': '.O.OOO', 'space': '......'}

englishAlpha = {}
englishNum = {}

for key, value in brailleAlphaNum.items():
    if key.isdigit():
        englishNum[value] = key
    elif key.isalpha():
        englishAlpha[value] = key

def brailleToEnglish(text: str) -> str:
    capitalFollows = False
    numberFollows = False
    res = []
    i = 0
    
    while i < len(text):
        brailleText = text[i:i+6]
        i += 6
        
        if brailleText == brailleAlphaNum['capitalFollows']:
            capitalFollows = True
        elif brailleText == brailleAlphaNum['numberFollows']:
            numberFollows = True
        elif brailleText == brailleAlphaNum['space']:
            res.append(' ')
            numberFollows = False
        else:
            if brailleText in englishAlpha and numberFollows == False:
                char = englishAlpha[brailleText]
                if capitalFollows:
                    res.append(char.upper())
                    capitalFollows = False
                else:
                    res.append(char)
            elif brailleText in englishNum and numberFollows == True:
                char = englishNum[brailleText] 
                if numberFollows:
                    res.append(char)
                else:
                    res.append(char)
    
    return ''.join(res)


def englishToBraille(text: str) -> str:
    res = []
    number = False
    
    for char in text:
        if char.isalpha():
            if char.isupper():
                res.append(brailleAlphaNum['capitalFollows'])
                char = char.lower()
            res.append(brailleAlphaNum[char])
        elif char.isdigit():
            if number == False:
                res.append(brailleAlphaNum['numberFollows'])
                number = True
            res.append(brailleAlphaNum[char])
        elif char == ' ':
            res.append(brailleAlphaNum['space'])
            number = False
    
    return ''.join(res)


def brailleOrEnglish(text: str) -> str:
    if all(char in {'O', '.'} for char in text):
        return brailleToEnglish(text)
    return englishToBraille(text)

def main():
    if len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
        print(brailleOrEnglish(text))
    else:
        print("Please provide input text.")

if __name__ == "__main__":
    main()
