import sys

#The translation from English to Braille is done by mapping each character to its corresponding Braille representation
def translateENG2BRA(StrToTranslate):
    dictionaryEngBra = {
        'A': '.....OO.....', 'B': '.....OO.O...', 'C': '.....OOO....', 'D': '.....OOO.O..', 'E':'.....OO..O..', 'F': '.....OOOO...' , 'G': '.....OOOOO..' , 'H': '.....OO.OO..' , 'I': '.....O.OO...' , 'J': '.....O.OOO..' , 'K': '.....OO...O.' , 'L': '.....OO.O.O.' , 'M': '.....OOO..O.' , 'N': '.....OOO.OO.' , 'O': '.....OO..OO.' , 'P': '.....OOOO.O.' , 'Q': '.....OOOOOO.' , 'R': '.....OO.OOO.' , 'S': '.....O.OO.O.' , 'T': '.....O.OOOO.' , 'U': '.....OO...OO' , 'V': '.....OO.O.OO' , 'W': '.....O.OOO.O' , 'X': '.....OOO..OO' , 'Y': '.....OOO.OOO' , 'Z': '.....OO..OOO' ,
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e':'O..O..', 'f': 'OOO...' , 'g': 'OOOO..' , 'h': 'O.OO..' , 'i': '.OO...' , 'j': '.OOO..' , 'k': 'O...O.' , 'l': 'O.O.O.' , 'm': 'OO..O.' , 'n': 'OO.OO.' , 'o': 'O..OO.' , 'p': 'OOO.O.' , 'q': 'OOOOO.' , 'r': 'O.OOO.' , 's': '.OO.O.' , 't': '.OOOO.' , 'u': 'O...OO' , 'v': 'O.O.OO' , 'w': '.OOO.O' , 'x': 'OO..OO' , 'y': 'OO.OOO' , 'z': 'O..OOO' ,
        ' ': '......' , '1': 'O.....' , '2': 'O.O...' , '3': 'OO....' , '4': 'OO.O..' , '5': 'O..O..' , '6': 'OOO...' , '7': 'OOOO..' , '8': 'O.OO..' , '9': '.OO...' , '0': '.OOO..' ,
        '.': '..OO.O' , ',': '..O...' , ';': '..OO..' , ':': '..O.O.' , '?': '..OO.O' , '!': '..O.OO' , '-': '..O..O' , '(': '..O.OO' , ')': '..OO.O' ,  '/': '.O...O' ,  '<': '.O.O..' , '>': '.O.O.O' , 
    }
    translatedStr = ''
    numbersFollow= False
    for char in StrToTranslate:
        #If the character is a number and numbersFollow is False we set numbersFollow to True and we include the Braille representation for "Number follow"
        if char in '0123456789' and numbersFollow == False:
            numbersFollow = True
            translatedStr += '.O.OOO'
            translatedStr += dictionaryEngBra[char]
        #If the character is a number and numbersFollow is True we just need to add the Braille representation for the number since we added the "Number follow" previously
        elif char not in '0123456789' and numbersFollow == True:
            numbersFollow = False
            translatedStr += dictionaryEngBra[char]
        #This handles any other character that is not a number
        else:       
            translatedStr += dictionaryEngBra[char]
    return translatedStr
#Helper Method to split string into chunks of 6
def split_into_chunks_of_six(StrToTranslate):
    return [StrToTranslate[i:i+6] for i in range(0, len(StrToTranslate), 6)]

def translateBraToEng(StrToTranslate):
    dictionaryBra2Eng = {
       'O.....': 'a' ,'O.O...':'b' , 'OO....': 'c' ,'OO.O..': 'd' ,'O..O..' : 'e',  'OOO...': 'f' ,  'OOOO..': 'g' ,  'O.OO..' : 'h',  '.OO...' : 'i',  '.OOO..' : 'j' ,  'O...O.' : 'k', 'O.O.O.': 'l',  'OO..O.' : 'm',  'OO.OO.': 'n',  'O..OO.': 'o',  'OOO.O.': 'p', 'OOOOO.' :'q' ,  'O.OOO.': 'r', '.OO.O.': 's' ,  '.OOOO.': 't' ,  'O...OO' : 'u',  'O.O.OO' : 'v',  '.OOO.O' : 'w',  'OO..OO': 'x',  'OO.OOO': 'y' ,  'O..OOO': 'z',
        '......': ' ','..OO.O': ')', '..O...': ',','..OO..': ';','..O.O.': ':','..O.OO': '(','..O..O': '-','.O...O': '/','.O.O..': '<','.O.O.O': '>'}
    dictCapital = {'O.....': 'A','O.O...': 'B','OO....': 'C','OO.O..': 'D','O..O..': 'E','OOO...': 'F','OOOO..': 'G','O.OO..': 'H','.OO...': 'I','.OOO..': 'J','O...O.': 'K','O.O.O.': 'L','OO..O.': 'M','OO.OO.': 'N','O..OO.': 'O','OOO.O.': 'P','OOOOO.': 'Q','O.OOO.': 'R','.OO.O.': 'S','.OOOO.': 'T','O...OO': 'U','O.O.OO': 'V','.OOO.O': 'W', 'OO..OO': 'X','OO.OOO': 'Y','O..OOO': 'Z',}
    dictBRANumbers = {'O.....':'1' ,  'O.O...': '2' ,  'OO....' : '3',  'OO.O..' : '4',  'O..O..': '5',  'OOO...': '6' , 'OOOO..' : '7',  'O.OO..' : '8',  '.OO...' : '9',  '.OOO..': 'O'}
    translatedStr = ''
    numbersFollow= False
    capitalFollow = False

    for chunk in split_into_chunks_of_six(StrToTranslate):
        #If the chunk is the chunk representing number follows we set numberFollow to True
        if chunk == '.O.OOO':
            numbersFollow = True
            continue
        #If the chunk is the chunk representing space we set numbersFollow to False and we add the space to the translated string
        elif chunk == '......':
            translatedStr += ' '
            numbersFollow = False
            continue
        #Handling numbers using our dictBRANumbers
        elif numbersFollow == True:
           translatedStr += dictBRANumbers[chunk]
           continue
        
       
        #Converting next chunk to capital   
        elif chunk == '.....O':
            capitalFollow = True
            continue
        #Handling Capitals
        elif capitalFollow == True:
            translatedStr += dictCapital[chunk]
            capitalFollow = False
            continue
        #Handling regular characters that are not numbers or capitals
        else:
            translatedStr += dictionaryBra2Eng[chunk]
            continue
    return translatedStr


def translate(StrToTranslate):
    
    translatedWord = ''
    #Checking if the string contains '..' or 'OO' to determine if the translation is from Braille to English or English to Braille
    #This assumes that a string in Braille would minimally contain .. or 00 somewhere in the string and that no english word would contain .. or 00
    if '..' in StrToTranslate or 'OO' in StrToTranslate: 
        
        translatedWord= translateBraToEng(StrToTranslate)
    #If the string does not contain '..' or 'OO' we assume it is an English word and we translate it to Braille
    else:
        translatedWord = translateENG2BRA(StrToTranslate)
    return translatedWord
    
def main():
    
    if len(sys.argv) > 1 :
        input_string = ' '.join(sys.argv[1:])
        result = translate(input_string)
        print(result)
        exit(0)

if __name__ == '__main__':
    main()

    

    
