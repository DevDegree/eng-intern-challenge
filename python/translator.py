import sys
from collections import Counter

#define the dictionaries:
eng_br = {'a':'O.....',
'b':'O.O...',
'c':'OO....',
'd':'OO.O..',
'e':'O..O..',
'f':'OOO...',
'g':'OOOO..',
'h':'O.OO..',
'i':'.OO...',
'j':'.OOO..',
'k':'O...O.',
'l':'O.O.O.',
'm':'OO..O.',
'n':'OO.OO.',
'o':'O..OO.',
'p':'OOO.O.',
'q':'OOOOO.',
'r':'O.OOO.',
's':'.OO.O.',
't':'.OOOO.',
'u':'O...OO',
'v':'O.O.OO',
'w':'.OOO.O',
'x':'OO..OO',
'y':'OO.OOO',
'z':'O..OOO',
'cap':'.....O',
'dec':'.O...O',
'num':'.O.OOO',
'sp':'......',
'.':'..OO.O',
',':'..O...',
'?':'..O.OO',
'!':'..OOO.',
':':'..OO..',
';':'..O.O.',
'-':'....OO',
'/':'.O..O.',
'<':'.OO..O',
'>':'O..OO.',
'(':'O.O..O',
')':'.O.OO.'}

eng_br_num = {'1':'O.....',
'2':'O.O...',
'3':'OO....',
'4':'OO.O..',
'5':'O..O..',
'6':'OOO...',
'7':'OOOO..',
'8':'O.OO..',
'9':'.OO...',
'0':'.OOO..'}

#we are going to assume only leters (no symbols like question marks, as is not clear thow to differentiate and it would miss translate)
br_eng = {'O.....':'a', 
'O.O...':'b', 
'OO....':'c', 
'OO.O..':'d', 
'O..O..':'e', 
'OOO...':'f', 
'OOOO..':'g', 
'O.OO..':'h', 
'.OO...':'i', 
'.OOO..':'j', 
'O...O.':'k', 
'O.O.O.':'l', 
'OO..O.':'m', 
'OO.OO.':'n', 
'O..OO.':'o', 
'OOO.O.':'p', 
'OOOOO.':'q', 
'O.OOO.':'r', 
'.OO.O.':'s', 
'.OOOO.':'t', 
'O...OO':'u', 
'O.O.OO':'v', 
'.OOO.O':'w', 
'OO..OO':'x', 
'OO.OOO':'y', 
'O..OOO':'z',
'.....O':'cap', 
'.O...O':'dec', 
'.O.OOO':'num', 
'......':'sp'}

br_eng_num = {'O.....':'1', 
'O.O...':'2', 
'OO....':'3', 
'OO.O..':'4', 
'O..O..':'5', 
'OOO...':'6', 
'OOOO..':'7', 
'O.OO..':'8', 
'.OO...':'9', 
'.OOO..':'0',
'......':'sp'}

#define the functions

def is_eng(word): #returns 1 if english, 0 if braile
    if len(word)==0: #print error if wmpty word
        print('word must be non blank')
    else:
        resp = Counter([l for l in word]) #count all the ocurrences of each letter
        if len(resp) <=2: #it could be braile
            ltrs = list(resp.keys()) #list of leters
            try:
                #remove the leters O and . assuming is braile
                ltrs.remove('O')
                ltrs.remove('.')
                
                if len(ltrs) == 0 : #if it is braile, there should not be anything left
                    return 0 
            except:
                return 1 #is a word with less than 2 leters but is not braile
        else:
            return 1 #return 1 as it is english leters
        

def engToBr(word):
    resp = '' #start with an empty word to return
    dic = eng_br #assume leters
    num = 0 #assume is letters
    for l in word: #iterate over every character of the input
        if l.isupper(): #for capitalized leter, add the capital braile symbol
            resp += dic['cap']
            resp += dic[l.lower()]
        elif l == ' ': #for spaces add space symbol
            dic = eng_br
            num = 0
            resp += dic['sp']
        elif l.isnumeric(): #for each numeric value adds numeric symbol prior to the number
            if num ==0:
                dic  = eng_br_num    
                resp += eng_br['num']
                num =1
            resp += dic[l]
        else: #if not number or capital or space, print the braile value of the character
            resp += dic[l]
    print(resp)

def brToEng(word):
    dic = br_eng #use eng letters dictionary by default
    resp = '' #start with an empty word to return
    c = 0 #capital indicator as 0
    for i in range(0, len(word),6): #iterate over the entire word in 6 by 6
        l = dic[word[i:i+6]] #review every 6 symbols to make up 1 braile simbol
        if l == 'sp': #if is a space
            dic = br_eng #return to letters dict
            l = ' '
        elif l == 'num': #if is a number, change dic to number
            dic = br_eng_num
            l=''
        elif l == 'cap': #if capital leters follows, indicate it
            c = 1
            l=''

        if (c == 1) & (l != ''): #if the previous was a capital indicator, capitalize the leter
            l = l.upper()
            c=0 #return the indicator to lower
        resp = resp+l #add the letter to the reponse
    print(resp)

def translator(word): #translate an input
    if is_eng(word) == 1:
        engToBr(word)
    else:
        brToEng(word)
        
def main():
    if len(sys.argv) <1:
        print("Please input at least 1 word")
        sys.exit(1)
    
    concatenated_input = ''
    
    for i in range(1,len(sys.argv)): #iterate over all input words
        # Concatenate the words
        if i >1: #add a space in front of each word (other than the first)
            concatenated_input += ' '
            
        concatenated_input += str(sys.argv[i])

    # translate
    translator(concatenated_input)
    
if __name__ == "__main__":
    main()