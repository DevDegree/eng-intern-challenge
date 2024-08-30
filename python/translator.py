# Ryan Baumgart, ryanjbaumgart@gmail.com
# Shopify - Eng Intern Challenge Fall - Winter 2025

# ------ Pseudocode / Brainstorming ------ 
# get arguments, compile as single string
# call function to translate string
# - identify whether it is currently English or Braille
# -- Braille has a length of a multiple of 6 and consists strictly of 'O' and '.'
# - if English:
# -- for i = 0 to string length:
# --- m_char = string[i]
# --- if m_char is alphabetical: 
# ---- if capital: add 'capital follows' as '.....O' then do toLowerCase()
# ---- ascii value of lower case (97 to 122) - 97 = values from 0 to 25
# ---- if within 0 to 9: add firstDecade[#] + ".." 
# ---- if within 10 to 19: add firstDecade[#] + "O." 
# ---- if within 20 to 25: add firstDecade[# - (# > 22 ? 1 : 0)] + "OO"
# ----- special case if # == 22 then: add ".OOO.O"
# --- else if m_char is numerical:
# ---- add 'number follows' as '.O.OOO'
# ---- while m_char is not a space ("......"):
# ----- add firstDecade[((parsed m_char) - 1) % 10]
# ----- i++
# --- else:
# ---- switch case statement for symbols:
# ----- space (' ') = "......"
# - if Braille:
# -- booleans: capital, number
# -- for i = 0 to string length skip by 6:
# --- m_brailleCell = string.substring(i, i+6)
# --- set capital as false (for every character)
# --- if m_brailleCell = 'capital follows' as '.....O' then set capital as true
# --- else if m_brailleCell = 'number follows' as '.O.OOO' then set number to true
# --- else if m_brailleCell = 'space' as '......' then set number to false and add space character (" ") and continue
# --- m_signature = m_brailleCell.substring(0, 3)
# --- m_decade = m_brailleCell.substring(4, end)
# --- whichDecade = 0
# --- if m_decade == '..':
# ---- if number: add (firstDecade.indexOf(m_signature) + 1) % 10 and continue
# --- else if m_decade == 'O.': whichDecade = 1
# --- else if m_decade == 'OO': whichDecade = 2
# --- else if m_decade == '.O': add (capital ? 'W' : 'w') and continue
# --- value = (firstDecade.indexOf(m_signature) + (capital ? 65 : 97) + (whichDecade * 10))
# --- if (whichDecade == 2) && (firstDecade.indexOf(m_signature) > 2): value -= 1
# --- add value as ascii character


# O.....

# array of strings corresponding to the first decade
# ["O...", "O.O.", "OO..", "OO.O", "O..O", "OOO.", "OOOO", "O.OO", ".OO.", ".OOO"]


import sys

def isBraille(input):
    if len(input) % 6 != 0:
        return False
    for i in input:
        if(i != 'O' and i != '.'):
            return False
    return True

def TranslateToBraille(englishInput):
    firstDecade = ["O...", "O.O.", "OO..", "OO.O", "O..O", "OOO.", "OOOO", "O.OO", ".OO.", ".OOO"]
    brailleOutput = ""

    i = 0
    while i < len(englishInput):
        m_char = englishInput[i]

        if(m_char.isalpha()):
            if(m_char.isupper()):
                brailleOutput += ".....O" # capital follows
                m_char = m_char.lower()
            alphabetIndex = ord(m_char) - 97
            
            if(alphabetIndex < 10):
                brailleOutput += firstDecade[alphabetIndex] + ".." # last two dots corresponding to 1st decade
            elif(alphabetIndex < 20):
                brailleOutput += firstDecade[alphabetIndex - 10] + "O." # last two dots corresponding to 2nd decade
            elif(alphabetIndex < 26 and alphabetIndex != 22):
                brailleOutput += firstDecade[(alphabetIndex - 20) - (1 if alphabetIndex > 22 else 0)] + "OO" # last two dots corresponding to 3rd decade
            else:
                brailleOutput += ".OOO.O" # special case for 'w'
        elif(m_char.isnumeric()):
            brailleOutput += ".O.OOO" # number follows
            while (m_char != ' '): # space character
                brailleOutput += firstDecade[(int(m_char) - 1) % 10] + ".."
                i += 1
                if (i == len(englishInput)):
                    break
                m_char = englishInput[i]
            if (i != len(englishInput)):
                brailleOutput += '......' # space character
        else:
            match m_char: # switch-case statement for other symbols
                case " ":
                    brailleOutput += '......' # space character
        
        i += 1

    return brailleOutput

def TranslateToEnglish(brailleInput):
    firstDecade = ["O...", "O.O.", "OO..", "OO.O", "O..O", "OOO.", "OOOO", "O.OO", ".OO.", ".OOO"]
    englishOutput = ""

    capital = False
    number = False

    for i in range(0, len(brailleInput), 6):
        m_brailleCell = brailleInput[i : i+6]
        if(m_brailleCell == ".....O"): # capital follows
            capital = True
            continue
        elif(m_brailleCell == ".O.OOO"): # number follows
            number = True
            continue
        elif(m_brailleCell == "......"): # space character
            number = False
            englishOutput += " "
            continue

        m_signature = m_brailleCell[0 : 4]
        m_decade = m_brailleCell[4 : 6]
        whichDecade = 0

        if(m_decade == ".."):
            if number:
                englishOutput += str((firstDecade.index(m_signature) + 1) % 10)
                continue
        elif(m_decade == "O."):
            whichDecade = 1
        elif(m_decade == "OO"):
            whichDecade = 2
        elif(m_decade == ".O"):
            englishOutput += 'W' if capital else 'w'
            continue
        
        value = (firstDecade.index(m_signature)) + (65 if capital else 97) + (whichDecade * 10)
        if (whichDecade == 2) and (firstDecade.index(m_signature) > 2):
            value -= 1 # account for 'w' special case
        englishOutput += chr(value)

        capital = False

    return englishOutput


def Translate(input):
    output = ""

    if(isBraille(input)):
        output = TranslateToEnglish(input)
    else:
        output = TranslateToBraille(input)

    return output


# main
numArgs = len(sys.argv)
inputStr = ""
for i in range(1, numArgs):
    inputStr += sys.argv[i]
    if(i != numArgs - 1):
        inputStr += ' '

result = Translate(inputStr)
print(result)