#Dictionary for braille to numbers
numbers = {
'O.....': '1',
'O.O...': '2',
'OO....': '3',
'OO.O..': '4',
'O..O..': '5',
'OOO...': '6',
'OOOO..': '7',
'O.OO..': '8',
'.OO...': '9',
'.OOO..': '0',
}

#Dictionary for braille to english
braille = {
'O.....': 'a',
'O.O...': 'b',
'OO....': 'c',
'OO.O..': 'd',
'O..O..': 'e',
'OOO...': 'f',
'OOOO..': 'g',
'O.OO..': 'h',
'.OO...': 'i',
'.OOO..': 'j',
'O...O.': 'k',
'O.O.O.': 'l',
'OO..O.': 'm',
'OO.OO.': 'n',
'O..OO.': 'o',
'OOO.O.': 'p',
'OOOOO.': 'q',
'O.OOO.': 'r',
'.OO.O.': 's',
'.OOOO.': 't',
'O...OO': 'u',
'O.O.OO': 'v',
'.OOO.O': 'w',
'OO..OO': 'x',
'OO.OOO': 'y',
'O..OOO': 'z',
'..OO.O': '.',
'..O...': ',',
'..O.OO': '?',
'..OOO.': '!',
'..OO..': ':',
'..O.O.': ';',
'....OO': '-',
'.O..O.': '/',
'.OO..O': '<',
#'O' has the same translation as '>'
#'O..OO.': '>',
'O.O..O': '(',
'.O.OO.': ')',
'......': ' ',
}

def get_key_braille(val) -> str:
    #Given a value, return the corresponding key from the braille dictionary
    for key, value in braille.items():
        if val == value:
            return key
    return "key doesn't exist"

def get_key_numbers(val) -> str:
    #Given a value, return the corresponding key from the numbers dictionary
    for key, value in numbers.items():
        if val == value:
            return key
    return "key doesn't exist"

def check(input) -> bool:
    #Check if the given string is braille or english
    if len(input) % 6 != 0:
        #all braille is divisible by 6
        return True #English
    for i in range(len(input)):
        if input[i] != 'O' and input[i] != '.':
            return True #English
        if i == 6:
            #if a regular character hasn't been found in the first 6 characters, it must be braille
            break
    return False #Braille

def translateToBraille(s) -> str:
    translation = []
    numberFlag = False
    for letter in s:
        if letter.isupper():
            translation.append(".....O") #uppercase follows
            letter = letter.lower()
        if letter == " ":
            translation.append("......") #space
            numberFlag = False
            continue
        if letter.isnumeric():
            if numberFlag == False:
                translation.append(".O.OOO") #number follows
                numberFlag = True
            translation.append(get_key_numbers(letter))
        else:
            if numberFlag:
                translation.append(".O...O") #decimal follows
                continue
            translation.append(get_key_braille(letter))
    return ''.join(translation)
        
def translateToEnglish(s) -> str:
    english = []
    upperFlag = False
    numberFlag = False
    for i in range(0,len(s),6):
        letter = s[i:i+6] #seperate braille by each letter (6 characters)
        if letter == ".....O": #uppercase follows
            upperFlag = True
            continue
        if letter == ".O.OOO": #number follows
            numberFlag = True
            continue
        if letter == "......": #numbers end when a space is identified
            numberFlag = False
        if upperFlag == True:
            english.append((braille.get(letter)).upper())
            upperFlag = False
        elif numberFlag:
            if letter == ".O...O": #decimal follows
                english.append('.')
                continue
            english.append(numbers.get(letter))
        else:
            english.append(braille.get(letter))
    return ''.join(english)

def main(input):
    if check(input):
        print(translateToBraille(input))
    else:
        print(translateToEnglish(input))

if __name__ == '__main__':
    main()