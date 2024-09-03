import re
import sys
from enum import Enum


#enum for alphabets and special characters

class BrailleAlphabetAndSpecialChars(Enum):
    a = "o....."
    b = "o.o..."
    c = "oo...."
    d = "oo.o.."
    e = "o..o.."
    f = "ooo..."
    g = "oooo.."
    h = "o.oo.."
    i = ".oo..."
    j = ".ooo.."
    k = "o...o."
    l = "o.o.o."
    m = "oo..o."
    n = "oo.oo."
    o = "o..oo."
    p = "ooo.o."
    q = "ooooo."
    r = "o.ooo."
    s = ".oo.o."
    t = ".oooo."
    u = "o...oo"
    v = "o.o.oo"
    w = ".ooo.o"
    x = "oo..oo"
    y = "oo.ooo"
    z = "o..ooo"
    period = "..oo.o"
    comma = "..o..."
    question = "..o.oo"
    exclaim = "..ooo."
    colon = "..oo.."
    sColon = "..o.o."
    hyphen = "....oo"
    slash = ".o..o."
    great = "o..oo."
    less = ".oo..o"
    open = "o.o..o"
    close = ".o.oo."
    space = "......"
    capital = ".....o"
    decimal = ".o...o"
    number = ".o.ooo"


#enum for numbers
class BrailleNumbers(Enum):
    N1 = "o....."
    N2 = "o.o..."
    N3 = "oo...."
    N4 = "oo.o.."
    N5 = "o..o.."
    N6 = "ooo..."
    N7 = "oooo.."
    N8 = "o.oo.."
    N9 = ".oo..."
    N0 = ".ooo.."


#while converting english to braille, change special chars to enum keys
def convertToSpecialChar(ch):
    if ch == '.':
        return "period"
    elif ch == ',':
        return "comma"
    elif ch == '?':
        return "question"
    elif ch == '!':
        return "exclaim"
    elif ch == ':':
        return "colon"
    elif ch == ';':
        return "sColon"
    elif ch == '-':
        return "hyphen"
    elif ch == '/':
        return "slash"
    elif ch == '>':
        return "great"
    elif ch == '<':
        return "less"
    elif ch == '(':
        return "open"
    elif ch == ')':
        return "close"
    else:
        return None

#while converting braille to english, changing enum keys to special chars
def convertSpecialStringToCharacter(specialInString):
    if specialInString == "period":
        return '.'
    elif specialInString == "comma":
        return ','
    elif specialInString == "question":
        return '?'
    elif specialInString == "exclaim":
        return '!'
    elif specialInString == "colon":
        return ':'
    elif specialInString == "sColon":
        return ';'
    elif specialInString == "hyphen":
        return '-'
    elif specialInString == "slash":
        return '/'
    elif specialInString == "great":
        return '>'
    elif specialInString == "less":
        return '<'
    elif specialInString == "open":
        return '('
    elif specialInString == "close":
        return ')'
    elif specialInString == "space":
        return ' '
    elif specialInString == "decimal":
        return '.'
    else:
        return None

# to check whether given input is braille or english
def detectLanguage(lang):
    regex_pattern = r'^[o.]+$'
    if ((len(lang) % 6 == 0) and not lang.isspace() and re.match(regex_pattern,lang)):
        detected_lang = "Braille"
    else:
        detected_lang = "English"
    return detected_lang

#English to Braille translation
def translateToBraille(english_string):
    translated_braille = ""

    i=0
    while i < len(english_string):
        c = english_string[i]
        #handling alphabets
        if c.isalpha():
            #handling upper case
            if c.isupper():
                translated_braille += BrailleAlphabetAndSpecialChars.capital.value
            translated_braille += BrailleAlphabetAndSpecialChars[c.lower()].value

        #handling numbers
        elif c.isnumeric():
            if i-1 < 0 or not english_string[i-1].isnumeric():
                translated_braille += BrailleAlphabetAndSpecialChars.number.value
                translated_braille += BrailleNumbers["N" + c].value
            elif english_string[i-1].isnumeric():
                translated_braille += BrailleNumbers["N"+c].value

        #handling space
        elif c.isspace():
            translated_braille += BrailleAlphabetAndSpecialChars.space.value

        #handling special characters
        elif not c.isalnum():
            if convertToSpecialChar(c):
                translated_braille += BrailleAlphabetAndSpecialChars[convertToSpecialChar(c)].value
        #nothing matches
        else:
            translated_braille += "$$$$$$"

        i += 1

    return translated_braille

#Braille to English translation
def translateToEnglish(braille_string):

    translated_English = ""
    capsBraille = False
    numbersBraille = False

    i=0
    while i<len(braille_string):

        braille_chunk = braille_string[i:i+6]

        if len(braille_chunk) < 6:
            break
        #check chunk is "number follows"
        if braille_chunk == BrailleAlphabetAndSpecialChars['number'].value:
            numbersBraille = True
        # check chunk is "capital follows"
        elif braille_chunk == BrailleAlphabetAndSpecialChars['capital'].value:
            capsBraille = True
        # check chunk is "space"
        elif braille_chunk == BrailleAlphabetAndSpecialChars['space'].value:
            translated_English += convertSpecialStringToCharacter("space")
            if numbersBraille == True:
                numbersBraille = False

        # check if chunk is alphabet characters
        elif (numbersBraille == False and capsBraille == False and BrailleAlphabetAndSpecialChars(braille_chunk).name.isalpha()
              and len(BrailleAlphabetAndSpecialChars(braille_chunk).name) == 1):
            translated_English += BrailleAlphabetAndSpecialChars(braille_chunk).name
        #check if read chunk is special characters
        elif (numbersBraille == False and capsBraille == False and
              convertSpecialStringToCharacter(BrailleAlphabetAndSpecialChars(braille_chunk).name)):
            translated_English += convertSpecialStringToCharacter(BrailleAlphabetAndSpecialChars(braille_chunk).name)
        elif numbersBraille == True:
            translated_English += BrailleNumbers(braille_chunk).name[1:2]
        elif capsBraille == True:
            translated_English += BrailleAlphabetAndSpecialChars(braille_chunk).name.upper()
            capsBraille = False
        else:
            translated_English += "$"

        i += 6

    return translated_English

if __name__ == '__main__':

    input_language = sys.argv[1]
    found_lang = detectLanguage(input_language)

    if(found_lang == "English"):
        translated_string = translateToBraille(input_language)
    else:
        translated_string = translateToEnglish(input_language)

    print(translated_string)




