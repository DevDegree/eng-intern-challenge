import sys

# dictionary used to translate letters and numbers to brail
letNumDict = {
    'a':'O.....',
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
    'A': '.....OO.....',
    'B': '.....OO.O...',
    'C': '.....OOO....',
    'D': '.....OOO.O..',
    'E': '.....OO..O..',
    'F': '.....OOOO...',
    'G': '.....OOOOO..',
    'H': '.....OO.OO..',
    'I': '.....O.OO...',
    'J': '.....O.OOO..',
    'K': '.....OO...O.',
    'L': '.....OO.O.O.',
    'M': '.....OOO..O.',
    'N': '.....OOO.OO.',
    'O': '.....OO..OO.',
    'P': '.....OOOO.O.',
    'Q': '.....OOOOOO.',
    'R': '.....OO.OOO.',
    'S': '.....O.OO.O.',
    'T': '.....O.OOOO.',
    'U': '.....OO...OO',
    'V': '.....OO.O.OO',
    'W': '.....O.OOO.O',
    'X': '.....OOO..OO',
    'Y': '.....OOO.OOO',
    'Z': '.....OO..OOO',
    '.' : '..OO.O',
    ',' : '..O...',
    '?' : '..O.OO',
    '!' : '..OOO.',
    ':' : '..OO..',
    ';' : '..O.O.',
    '-' : '....OO',
    '/' : '.O..O.',
    '<' : '.OO..O',
    '>' : 'O..OO.',
    '(' : 'O.O..O',
    ')' : '.O.OO.'
}


brailleDict = {letNumDict[k]: k for k in letNumDict.keys() if not k.isdigit()}
brailleNumDict = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0'
}

def isBraille(text): 
    return text.count("O") + text.count(".") == len(text)


def main():
    if len(sys.argv) > 1:
        input = ' '.join(sys.argv[1:])
        output = ""
        if isBraille(input):
            i = 0
            while i + 6 <= len(input):
                #Check the first 6 letters for special input
                letter = input[i:i + 6]
                print(input)
                print("Checking: " + letter)
                if letter == '.....O':  #Capital Letter, just consume the next 12 characters
                    output += brailleDict[input[i:i + 12]]
                    i += 12
                elif letter == '.O.OOO': #Number. skip the 6, and go record all the following numbers intil the next space
                    i += 6
                    while input[i:i + 6] != '......' and i + 6 <= len(input):
                        if input[i:i + 6] == '.O...O': #This just checks for a decimal point, skips it, and continues recording numbers
                             output += '.'
                             i += 6
                        else:
                            output += brailleNumDict[input[i:i + 6]] #record number using brailNumDict Dictionary
                            # print("added " + input[i:i + 6] + ",   into: " + brailleNumDict[input[i:i + 6]])
                            # print('output: ' + output)
                            # print('input: ' + input)
                            # print("i: "+ str(i))
                            # print("letter: " + input[i:i + 6])
                            i += 6  
                else:   #Just recording regular lowcase letter
                    output += brailleDict[letter]
                    i += 6
                print(output)
        else:
            inputs = input.split(' ')
            i = 0
            while i < len(inputs):
                if inputs[i][0].isdigit(): #Recording a number
                   digit = 0
                   output += '.O.OOO' #symbol to show in braile that a number is following
                   while digit < len(inputs[i]):
                       if inputs[i][digit] == '.':
                           output += '.O...O' #shows that the rest of the follwing numbers are decimals
                       else:
                           output += letNumDict[inputs[i][digit]]
                       digit += 1
                   if i < len(inputs) - 1:
                        output += '......'
                else: #Or recording a letter
                    letter = 0
                    while(letter < len(inputs[i])):
                        output += letNumDict[inputs[i][letter]]
                        letter += 1
                    if i < len(inputs) - 1:
                        output += '......'
                i +=1
        print(output)
    else:
        print("empty input")

if __name__ == "__main__":
    main()