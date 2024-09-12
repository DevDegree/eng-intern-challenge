
import sys

class brailleTranslator:
    def __init__(self):
         self.braille = {
            97 : 'O.....',
            98 : 'O.O...',
            99 : 'OO....',
            100 : 'OO.O..',
            101 : 'O..O..',
            102 : 'OOO...',
            103 : 'OOOO..',
            104 : 'O.OO..',
            105 : '.OO...',
            106 : '.OOO..',
            107 : 'O...O.',
            108 : 'O.O.O.',
            109 : 'OO..O.',
            110 : 'OO.OO.',
            111 : 'O..OO.',
            112 : 'OOO.O.',
            113 : 'OOOOO.',
            114 : 'O.OOO.',
            115 : '.OO.O.',
            116 : '.OOO.O',
            117 : 'O...OO',
            118 : 'O.O.OO',
            119 : '.OOO.O',
            120 : 'OO..OO',
            121 : 'OO.OOO',
            122 : 'O..OOO',
            49 : 'O.....',
            50 : 'O.O...',
            51 : 'OO....',
            52 : 'OO.O..',
            53 : 'O..O..',
            54 : 'OOO...',
            55 : 'OOOO..',
            56 : 'O.OO..',
            57 : '.OO...',
            48 : '.OOO..',
            'capital_follows' : '.....O',
            'decimal_follows' : '.O...O',
            'number_follows' : '.O.OOO',
            46 : '..OO.O',
            44 : '..O...',
            63 : '..O.OO',
            33 : '..OOO.',
            58 : '..OO..',
            59 : '..O.O.',
            45 : '....OO',
            47 : '.O..O.',
            60 : '.OO..O',
            62 : 'O..OO.',
            40 : 'O.O..O',
            41 : '.O.OO.',
            32 : '......',
        }

    def isBraille(self, text):
        is_braille = True
        for char in text:
            if not(char == '.' or char == 'O'):
                is_braille = False
        return is_braille
    
    def translator(self, input):
        output = ''
        num_flag = False
        capital_flag = False

        # Check if the input is in Braille or English
        is_braille = self.isBraille(input)
        
        if is_braille:
            # traverse to check input in lenght of 6
            for start in range(0, len(input), 6):
                
                # traverse through map to check if input exist in value
                for key, val in self.braille.items():                  
                    
                    # created a token of input string
                    # check if token exist in value
                    if val == input[start: start + 6]:

                        # rasied capital flag when capital braille symbol is encountered
                        if key == 'capital_follows':
                            capital_flag = True
                            continue

                        # if capital flag raised decreased the ASCII Value by 32
                        # to convert from lowercase to uppercase
                        if capital_flag :
                            key -= 32
                            capital_flag = False

                        # raised number flag when number braille symbol is encountered
                        # moved to next string if condition met true
                        if key == 'number_follows':
                            num_flag = True  
                            continue
                        
                        # if number flag is raised convert ASCII(Character) to ASCII(Number)
                        if num_flag:

                            # for number 0
                            if key == 106:
                                key = 48
                                
                            # for number 1 to 9
                            if key > 96 and key < 106:
                                key -= 48

                        # reset the number flag when space is encountered
                        if key == 32:
                            num_flag = False
                        
                        output += chr(key)
                        break
            print(output)

        # to convert string to braille
        else:
            # loop through input 
            for char in input:
                # convert character to interger
                num = ord(char)

                # check if input is capital
                # convert ASCII uppercase character to ASCII lowercase character 
                if num > 64 and num < 91:
                    output += '.....O'
                    num += 32
                    output += self.braille[num]

                # check for number
                elif num > 47 and num < 58:

                    # raised the number flag and add braille syumbol for number
                    if not(num_flag):
                        num_flag = True
                        output += '.O.OOO'
                    output += self.braille[num]
                
                # check for characters
                else:
                    output += self.braille[num]
                
                # reset number flag if space is encountered
                if num == 32:
                    num_flag = False
            
            print(output)
                
# class object
translate = brailleTranslator()
sToGether = ""

# loop through command line argument
for i in range(1, len(sys.argv)):
    # concat arguments
    sToGether += sToGether.join([sys.argv[i]])

    # if last argument, do not add trailling space
    if len(sys.argv)- 1 == i:
        continue
    # add trailling space after arguments
    sToGether += " "

# calling class function
translate.translator(sToGether)


