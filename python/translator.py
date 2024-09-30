### Divjot Bhogal
### 2024-09-30
### Braille Translator - Shopify Intern Challenge
## Detects whether input is English or Braille, then converts it into opposite language

class Braille:
    def __init__(self):
        self.board = []
        self.capital = False
        self.number = False
        self.decimal = False
        for i in range(3):
            self.board.append(['.', '.'])

    def setBoard(self):
        braille_input = input()
        counter = 0
        isAlphabet = False
        for i in range(len(braille_input)):
            if (braille_input[i] != '.' and braille_input[i] != 'O'):
                isAlphabet = True
                break
        if (isAlphabet == False):
            while(counter != len(braille_input)):
                for i in range(3):
                    for j in range(2):
                        self.board[i][j] = braille_input[counter]
                        counter += 1
                self.readBoard()
        else:
            self.writeBoard(braille_input)

    def writeBoard(self, braille_input):
        for x in braille_input:
            if (x.isupper()):
                print('.....O', end = "")
            if (x.isnumeric() and not(self.number)):
                print('.O.OOO', end = "")
                self.number = True
            if (x == '.' or x == ',' or x == '!' or x == '?' or x == '-' or x == ':' or x == ';' or x == '(' or x == ')' or x == '<' or x == ">"):
                print('.O...O')     # Doesn't specify if decimals are until end of space or only next symbol
                                    # Assuming it is only next symbol
            if(x == 'A' or x == 'a'):
                print('O.....', end = "")
            elif(x == 'B' or x == 'b'):
                print('O.O...', end = "")
            elif(x == 'C' or x == 'c'):
                print('OO....', end = "")
            elif(x == 'D' or x == 'd'):
                print('OO.O..', end = "")
            elif(x == 'E' or x == 'e'):
                print('O..O..', end = "")
            elif(x == 'F' or x == 'f'):
                print('OOO...', end = "")
            elif(x == 'G' or x == 'g'):
                print('OOOO..', end = "")
            elif(x == 'H' or x == 'h'):
                print('O.OO..', end = "")
            elif(x == 'I' or x == 'i'):
                print('.OO...', end = "")
            elif(x == 'J' or x == 'j'):
                print('.OOO..', end = "")
            elif(x == 'K' or x == 'k'):
                print('O...O.', end = "")
            elif(x == 'L' or x == 'l'):
                print('O.O.O.', end = "")
            elif(x == 'M' or x == 'm'):
                print('OO..O.', end = "")
            elif(x == 'N' or x == 'n'):
                print('OO.OO.', end = "")
            elif(x == 'O' or x == 'o'):
                print('O..OO.', end = "")
            elif(x == 'P' or x == 'p'):
                print('OOO.O.', end = "")
            elif(x == 'Q' or x == 'q'):
                print('OOOOO.', end = "")
            elif(x == 'R' or x == 'r'):
                print('O.OOO.', end = "")
            elif(x == 'S' or x == 's'):
                print('.OO.O.', end = "")
            elif(x == 'T' or x == 't'):
                print('.OOOO.', end = "")
            elif(x == 'U' or x == 'u'):
                print('O...OO', end = "")
            elif(x == 'V' or x == 'v'):
                print('O.O.OO', end = "")
            elif(x == 'W' or x == 'w'):
                print('.OOO.O', end = "")
            elif(x == 'X' or x == 'x'):
                print('OO..OO', end = "")
            elif(x == 'Y' or x == 'y'):
                print('OO.OOO', end = "")
            elif(x == 'Z' or x == 'z'):
                print('O..OOO', end = "")
            elif(x == '0'):
                print('.OOO..', end = "")
            elif(x == '1'):
                print('O.....', end = "")
            elif(x == '2'):
                print('O.O...', end = "")
            elif(x == '3'):
                print('OO....', end = "")
            elif(x == '4'):
                print('OO.O..', end = "")
            elif(x == '5'):
                print('O..O..', end = "")
            elif(x == '6'):
                print('OOO...', end = "")
            elif(x == '7'):
                print('OOOO..', end = "")
            elif(x == '8'):
                print('O.OO..', end = "")
            elif(x == '9'):
                print('.OO...', end = "")
            elif(x == ' '):
                print('......', end = "")
                self.number = False
            elif(x == '!'):
                print('..OOO.', end = "")
            elif(x == '?'):
                print('.O..OO', end = "")
            elif(x == ':'):
                print('..OO..', end = "")
            elif(x == ';'):
                print('..O.O.', end = "")
            elif(x == '-'):
                print('....OO', end = "")
            elif(x == '/'):
                print('O....O', end = "")
            elif(x == '>'):
                print('O..OO.', end = "")
            elif(x == '<'):
                print('.OO..O', end = "")
            
    def readBoard(self):
        if (self.board == [['.', '.',], ['.', '.',], ['.', 'O']]):
            self.capital = True
        elif (self.board == [['.', 'O',], ['.', 'O'], ['O', 'O']]):
            self.number = True
        elif (self.board == [['.', 'O',], ['.', '.',], ['.', 'O']]):
            self.decimal = True
        elif (self.board == [['.', '.'], ['.', '.'], ['.', '.']]):
            print(' ', end = "")
        elif (self.board == [['O', '.',], ['.', '.',], ['.', '.']] and self.capital == True and self.number == False and self.decimal == False):
            print('A', end = "")
            self.capital = False
        elif (self.board == [['O', '.'], ['O', '.',], ['.', '.']] and self.capital == True and self.number == False and self.decimal == False):
            print('B', end = "")
            self.capital = False
        elif (self.board == [['O', 'O'], ['.', '.'], ['.', '.']] and self.capital == True and self.number == False and self.decimal == False):
            print('C', end = "")
            self.capital = False
        elif (self.board == [['O', 'O'], ['.', 'O'], ['.', '.']] and self.capital == True and self.number == False and self.decimal == False):
            print('D', end = "")
            self.capital = False
        elif (self.board == [['O', '.'], ['.', 'O',], ['.', '.']] and self.capital == True and self.number == False and self.decimal == False):
            print('E', end = "")
            self.capital = False
        elif (self.board == [['O', 'O'], ['O', '.'], ['.', '.']] and self.capital == True and self.number == False and self.decimal == False):
            print('F', end = "")
            self.capital = False
        elif (self.board == [['O', 'O'], ['O', 'O'], ['.', '.']] and self.capital == True and self.number == False and self.decimal == False):
            print('G', end = "")
            self.capital = False
        elif (self.board == [['O', '.'], ['O', 'O'], ['.', '.']] and self.capital == True and self.number == False and self.decimal == False):
            print('H', end = "")
            self.capital = False
        elif (self.board == [['.', 'O'], ['O', '.'], ['.', '.']] and self.capital == True and self.number == False and self.decimal == False):
            print('I', end = "")
            self.capital = False
        elif (self.board == [['.', 'O'], ['O', 'O'], ['.', '.']] and self.capital == True and self.number == False and self.decimal == False):
            print('J', end = "")
            self.capital = False
        elif (self.board == [['O', '.'], ['.', '.',], ['O', '.']] and self.capital == True and self.number == False and self.decimal == False):
            print('K', end = "")
            self.capital = False
        elif (self.board == [['O', '.'], ['O', '.',], ['O', '.']] and self.capital == True and self.number == False and self.decimal == False):
            print('L', end = "")
            self.capital = False
        elif (self.board == [['O', 'O'], ['.', '.',], ['M', '.']] and self.capital == True and self.number == False and self.decimal == False):
            print('M', end = "")
            self.capital = False
        elif (self.board == [['O', 'O',], ['.', 'O'], ['O', '.']] and self.capital == True and self.number == False and self.decimal == False):
            print('N', end = "")
            self.capital = False
        elif (self.board == [['O', '.'], ['.', 'O',], ['O', '.']] and self.capital == True and self.number == False and self.decimal == False):
            print('O', end = "")
            self.capital = False
        elif (self.board == [['O', 'O'], ['O', '.'], ['O', '.']] and self.capital == True and self.number == False and self.decimal == False):
            print('P', end = "")
            self.capital = False
        elif (self.board == [['O', 'O'], ['O', 'O'], ['O', '.']] and self.capital == True and self.number == False and self.decimal == False):
            print('Q', end = "")
            self.capital = False
        elif (self.board == [['O', '.'], ['O', 'O'], ['O', '.']] and self.capital == True and self.number == False and self.decimal == False):
            print('R', end = "")
            self.capital = False
        elif (self.board == [['.', 'O'], ['O', '.'], ['O', '.']] and self.capital == True and self.number == False and self.decimal == False):
            print('S', end = "")
            self.capital = False
        elif (self.board == [['.', 'O'], ['O', 'O'], ['O', '.']] and self.capital == True and self.number == False and self.decimal == False):
            print('T', end = "")
            self.capital = False
        elif (self.board == [['O', '.'], ['.', '.'], ['O', 'O']] and self.capital == True and self.number == False and self.decimal == False):
            print('U', end = "")
            self.capital = False
        elif (self.board == [['O', '.'], ['O', '.'], ['O', 'O']] and self.capital == True and self.number == False and self.decimal == False):
            print('V', end = "")
            self.capital = False
        elif (self.board == [['.', 'O'], ['O', 'O'], ['.', 'O']] and self.capital == True and self.number == False and self.decimal == False):
            print('W', end = "")
            self.capital = False
        elif (self.board == [['O', 'O',], ['.', '.'], ['O', 'O']] and self.capital == True and self.number == False and self.decimal == False):
            print('X', end = "")
            self.capital = False
        elif (self.board == [['O', 'O',], ['.', 'O'], ['O', 'O']] and self.capital == True and self.number == False and self.decimal == False):
            print('Y', end = "")
            self.capital = False
        elif (self.board == [['O', '.'], ['.', 'O'], ['O', 'O']] and self.capital == True and self.number == False and self.decimal == False):
            print('Z', end = "")
            self.capital = False
        elif (self.board == [['O', '.',], ['.', '.',], ['.', '.']] and self.capital == False and self.number == False and self.decimal == False):
            print('a', end = "")
        elif (self.board == [['O', '.'], ['O', '.',], ['.', '.']] and self.capital == False and self.number == False and self.decimal == False):
            print('b', end = "")
        elif (self.board == [['O', 'O'], ['.', '.'], ['.', '.']] and self.capital == False and self.number == False and self.decimal == False):
            print('c', end = "")
        elif (self.board == [['O', 'O'], ['.', 'O'], ['.', '.']] and self.capital == False and self.number == False and self.decimal == False):
            print('d', end = "")
        elif (self.board == [['O', '.'], ['.', 'O',], ['.', '.']] and self.capital == False and self.number == False and self.decimal == False):
            print('e', end = "")
        elif (self.board == [['O', 'O'], ['O', '.'], ['.', '.']] and self.capital == False and self.number == False and self.decimal == False):
            print('f', end = "")
        elif (self.board == [['O', 'O'], ['O', 'O'], ['.', '.']] and self.capital == False and self.number == False and self.decimal == False):
            print('g', end = "")
        elif (self.board == [['O', '.'], ['O', 'O'], ['.', '.']] and self.capital == False and self.number == False and self.decimal == False):
            print('h', end = "")
        elif (self.board == [['.', 'O'], ['O', '.'], ['.', '.']] and self.capital == False and self.number == False and self.decimal == False):
            print('i', end = "")
        elif (self.board == [['.', 'O'], ['O', 'O'], ['.', '.']] and self.capital == False and self.number == False and self.decimal == False):
            print('j', end = "")
        elif (self.board == [['O', '.'], ['.', '.',], ['O', '.']] and self.capital == False and self.number == False and self.decimal == False):
            print('k', end = "")
        elif (self.board == [['O', '.'], ['O', '.',], ['O', '.']] and self.capital == False and self.number == False and self.decimal == False):
            print('l', end = "")
        elif (self.board == [['O', 'O'], ['.', '.',], ['M', '.']] and self.capital == False and self.number == False and self.decimal == False):
            print('m', end = "")
        elif (self.board == [['O', 'O',], ['.', 'O'], ['O', '.']] and self.capital == False and self.number == False and self.decimal == False):
            print('n', end = "")
        elif (self.board == [['O', '.'], ['.', 'O',], ['O', '.']] and self.capital == False and self.number == False and self.decimal == False):
            print('o', end = "")
        elif (self.board == [['O', 'O'], ['O', '.'], ['O', '.']] and self.capital == False and self.number == False and self.decimal == False):
            print('p', end = "")
        elif (self.board == [['O', 'O'], ['O', 'O'], ['O', '.']] and self.capital == False and self.number == False and self.decimal == False):
            print('q', end = "")
        elif (self.board == [['O', '.'], ['O', 'O'], ['O', '.']] and self.capital == False and self.number == False and self.decimal == False):
            print('r', end = "")
        elif (self.board == [['.', 'O'], ['O', '.'], ['O', '.']] and self.capital == False and self.number == False and self.decimal == False):
            print('s', end = "")
        elif (self.board == [['.', 'O'], ['O', 'O'], ['O', '.']] and self.capital == False and self.number == False and self.decimal == False):
            print('t', end = "")
        elif (self.board == [['O', '.'], ['.', '.'], ['O', 'O']] and self.capital == False and self.number == False and self.decimal == False):
            print('u', end = "")
        elif (self.board == [['O', '.'], ['O', '.'], ['O', 'O']] and self.capital == False and self.number == False and self.decimal == False):
            print('v', end = "")
        elif (self.board == [['.', 'O'], ['O', 'O'], ['.', 'O']] and self.capital == False and self.number == False and self.decimal == False):
            print('w', end = "")
        elif (self.board == [['O', 'O',], ['.', '.'], ['O', 'O']] and self.capital == False and self.number == False and self.decimal == False):
            print('x', end = "")
        elif (self.board == [['O', 'O',], ['.', 'O'], ['O', 'O']] and self.capital == False and self.number == False and self.decimal == False):
            print('y', end = "")
        elif (self.board == [['O', '.'], ['.', 'O'], ['O', 'O']] and self.capital == False and self.number == False and self.decimal == False):
            print('z', end = "")
        elif (self.board == [['O', '.',], ['.', '.',], ['.', '.']] and self.number == True):
            print('1', end = "")
        elif (self.board == [['O', '.'], ['O', '.',], ['.', '.']] and self.number == True):
            print('2', end = "")
        elif (self.board == [['O', 'O'], ['.', '.'], ['.', '.']] and self.number == True):
            print('3', end = "")
        elif (self.board == [['O', 'O'], ['.', 'O'], ['.', '.']] and self.number == True):
            print('4', end = "")
        elif (self.board == [['O', '.'], ['.', 'O',], ['.', '.']] and self.number == True):
            print('5', end = "")
        elif (self.board == [['O', 'O'], ['O', '.'], ['.', '.']] and self.number == True):
            print('6', end = "")
        elif (self.board == [['O', 'O'], ['O', 'O'], ['.', '.']] and self.number == True):
            print('7', end = "")
        elif (self.board == [['O', '.'], ['O', 'O'], ['.', '.']] and self.number == True):
            print('8', end = "")
        elif (self.board == [['.', 'O'], ['O', '.'], ['.', '.']] and self.number == True):
            print('9', end = "")
        elif (self.board == [['.', 'O'], ['O', 'O'], ['.', '.']] and self.number == True):
            print('10', end = "")
        elif (self.board == [['.', '.'], ['O', 'O'], ['.', 'O']] and self.decimal == True and self.number == False):
            print('.', end = "")
        elif (self.board == [['.', '.'], ['O', '.'], ['.', '.']] and self.decimal == True and self.number == False):
            print(',', end = "")
        elif (self.board == [['.', '.'], ['O', '.'], ['O', 'O']] and self.decimal == True and self.number == False):
            print('?', end = "")
        elif (self.board == [['.', '.'], ['O', 'O'], ['O', '.']] and self.decimal == True and self.number == False):
            print('!', end = "")
        elif (self.board == [['.', '.'], ['O', 'O'], ['.', '.']] and self.decimal == True and self.number == False):
            print(':', end = "")
        elif (self.board == [['.', '.'], ['O', '.'], ['O', '.']] and self.decimal == True and self.number == False):
            print(';', end = "")
        elif (self.board == [['.', '.'], ['.', '.'], ['O', 'O']] and self.decimal == True and self.number == False):
            print('-', end = "")
        elif (self.board == [['.', 'O'], ['.', '.'], ['O', '.']] and self.decimal == True and self.number == False):
            print('/', end = "")
        elif (self.board == [['.', 'O'], ['O', '.'], ['.', 'O']] and self.decimal == True and self.number == False):
            print('<', end = "")
        elif (self.board == [['O', '.'], ['.', 'O'], ['O', '.']] and self.decimal == True and self.number == False):
            print('>', end = "")
        elif (self.board == [['O', '.'], ['O', '.'], ['.', 'O']] and self.decimal == True and self.number == False):
            print('(', end = "")
        elif (self.board == [['.', 'O'], ['.', 'O'], ['O', '.']] and self.decimal == True and self.number == False):
            print(')', end = "")
        else:
            print('Invalid input')

test = Braille()
test.setBoard()