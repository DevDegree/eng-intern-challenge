import sys

#assuming that the input is only braille or only a string
#assuming that braille input is only a single string
#assuming that english input is a list of strings

CAPITAL_NEXT = ".....O"
NUMBER_NEXT = ".O.OOO"
SPACE = "......"

#dict to convert from english to braille
english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 
    'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 
    'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......'
}

#mapping from braille to english
braille_to_english = {x : y for y, x in english_to_braille.items()}

# Dict to map numbers to Braille representations
numbers_to_braille = {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
}

# Mapping from braille to numbers
braille_to_numbers = {x : y for y, x in numbers_to_braille.items()}

def isBraille(text):
    #assume that braille is only inputted as single string
    if len(text) > 1:
        return False
    #can only contain "." and "O"
    if len(text) == 1:
        for char in text[0]:
            if char not in (".", "O"):
                print("not in")
                return False
        return True
    return False

def convert_to_english(braille):
    #convert braille to english
    #use a sliding window of 6 characters to get the english character
    res = []
    left = 0
    capital = False
    number = False
    for i in range(6, len(braille) + 1, 6):
        char = braille[left:i]
        if char == CAPITAL_NEXT:
            capital = True
        elif char == NUMBER_NEXT:
            number = True
        elif char == SPACE:
            res.append(" ")
            number = False
        elif number:
                res.append(braille_to_numbers[char])
        elif char in braille_to_english:
            if capital:
                res.append(braille_to_english[char].upper())
                capital = False
            else:
                res.append(braille_to_english[char])
        else:
            raise Exception("Invalid Braille character: ", char)
            
        left = i
    return "".join(res)

def convert_to_braille(texts):
    #convert english to braille
    res = []
    for text in texts:
        number = False
        currStr = []
        english = text
        for char in english:
            if char == " ":
                number = False
            if char.isupper():
                #if the character is a capital letter, add the CAPITAL_NEXT character
                currStr.append(CAPITAL_NEXT)
                char = char.lower()
                currStr.append(english_to_braille[char])
            elif char.isdigit():
                #if the character is a number add the NUMBER_NEXT character
                if not number:
                    currStr.append(NUMBER_NEXT)
                    number = True
                currStr.append(numbers_to_braille[char])
            else:
                currStr.append(english_to_braille[char])
        res.append("".join(currStr))
    return SPACE.join(res)



def main():
    text = sys.argv[1:]
    if isBraille(text):
        print(convert_to_english(text[0]))
    else:
        print(convert_to_braille(text))

if __name__ == "__main__":
    main()