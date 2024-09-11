import sys




class brailleTranslator:


    #class variables for the braille translator
    toTranslate=[]
    isBraille=False
    isCapital=False
    isNumber=False
    translation=""


    #dictionary for the alphabet characters
    englishToBraille = {
        'a': 'O.....',   # Braille for 'a'
        'b': 'O.O...',   # Braille for 'b'
        'c': 'OO....',   # Braille for 'c'
        'd': 'OO.O..',   # Braille for 'd'
        'e': 'O..O..',   # Braille for 'e'
        'f': 'OOO...',   # Braille for 'f'
        'g': 'OOOO..',   # Braille for 'g'
        'h': 'O.OO..',   # Braille for 'h'
        'i': '.OO...',   # Braille for 'i'
        'j': '.OOO..',   # Braille for 'j'
        'k': 'O...O.',   # Braille for 'k'
        'l': 'O.O.O.',   # Braille for 'l'
        'm': 'OO..O.',   # Braille for 'm'
        'n': 'OO.OO.',   # Braille for 'n'
        'o': 'O..OO.',   # Braille for 'o'
        'p': 'OOO.O.',   # Braille for 'p'
        'q': 'OOOOO.',   # Braille for 'q'
        'r': 'O.OOO.',   # Braille for 'r'
        's': '.OO.O.',   # Braille for 's'
        't': '.OOOO.',   # Braille for 't'
        'u': 'O...OO',   # Braille for 'u'
        'v': 'O.O.OO',   # Braille for 'v'
        'w': '.OOO.O',   # Braille for 'w'
        'x': 'OO..OO',   # Braille for 'x'
        'y': 'OO.OOO',   # Braille for 'y'
        'z': 'O..OOO',   # Braille for 'z'
        'cap':'.....O',  # Braille for 'capitals'
        'num': '.O.OOO', # Braille for 'numbers'
        'space': '......'# Braille for 'spaces'
    }


    #dictionary for the numbers
    numsToBraille = {
        '1': 'O.....',   # Braille for '1'
        '2': 'O.O...',   # Braille for '2'
        '3': 'OO....',   # Braille for '3'
        '4': 'OO.O..',   # Braille for '4'
        '5': 'O..O..',   # Braille for '5'
        '6': 'OOO...',   # Braille for '6'
        '7': 'OOOO..',   # Braille for '7'
        '8': 'O.OO..',   # Braille for '8'
        '9': '.OO...',   # Braille for '9'
        '0': '.OOO..',   # Braille for '0'
    }


    #inverse dictionaries
    brailleToEnglish = {v: k for k, v in englishToBraille.items()}
    brailleToNums = {v: k for k, v in numsToBraille.items()}


    #initializer for the class
    def __init__(self) -> None:
        self.toTranslate=sys.argv
        self.toTranslate.pop(0)
        self.toTranslate=" ".join(self.toTranslate)
        self.isBraille=self.checkBraille()


    #displays the translated string
    def display(self):
        return self.translation
   
    #check if its braille
    def checkBraille(self):
        if (len(self.toTranslate)%6!=0):
            return False
           
       
        for char in self.toTranslate:
            if (char!='O')and(char!='.'):
                return False
           
        return True


    #translates the english or braille
    def translate(self):


        #starts as english
        if(not(self.isBraille)):
            for char in self.toTranslate:




                #alphabet character
                if(char.isalpha()):
                    if(char.isupper()):
                        self.translation+=self.englishToBraille['cap']
                        char=char.lower()
                    self.translation+=self.englishToBraille[char]




                #space or number
                else:
                    #is space
                    if(char==" "):
                        self.isNumber=False
                        self.translation+=self.englishToBraille['space']
                    #is number
                    else:
                        if(not(self.isNumber)):
                            self.translation+=self.englishToBraille['num']
                            self.isNumber=True
                        self.translation+=self.numsToBraille[char]
           


        #braille to english
        else:
            self.toTranslate= [self.toTranslate[i:i+6] for i in range(0, len(self.toTranslate), 6)]
            for braille in self.toTranslate:


                #next are numbers
                if(braille ==".O.OOO"):
                    self.isNumber=True
                    continue


                #next is capital
                elif(braille ==".....O"):
                    self.isCapital=True
                    continue


                #next is space
                elif(braille=="......"):
                    self.isNumber=False
                    self.translation+=" "
                    continue


                #is a letter
                if(not(self.isNumber)):
                    char=self.brailleToEnglish[braille]
                    if(self.isCapital):
                        char=char.upper()
                    self.translation+=char


                #is a number
                else:
                    self.translation+=self.brailleToNums[braille]
           
bt=brailleTranslator()
bt.translate()
print(bt.display())

















