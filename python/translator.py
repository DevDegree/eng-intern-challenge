import sys

dic = {
    'O.....': ["a", 'A', "1"],
    'O.O...': ["b", 'B', "2"],
    'OO....': ["c", 'C', "3"],
    'OO.O..': ["d", 'D', "4"],
    'O..O..': ["e", 'E', "5"],
    'OOO...': ["f", 'F', "6"],
    'OOOO..': ["g", 'G', "7"],
    'O.OO..': ["h", 'H', "8"],
    '.OO...': ["i", 'I', "9"],
    '.OOO..': ["j", 'J', "O"],
    'O...O.': ["k", 'K'],
    'O.O.O.': ["l", 'L'],
    'OO..O.': ["m", 'M'],
    'OO.OO.': ["n", 'N'],
    'O..OO.': ["o", 'O'],
    'OOO.O.': ["p", 'P'],
    'OOOOO.': ["q", 'Q'],
    'O.OOO.': ["r", 'R'],
    '.OO.O.': ["s", 'S'],
    '.OOOO.': ["t", 'T'],
    'O...OO': ["u", 'U'],
    'O.O.OO': ["v", 'V'],
    '.OOO.O': ["w", 'W'],
    'OO..OO': ["x", 'X'],
    'OO.OOO': ["y", 'Y'],
    'O..OOO': ["z", 'Z'],
    '......': [' '],
}
# Function to translate Braille to english and vice versa
def translator(inp):
    capital = '.....O'
    number = ".O.OOO"
    word = ""
    word_list = []
    isStillNumber = False
    isBrialle = False
    whichSpecial = 0
    # detecting braille or english and splitting
    if ("." in inp[0]):
        isBrialle = True
        for i in range(0, len(inp), 6):
            sep = inp[i:i+6]
            word_list.append(sep)
    else:
        word_list = list(inp)
    # conditionally runs based off if enlish or braille
    if (not isBrialle):
        for i in range(0, len(word_list), 1):#loop through the english letters
            if (word_list[i].isupper()):
                word += capital
            elif (word_list[i].isdigit() and not isStillNumber):
                isStillNumber = True
                word += number
            elif (word_list[i] == ' '):
                isStillNumber = False

            word += ''.join(key for key, values in dic.items() if word_list[i] in values)
    else:
        for i in range(0, len(word_list), 1):#loop through braille letters
            if (word_list[i] == capital):
                whichSpecial = 1
                continue
            elif (word_list[i] == number):
                whichSpecial = 2
                continue
            elif (dic[word_list[i]] == ' '):
                whichSpecial = 0

            word += dic[word_list[i]][whichSpecial]
            whichSpecial = 0 if whichSpecial == 1 else whichSpecial
    return word #returns the translated word


if __name__ == '__main__':
    input_args = sys.argv[1:]  

    input_string = " ".join(input_args)
    print(translator(input_string))