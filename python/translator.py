import sys
import re

#common resources
ENGLISH_LETTERS = {
    "a" : "o....." ,
    "b" : "o.o..." ,
    "c" : "oo...." ,
    "d" : "oo.o..",
    "e" : "o..o.." ,
    "f" : "ooo..." ,
    "g" : "oooo.." ,
    "h" : "o.oo.." ,
    "i" : ".oo...", 
    "j" : ".ooo.." ,
    "k" : "o...o." ,
    "l" : "o.o.o." ,
    "m" : "oo..o." ,
    "n" : "oo.oo." ,
    "o" : "o..oo." ,
    "p" : "ooo.o." ,
    "q" : "ooooo." ,
    "r" : "o.ooo." ,
    "s" : ".oo.o." ,
    "t" : ".oooo.",
    "u" : "o...oo" ,
    "v" : "o.o.oo" ,
    "w" : ".ooo.o",
    "x" : "oo..oo" ,
    "y" : "oo.ooo" ,
    "z" : "o..ooo" ,
    "capital" : ".....o",
    "decimal" : ".o...o",
    "number" : ".o.ooo", 
     " " : "......" ,
}

ENGLISH_NUMBERS = {
     "0" : ".ooo..",
     "1" : "o.....",
     "2" : "o.o...",
     "3" : "oo....",
     "4" : "oo.o..",
     "5" : "o..o..",
     "6" : "ooo...",
     "7" : "oooo..",
     "8" : "o.oo..",
     "9" : ".oo...",
}

BRAILLE_LETTERS = {
    "o....." : "a",
    "o.o..." : "b",
    "oo...." : "c",
    "oo.o.." : "d",
    "o..o.." : "e",
    "ooo..." : "f",
    "oooo.." : "g",
    "o.oo.." : "h",
    ".oo..." : "i",
    ".ooo.." : "j",
    "o...o." : "k",
    "o.o.o." : "l",
    "oo..o." : "m",
    "oo.oo." : "n",
    "o..oo." : "o",
    "ooo.o." : "p",
    "ooooo." : "q",
    "o.ooo." : "r",
    ".oo.o." : "s",
    ".oooo." : "t",
    "o...oo" : "u",
    "o.o.oo" : "v",
    ".ooo.o" : "w",
    "oo..oo" : "x",
    "oo.ooo" : "y",
    "o..ooo" : "z",
    "capital" : ".....o",
    "decimal" : ".o...o",
    "number" : ".o.ooo", 
    "......" : " " ,
}

BRAILLE_NUMBERS = {
    ".ooo.." : "0",
    "o....." : "1",
    "o.o..." : "2",
    "oo...." : "3",
    "oo.o.." : "4",
    "o..o.." : "5",
    "ooo..." : "6",
    "oooo.." : "7",
    "o.oo.." : "8",
    ".oo..." : "9",
}

#braille and english parsers
def convert_to_english(input):
    sentence = ""
    letter = ""
    capital = False
    number = False

    for i in range(1, len(input)):
        letter += input[i] #add character to braille letter
        if i%6 == 0: # a full letter is ready for translation (6 characters parsed)

            #if letter is a capital flag, reset letter string and skip to next iteration
            if letter == BRAILLE_LETTERS["capital"]:   
                capital = True

            #if letter is a number flag, reset letter string and skip to next iteration
            elif letter == BRAILLE_LETTERS["number"]:   
                number = True

            #if letter is a decimal flag, reset letter string and skip to next iteration
            elif letter == BRAILLE_LETTERS["decimal"]:   
                sentence += "."

            #else time to translate letter
            # if capital letter
            elif capital:
                sentence += BRAILLE_LETTERS[letter].upper()
                capital= False
            
            elif number:
                if BRAILLE_LETTERS[letter] == " ": 
                    #turn off number mode at a space
                    number = False
                    sentence += BRAILLE_LETTERS[letter]
                else:
                    sentence += BRAILLE_NUMBERS[letter]

            #elif decimal:
                #sentence += BRAILLE_NUMBERS[letter]

            else:
                sentence += BRAILLE_LETTERS[letter]

            #resetting letter only because we've processed it
            letter = ""

    print(sentence)  

    return(sentence)

def convert_to_braille(input):

    sentence = ""
    #letter = ""
    numbers = False

    for i in range(len(input)):
        #print(i)

        #cases
        #capital 
        #add capital follows character
        if ord(input[i]) >= 65 and ord(input[i]) <= 90:
            sentence += ENGLISH_LETTERS['capital']
            sentence += ENGLISH_LETTERS[chr(ord(input[i]) + 32)] #change to .tolower()
            continue
        
        #numbers 

        #if number
        if ord(input[i]) >= 48 and ord(input[i]) <= 57:
            #if first number send numbers follows char and turn on flag
            if numbers == False:
                numbers = True
                sentence += ENGLISH_LETTERS['number']
                sentence += ENGLISH_NUMBERS[input[i]]
                continue
            else:
                sentence += ENGLISH_NUMBERS[input[i]]
                continue
        #if not a number and the flag is still on, turn it off (reached the end of number seq)        
        if numbers:
            numbers = False
        #all other non special cases translate the letter
        sentence += ENGLISH_LETTERS[input[i]]

    
    print(sentence.replace("o", "O"))
    return(sentence.replace("o", "O")) #might need to change this

#process input

if len(sys.argv) < 3:
    input = sys.argv[1]
else:
    input = sys.argv[1:]
    input_string = ""

    for word in input:
        input_string += word + ' '

    input = input_string[0: -1]
    
#send to correct parser
pattern = r'^[.O]+$'
if (bool(re.match(pattern, input))) and len(input) > 1 and len(input) % 6 == 0:
    input = "-" + input
    input = input.replace("O", "o") #might need to change this
    convert_to_english(input)
else:
    convert_to_braille(input)

#TODO 
#special characters?
#change o's to O's in dictionaries
