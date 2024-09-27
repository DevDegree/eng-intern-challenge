import sys

letter_to_braille={'a':'O.....','b':'O.O...','c':'OO....','d':'OO.O..','e':'O..O..','f':'OOO...','g':'OOOO..','h':'O.OO..','i':'.OO...','j':'.OOO..','k':'O...O.',
'l':'O.O.O.','m':'OO..O.','n':'OO.OO.','o':'O..OO.','p':'OOO.O.','q':'OOOOO.','r':'O.OOO.','s':'.OO.O.','t':'.OOOO.','u':'O...OO','v':'O.O.OO','w':'.OOO.O',
'x':'OO..OO','y':'OO.OOO','z':'O..OOO',' ':'......','A':'.....OO.....','B':'.....OO.O...','C':'.....OOO....','D':'.....OOO.O..','E':'.....OO..O..','F':'.....OOOO...',
'G':'.....OOOOO..','H':'.....OO.OO..','I':'.....O.OO...','J':'.....O.OOO..','K':'.....OO...O.','L':'.....OO.O.O.','M':'.....OOO..O.','N':'.....OOO.OO.','O':'.....OO..OO.',
'P':'.....OOOO.O.','Q':'.....OOOOOO.','R':'.....OO.OOO.','S':'.....O.OO.O.','T':'.....O.OOOO.','U':'.....OO...OO','V':'.....OO.O.OO','W':'.....O.OOO.O','X':'.....OOO..OO',
'Y':'.....OOO.OOO','Z':'.....OO..OOO','1':'O.....','2':'O.O...','3':'OO....','4':'OO.O..','5':'O..O..','6':'OOO...','7':'OOOO..','8':'O.OO..','9':'.OO...','0':'.OOO..','.':'..OO.O'}

braille_to_letter={'O.....':'a','O.O...':'b','OO....':'c','OO.O..':'d','O..O..':'e','OOO...':'f','OOOO..':'g','O.OO..':'h','.OO...':'i','.OOO..':'j','O...O.':'k',
'O.O.O.':'l','OO..O.':'m','OO.OO.':'n','O..OO.':'o','OOO.O.':'p','OOOOO.':'q','O.OOO.':'r','.OO.O.':'s','.OOOO.':'t','O...OO':'u','O.O.OO':'v','.OOO.O':'w',
'OO..OO':'x','OO.OOO':'y','O..OOO':'z','..OO.O':'.','......':' '}

braille_to_number={'O.....':'1','O.O...':'2','OO....':'3','OO.O..':'4','O..O..':'5','OOO...':'6','OOOO..':'7','O.OO..':'8','.OO...':'9','.OOO..':'0','..OO.O':'.'}

words=sys.argv

braille=True
if words[1]:
    if len(words)>2:
        braille=False
    if len(words[1])%6!=0:
        braille=False
    for j in range(1,len(words)):
        for i in words[j]:
            if i not in {'O','.'}:
                braille=False
                break

output=''
if not braille:
    for i in range(1,len(words)):
        number=False
        for j in words[i]:
            if not number and j in {'1','2','3','4','5','6','7','8','9','0'}:
                output=output+'.O.OOO'
                number=True
            output=output+letter_to_braille[j]
        if i!=len(words)-1:
            output=output+letter_to_braille[' ']
else:
    for i in range(1,len(words)):
        start=0
        number=False
        while start<=len(words[i])-1:
            token=words[i][start:start+6]
            if token=='.O.OOO':
                number=True
            elif number:
                if token=='......':
                    number=False
                    output=output+' '
                else:
                    output=output+braille_to_number[token]
            elif token=='.....O':
                start+=6
                token=words[i][start:start+6]
                output=output+braille_to_letter[token].upper()
            else:
                output=output+braille_to_letter[token]
            start+=6
        if i!=len(words)-1:
            output+='......'
            

print(output)



