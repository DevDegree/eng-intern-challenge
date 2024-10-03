import sys



braille_to_english_letters = {
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
    '.O.OOO' : 'number'
}


braille_to_english_numbers = {
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
    '......': ' '
}



english_to_braille_dict = {
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
    'capital': '.....O',
    'number': '.O.OOO'
}


def braille_to_english(word):
    english_word = ""
    i = 0
    while (i+1)*6 <= len(word):
        if braille_to_english_letters[word[i*6: (i+1)*6]] == "capital":
            i+=1
            if (i+1)*6 > len(word):
                break
            english_word += braille_to_english_letters[word[i*6: (i+1)*6]].upper()
        elif braille_to_english_letters[word[i*6: (i+1)*6]] == "number":
            i += 1
            while (i+1)*6 <= len(word) and braille_to_english_numbers[word[i*6: (i+1)*6]] != " ":
                english_word += braille_to_english_numbers[word[i*6: (i+1)*6]]
                i += 1
            if (i+1)*6 <= len(word):
                english_word += " "
        else:
            english_word += braille_to_english_letters[word[i*6: (i+1)*6]]
        i += 1
    return english_word


def english_to_braille(word):
    braille_word = ""
    i = 0
    number_flag = False
    while i < len(word):
        if word[i].isnumeric():
            if not number_flag: 
                braille_word += english_to_braille_dict["number"]
                number_flag = True
            braille_word += english_to_braille_dict[word[i]]
            
        elif word[i].isupper():
            if number_flag:
                number_flag = False
            braille_word += english_to_braille_dict["capital"]
            braille_word += english_to_braille_dict[word[i].lower()]
        else:
            if number_flag:
                number_flag = False
            braille_word += english_to_braille_dict[word[i]]
        i += 1
    return braille_word



        
words = sys.argv[1:]

input_words = " ".join(words)

if all((i in [".", "O"] for i in input_words )):
    print(braille_to_english(input_words))
else:
    print(english_to_braille(input_words))
