# This is my first time ever coding in python, I've used Javascript before so I should really be working in Javascript
# However this is as good as anytime to learn python so here I am

import sys
#hard coded translation tables
#
#Part 1
#

brailleToEnglish = {
    #keys : values
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO.O..': 'd',
    'O..O..': 'e',
    'OOO...': 'f',
    'OOOO..': 'g',
    'O.OO..': 'h',
    '.OO...': 'i',
    '.OOO..': 'j',
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o',
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OOO.O': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z',
    '..OO.O': '.',
    '..O...': ',',
    '...OOO': '?',
    '..OOO.': '!',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '-',
    '.O..O.': '/',
    '.OO..O': '<',
    #'O..OO.': '>',
    'O.O..O': '(',
    '.O.OO.': ')',
    '......': ' '
}

englishToBraile = {v: k for k, v in brailleToEnglish.items()} #makes a new dictionary that is a duplicate of the braileToEnglish dictionary except the keys and values are swapped

numbersToLetters = { # dictionary for numbers to letters
    '1' : 'a',
    '2' : 'b',
    '3' : 'c',
    '4' : 'd',
    '5' : 'e',
    '6' : 'f',
    '7' : 'g',
    '8' : 'h',
    '9' : 'i',
    '0' : 'j'
}

lettersToNumbers = {v: k for k, v in numbersToLetters.items()} # dictionary for letters to numbers


#Get input
#
#Part 2
#
if len(sys.argv) == 1:
        print("No Input")
        sys.exit(1) #standard error code apparently

firstWord = sys.argv[1]
myInput = sys.argv[1:] # I find it very cool that I can take all the arguemnts with one simple line like this


#Check if english or braille
#
#Part 3
#
englishInput = False
if len(myInput) != 1 or (len(firstWord) % 6) != 0:
    englishInput = True # If it has more than one argument, or its not divisble by 6 I already know it has to be english input
else: 
    for char in firstWord:
         if char not in [".", "O"]: #if it has any character that isnt a "." or "O" it will assume its englishInput
              englishInput = True   #meaning something like OOOOO. could cause an error if it thinks its braille when it isn't

#translate from one to the other
#
#Part 4
#
answer = ""
if englishInput: 
    for currWord in myInput:
        number = False
        for currChar in currWord:
            if currChar.isdigit() and not number: # really interesting I can almost talk english to the python compiler saying "and not" instead of && !
                answer = answer + ".O.OOO" 
                number = True
                    
            if currChar.isupper():
                answer = answer + ".....O"
                currChar = currChar.lower()

            if number:
                answer = answer + englishToBraile[numbersToLetters[currChar]]
            else:
                answer = answer + englishToBraile[currChar]
        answer = answer + "......"

    answer = answer[:-6]

else:
     #print("braille")
     capital = False
     decimal = False #Does this even matter? The decimal doesnt even have any conflicting braile character, the > conflics with o so Im going to use the decimal follows for it only
     number = False
     for i in range(len(firstWord) // 6):
        currPart = firstWord[6*i:6*i+6] #Grabbing 6 characters at a time from the braille
        if currPart == ".....O": #Capital
             capital = True
        elif currPart == ".O...O": #Decimal
             decimal = True
        elif currPart == ".O.OOO": #Number
             number = True
        else:
            if capital: #Add corresponding characters
                answer = answer + brailleToEnglish[currPart].capitalize()
                capital = False
            elif number:
                 if currPart == "......": #Stops printing numbers if it sees a space
                      answer = answer + brailleToEnglish[currPart]
                      number = False
                 else:
                      answer = answer + lettersToNumbers[brailleToEnglish[currPart]]
            elif decimal:
                if currPart == "O..OO.":
                     answer = answer + ">"
                else:
                    answer = answer + brailleToEnglish[currPart]
                decimal = False
            else: 
                 answer = answer + brailleToEnglish[currPart]

'''
.....O cap
O.OO.. H
O..O.. e
O.O.O. l
O.O.O. l
O..OO. o
...... space
.OOO.O w
O..OO. o
O.OOO. r
O.O.O. l
OO.O.. d


.....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO test case output
.....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO my output when I run it myself manually
'''
#return answer
print(answer)
'''
overall using python was actually pretty fun, it was really frustrating at the start because I did not know the syntax at all. But now that I have it working I'm glad I chose
to use python because it feels more rewarding, also pythons pretty cool

Learning python while doing this took a long time, so I am aware of some improvements I can make, however I don't have time for them. I have listed them below:
-Format dictionaries better
-Handle error of something not being in dictionary
-Fix the issue with the distinction between braille and English noted on lines 93 and 94
-Currently if you input a . in english it won't show the "Decimal follows" braille before it shows the decimal braille
-Overall clean up document

Future things to add:
-Make it able to read braille from a digital picture 
'''
