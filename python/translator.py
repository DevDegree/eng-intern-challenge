import sys
import re

file = open("brailleEng.txt", "r")
lines = file.readlines()
file.close()


eng_to_braille = {}
braille_to_eng = {}

for line in lines:
    curr = line.strip()

    #check curr line is not blank
    if curr:
        #index of equals sign on each line
        i=curr.index("=")
        eng = curr[:i].strip("'")
        braille = curr[i+1:]

        eng_to_braille[eng] = braille

        #one braille symbol can map to multiple Eng translations, so each value here is a list of translations
        braille_to_eng[braille] = braille_to_eng.get(braille, []) + [eng]



text=' '.join(sys.argv[1:])

#return string
res = ''

#the dictionary we will use
d = {}

#mark whether input text is Braille 
is_braille=False

if len(text) > 0 and len(text) % 6 == 0 and text[:6] in braille_to_eng:
    #check if text contains only . or O
    #if text contains any other characters besides . or O, then is English
    if re.search('[^(O.)]', text):
        d = eng_to_braille
        #print("english")
    else:
         d=braille_to_eng
         is_braille=True
         #print("is braille")

else:
    #if input text is in English
    d=eng_to_braille
    #print("english")


if is_braille:
    #mark whether we need to capitalize the next letter
    capitalize = False
    num_mode = False


    #process in 6-character chunks
    for i in range(0, len(text), 6):

        translated = d[text[i:i+6]]
        #print(translated)
        #RESET num_mode to False whenever there is a space
        if translated[0] == ' ':
            num_mode = False

        #if current braille is NUM_FOLLOWS:
        if translated[0] == "NUM_FOLLOWS":
            num_mode = True
            continue 
            #don't need to add this translation to result, so skip to next
        

        #if translating braille to numbers
        if num_mode == True:
            if translated[0] == "DECIMAL_FOLLOWS":
                res += '.'

            else:
                res += translated[1]
        
        
        #if not translating braille to numbers
        else:
            if translated[0] == "CAPITAL_FOLLOWS":
                capitalize = True
                continue
            if capitalize == True:
                res += translated[0]
                #"CAPITAL_FOLLOWS" only capitalizes the following letter, so immediately set capitalize to False.
                # This prevents making the following letters capital.
                capitalize = False
            else:
                res += translated[0].lower()



    
else:
    num_mode = False
    
    for c in text:
            
            #if c is a number
            if c.isdigit():
                #only add 'NUM_FOLLOWS' before the first digit in a sequence of digits
                if num_mode == False:
                    res += d['NUM_FOLLOWS']
                    num_mode = True
                res += d[c]
            #if c is not a number
            else:
                #check for case of decimal number!
                #i.e. check if there is a number following '.'
                if c == '.' and (text.index(c)+1 < len(text)) and text[text.index(c)+1].isdigit():
                    res+=d['DECIMAL_FOLLOWS']
                    num_mode = True

                else:
                    num_mode = False
                    if c.isupper():
                        res += d['CAPITAL_FOLLOWS']
                    res += d[c.upper()]


print(res)
