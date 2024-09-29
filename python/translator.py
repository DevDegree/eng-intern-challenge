import sys

translation_dictionary = {
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
    '.....O': 'upper',
    '......': ' ',
    '.O.OOO': 'toNum',
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO', 
    ' ': '......',
    'upper': '.....O',
    'toNum': '.O.OOO'
}

# Converts a given string from Braille to English
def brailleToEnglish(sentence: str) -> str:
    result = ""
    upper = False
    toNum = False
    for i in range(0, len(sentence), 6):
        braille_letter = sentence[i:i+6]
        if translation_dictionary[braille_letter] == 'upper':
            upper = True
        elif translation_dictionary[braille_letter] == 'toNum':
            toNum = True
        elif translation_dictionary[braille_letter] == ' ':
            result += ' '
            toNum = False
        elif upper:
            result += translation_dictionary[braille_letter].upper()
            upper = False
        elif toNum:
            result += str(ord(translation_dictionary[braille_letter]) - ord('a') + 1)
        else:
            result += translation_dictionary[braille_letter]
    return result

# Converts a given string from English to Braille
# if it is the last string in the input, a space character is ommitted from the end
def englishToBraille(sentence: str, last: bool) -> str:
    result = ""
    toNum = False
    for i in range(len(sentence)):
            letter = sentence[i]
            if letter in '1234567890':
                if not toNum:
                    result += translation_dictionary['toNum']
                    toNum = True
                result += translation_dictionary[chr(ord(letter) - ord('0') + ord('a') - 1)]
            elif letter not in translation_dictionary and letter.lower() in translation_dictionary:
                result += translation_dictionary['upper']
                result += translation_dictionary[letter.lower()]
            else:
                result += translation_dictionary[letter]
    if last:
        return result
    return result + translation_dictionary[' ']

# Determines whether the input string is in Braille or English, and translates the string
# into the other language
def translateSentence(input_sentence: str, last: bool) -> str:
    if '.' in input_sentence:
        return brailleToEnglish(input_sentence)
    else:
        return englishToBraille(input_sentence, last)

# Separates the input into separate strings, main function of the program
def translate():
    inputArray = sys.argv[1:]
    translation = ''
    for i, w in enumerate(inputArray):
        if i == len(inputArray) - 1:
            translation += translateSentence(w, True)
        else:
            translation += translateSentence(w, False)
    print(translation)


        

if __name__ == '__main__':
    translate()
