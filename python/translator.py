import sys

numbers = '1234567890'
letters = 'abcdefghijklmnopqrstuvwxyz'
braille_chars = 'O.'

eng_to_brai = {
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
  '1': 'O.....',
  '2': 'O.O...',
  '3': 'OO....',
  '4': 'OO.O..',
  '5': 'O..O..',
  '6': 'OOO...',
  '7': 'OOOO..',
  '8': 'O.OO..',
  '9': '.OO...',
  '0': '.OOO..',
  ' ': '......',
  'capital': '.....O',
  'decimal': '.O....O',
  'number': '.O.OOO'
}

brai_to_eng = {
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
    '......': ' ',
    '.....O': 'capital',
    '.O.OOO': 'number'
}

num_to_letter = {
    '1': 'a',
    '2': 'b',
    '3': 'c',
    '4': 'd',
    '5': 'e',
    '6': 'f',
    '7': 'g',
    '8': 'h',
    '9': 'i',
    '0': 'j'
}

letter_to_num = {
    'a': '1',
    'b': '2',
    'c': '3',
    'd': '4',
    'e': '5',
    'f': '6',
    'g': '7',
    'h': '8',
    'i': '9',
    'j': '0'
}

def split_into_chunks(s: str, chunk_size: int) -> list:
  return [s[i:i + chunk_size] for i in range(0, len(s), chunk_size)]

def is_valid_braille(words: list) -> bool:
  return all(word in brai_to_eng for word in words)

def convert_to_english(chunks: list) -> str:
    #whats our approach?
    #for any regular letter or number, add it to the result string 
    #for capitals, have a bool, set it to true for a capital, then for the next letter, if capital is true, set it to capital and set it to false
    #for numbers, have a bool as well, set it to true when coming across that, then have a case where if it is true and there is a space, turn it to false
    result = ''
    isCapital = False
    isNumber = False
    for chunk in chunks:
        english = brai_to_eng[chunk]
        if english == 'capital':
            isCapital = True
        elif english == 'number':
            isNumber = True
        elif isCapital == True and english in letters:
            result += english.upper()
            isCapital = False
        elif english == ' ':
            result += english
            isNumber = False
        elif isNumber == True:
            result += letter_to_num[english]
        else:
            result += english
            if isNumber == True and english == ' ':
                isNumber = False
    return result
            
def convert_to_braille(string: str) -> str:
    result = ''
    isNumber = False
    #two things we have to watch out for uppercase letters and numbers
    #for uppercase letters, we can check each char to see, using isupper(), if so, we add the capital, and eng_to_brai[char.lower()]
    #for numbers, we check if its the first, 
    #for the number, we can assume it is solely a number until the space, we have two cases
    # isNumber bool is false and it is a number, thus we add the number braille before adding the actual number
    # isNUmber bool is true and it is a number, thus we just add the number 
    for letter in string:
        if letter.isalpha() or letter == ' ':
            if letter.isupper():
                result += eng_to_brai['capital']
            result += eng_to_brai[letter.lower()]
            isNumber = False
        else:
            if isNumber == False:
                isNumber = True
                result += eng_to_brai['number']
            result += eng_to_brai[letter]
    return result
    

def translate(string :str):
  #check string length and if it only contains O's and .'s
  if len(string)%6 == 0 and all(char in braille_chars for char in string) and is_valid_braille(split_into_chunks(string, 6)):
    print(convert_to_english(split_into_chunks(string, 6)))
  else:
    print(convert_to_braille(string))
    
    
if len(sys.argv) > 1:
    translate(' '.join(sys.argv[1:]))
else:
    translate(input())
