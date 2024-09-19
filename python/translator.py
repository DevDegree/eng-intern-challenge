

import sys
#store the brail dots in dictonary for easy to decode
brail_dic = {
            'o.....':'a','o.o...':'b',
            'oo....':'c','oo.o..':'d',
            'o..o..':'e','ooo...':'f',
            'oooo..':'g','o.oo..':'h',
            '.oo...':'i','.ooo..':'j',
            'o...o.':'k','o.o.o.':'l',
            'oo..o.':'m','oo.oo.':'n',
            'o..oo.':'o','ooo.o.':'p',
            'ooooo.':'q','o.ooo.':'r',
            '.oo.o.':'s','.oooo.':'t',
            'o...oo':'u','o.o.oo':'v',
            '.ooo.o':'w','oo..oo':'x',
            'oo.ooo':'y','o..ooo':'z',
            '.....o':'caps','.o...o':'decimal',
            '.o.ooo':'number',"......":" "
            }
Eng_dic = {v: k for k, v in brail_dic.items()}


def BrailToEng(text:str) -> str:
    if(len(text)%6 !=0):
         return("NOT PROPER BRAIL FORMAT")
    # print(text)
    result = ''
    num_flag = False
    i = 0
    while i<len(text):
        braille_char = text[i:i+6]
        decodedChar= brail_dic.get(braille_char, '')
        if decodedChar == 'number':
            num_flag = True
            i += 6  # Move to the next character after handling the 'number' flag
            continue
        # If we're in number mode, translate accordingly
        if num_flag:
            if decodedChar == ' ':  # Stop number mode if a space is encountered
                result +=" "
                num_flag = False
            else:
                result += str(((ord(decodedChar) - 97) + 1) % 10)  # Convert Braille letters to numbers
            i += 6
            continue
        if(decodedChar=='caps'):
            i+=6 #increment to next char after we ack capitalization
            result += brail_dic.get(text[i:i+6], '').upper()
        else:
            result +=decodedChar
          
        i+=6
    return result


def EngToBrail(text:str):
    result = ""
    NUM_FLAG = False
    i = 0
    while(i<len(text)):
        char = text[i]
        if(char.isdigit() and not NUM_FLAG):
            NUM_FLAG = True
            result +=Eng_dic.get("number","")
            continue
        if(char.isdigit() and NUM_FLAG):
            num_to_char = chr(((int(char)-1)%10+97))#map numbers to alphabet value
            result +=Eng_dic.get(num_to_char,"")
            # print(num_to_char)
            i+=1
            continue
        
        if(NUM_FLAG):
            result += Eng_dic.get(' ','') #add space between text and number 
            NUM_FLAG= False
            i+=1
            continue
        if(char.isupper()):
            result += Eng_dic.get("caps","") + Eng_dic[char.lower()] # add caps before a capital
            # print(char)
        else:
            result += Eng_dic[char]
            # print(char)
        i +=1
    return result.upper()

def preproccessing(text:str):
    result = ""
    if(len(text)%6 ==0):
        try:
            lowercase_text = text.lower()
            result = BrailToEng(lowercase_text)
        except:
            result =  EngToBrail(text)
    else:
        result = EngToBrail(text)
    return result

arguments = sys.argv
input = ""
for i in range (1, len(arguments)):
    input +=arguments[i] +" "
print(preproccessing(input.strip()))

