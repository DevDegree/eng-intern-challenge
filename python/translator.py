
import sys
from textwrap import wrap

#English Letters
English_Upper = {'A':'O.....','B':'O.O...', 'C':'OO....', 'D':'OO.O..', 'E':'O..O..', 'F':'OOO...', 'G':'OOOO..',
                 'H':'O.OO..', 'I':'.OO...', 'J':'.OOO..', 'K':'O...O.', 'L':'O.O.O.', 'M':'OO..O.', 'N':'OO.OO.',
                 'O':'O..OO.', 'P':'OOO.O.', 'Q':'OOOOO.', 'R':'O.OOO.', 'S':'.OO.O.', 'T':'.OOOO.', 'U':'O...OO',
                 'V':'O.O.OO', 'W':'.OOO.O','X':'OO..OO', 'Y':'OO.OOO', 'Z':'O..OOO'}
English_Lower = {'a':'O.....','b':'O.O...', 'c':'OO....', 'd':'OO.O..', 'e':'O..O..', 'f':'OOO...', 'g':'OOOO..',
                 'h':'O.OO..', 'i':'.OO...', 'j':'.OOO..', 'k':'O...O.', 'l':'O.O.O.', 'm':'OO..O.', 'n':'OO.OO.',
                 'o':'O..OO.', 'p':'OOO.O.', 'q':'OOOOO.', 'r':'O.OOO.', 's':'.OO.O.', 't':'.OOOO.', 'u':'O...OO',
                 'v':'O.O.OO', 'w':'.OOO.O','x':'OO..OO', 'y':'OO.OOO', 'z':'O..OOO'}
#Ballie Symbols
Brallie_Upper = {'O.....': 'A', 'O.O...': 'B', 'OO...': 'C', 'OO....': 'D', 'OO.O..': 'E', 'O..O..': 'F', 'OOOO..': 'G',
                'O.OO..': 'H', '.OO...': 'I', '.OOO..': 'J', 'O...O.': 'K', 'O.O.O.': 'L', 'OO..O.': 'M', 'OO.OO.': 'N',
                'O..OO.': 'O', 'OOO.O.': 'P', 'OOOOO.': 'Q', 'O.OOO.': 'R', '.OO.O.': 'S', '.OOOO.': 'T', 'O...OO': 'U',
                'O.O.OO': 'V', '.OOO.O': 'W', 'OO..OO': 'X', 'OO.OOO': 'Y', 'O..OOO': 'Z'}

Brallie_Lower = {'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g',
                'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n',
                'O..OO.': 'o', 'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u',
                'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 'O..OOO': 'z'}
#Punctuation
English_Punctuation = {'capital':'.....O', 'decimal':'.O...O', 'number': '.O.OOO'}

Brallie_Punctuation = {'.....O': 'capital', '.O...O': 'decimal', '.O.OOO': 'number'}

#Numbers
English_Numbers = {'1':'O.....','2':'O.O...', '3':'OO....', '4':'OO.O..', '5':'O..O..', '6':'OOO...', '7':'OOOO..',
            '8':'O.OO..', '9':'.OO...', 'O':'.OOO..'}
Brallie_Numbers = {'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': 'O'}

#Grammer:
English_Grammer = {'.':'..OO.O',',': '..O...','?':'..O.OO','!':'..OOO.', ':':'..OO..',';':'..O.O.','-':'....OO',
                   '/':'.O..O.','<':'.OO..O','>':'O..OO.','(': 'O.O..O', ')':'.O.OO.', ' ': '......'}

Brallie_Grammer = {'..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!', '..OO..': ':', '..O.O.': ';',
                   '....OO': '-', '.O..O.': '/', '.OO..O': '<', 'O..OO.': '>', 'O.O..O': '(', '.O.OO.': ')',
                   '......': ' '}
#Translate to Braille3
def Braille_Translator(sentence):
    output = ""
    number = False
    for char in sentence:
        if char in English_Upper:
            number = False
            output = output + English_Punctuation['capital'] + English_Upper[char]
        elif char in English_Lower:
            number = False
            output += English_Lower[char]
        elif char in English_Numbers and number == False:
            output = output + English_Punctuation['number'] + English_Numbers[char]
            number = True
        elif  char in English_Numbers and number == True:
            output += English_Numbers[char]
        elif char in English_Grammer:
            number = False
            output += English_Grammer[char]
    print(output)


#Translate to English
def English_Translator(sentence):
    sentence = wrap(sentence, 6)
    number = False
    output = ""
    i = 0
    length = len(sentence)
    while i < length: 
       if sentence[i] == English_Punctuation['capital']:
           i += 1
           output = output + Brallie_Upper[sentence[i]]
           number = False
           i = i + 1
       elif sentence[i] in Brallie_Grammer:
           output += Brallie_Grammer[sentence[i]]
           number = False
           i += 1
       elif sentence[i] == English_Punctuation['number'] and number == False:  
           i+=1  
           output += Brallie_Numbers[sentence[i]]
           number = True
           i += 1
       elif sentence[i] in Brallie_Numbers and number == True:
           
           output += Brallie_Numbers[sentence[i]]
           i += 1
       elif sentence[i] in Brallie_Lower:
           output = output + Brallie_Lower[sentence[i]]
           number = False
           i+=1
               
    print(output)

    
sentence = sys.argv
length = len(sentence)

char = 1
sentence2 = ''
while char < length:
    sentence2 += sentence[char]
    char += 1

if sentence2[0] in English_Upper or sentence2[0] in English_Lower or sentence2[0] in English_Numbers:
    Braille_Translator(sentence2)
else:
     English_Translator(sentence2)
