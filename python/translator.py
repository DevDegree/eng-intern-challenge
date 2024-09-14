#!/usr/bin/env python
import sys
charecter = ['a','b','c','d','e','f','g',
             'h','i','j','k','l','m',
             'n','o','p', 'q','r','s','t',
             'u','v','w','x','y','z','.',
             ',','?','!',':',';','_','/',
             '<','>','(',')','^','#',' ','.#']
symbols =  ['O.....','O.O...','OO....','OO.O..', 'O..O..','OOO...','OOOO..','O.OO..','.OO...',
            '.OOO..','O...O.','O.O.O.','OO..O.','OO.OO.','O..OO.','OOO.O.','OOOOO.','O.OOO.','.OO.O.',
            '.OOOO.','O...OO','O.O.OO','.OOO.O','OO..OO','OO.OOO','O..OOO', '..OO.O',
            '..O...','..O.OO','..OOO.','..OO..','..O.O.','....OO','.O..O.',
            '.OO..O','O..OO.','O.O..O','.O.OO.','.....O','.O.OOO','......','.O...O']
time = 2;
for element in sys.argv[1:]:
    text = element
    if (not (len(text) % 6)) and (text.count('O') + text.count('.') == len(text)):
        dictword = {symbols[i]: charecter[i] for i in range(len(symbols))}
        text = map(''.join, zip(*[iter(text)]*6))
        words = list("".join(dictword[a] for a in text))
        number = False
        numbers = {'a':'1', 'b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'0'}
        for i in range (len(words)):
            if words[i] == '>' and (not((i == 0 or words[i-1] == ' ') and words[i+1] == ' ')):
                words[i] = 'o'
        i = 0;
        while i < len(words):
            if words[i] == '^':
                words[i+1] = words[i+1].swapcase()
            if words[i] == '#':
                number = True
            if words[i] == ' ':
                number = False
            if number and words[i] in numbers.keys():
                words[i] = numbers[words[i]]
            i+=1
        words[:] = (value for value in words if value != '^')
        words[:] = (value for value in words if value != '#')
        print(''.join(words),end='')
        if time < len(sys.argv):
            print(' ',end='')
    else:
        letters = {'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','0':'j'}
        text = list(map(''.join, zip(*[iter(text)]*1)))
        i = 0;
        while i < len(text):
            if text[i].isupper():
                text[i] = text[i].swapcase()
                text = text[:i] + ['^'] + text[i:]
            if text[i].isdigit():
                text[i] = letters[text[i]]
                if (i == 0 or text[i-1] == ' '):
                    text = text[:i] + ['#'] + text[i:]
            i+=1
        dictword = {charecter[i]: symbols[i] for i in range(len(charecter))}
        words = "".join(dictword[a] for a in text)
        print(str(words),end='')
        if time < len(sys.argv):
            print('......',end='')
    time+=1;
