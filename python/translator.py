import sys #to run the command line interface
#The comments I've added are to explain the code and how it works.
#lines 4 through 64 are the dictionaries that will be used to translate the text to braille
RULES_TO_BRAILLE={
    'capital':'.....O',
    'decimal':'.O...O',
    'number':'.O.OOO'
}
SYMBOLS_TO_BRAILLE={
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
    ')':'.O.OO.',
    ' ':'......'
}
LETTERS_TO_BRAILLE={
    'a':'O.....',
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
    'z':'O..OOO'
}
NUMBERS_TO_BRAILLE={
    '1':'O.....',
    '2':'O.O...',
    '3':'OO....',
    '4':'OO.O..',
    '5':'O..O..',
    '6':'OOO...',
    '7':'OOOO..',
    '8':'O.OO..',
    '9':'.OO...',
    '0':'.OOO..',     
}

#Lines 66 through 70 are the dictionaries that will be used to translate the braille to text
BRAILLE_TO_LETTERS = {v: k for k, v in LETTERS_TO_BRAILLE.items()}
BRAILLE_TO_NUMBERS = {v: k for k, v in NUMBERS_TO_BRAILLE.items()}
BRAILLE_TO_SYMBOLS = {v: k for k, v in SYMBOLS_TO_BRAILLE.items()}
BRAILLE_TO_RULES = {v: k for k, v in RULES_TO_BRAILLE.items()}

#Checking whether the text is braille or not by just checking if the text contains any character other than 'O' and '.'
#Braille text will only contain 'O' and '.' characters
def check_input(text):
    for char in text:
        if char!="O" and char!=".":
            return english_to_braille(text)
    return braille_to_english(text)

#Translating from English to Braille
def english_to_braille(text):
    result=''
    isNumber = False
    for char in text:
        if char.isalpha():
            isNumber = False
            if char.isupper(): #If character is uppercase, then add the capital rule before the letter
                result+=RULES_TO_BRAILLE['capital'] 
            result+=LETTERS_TO_BRAILLE[char.lower()]
        elif char.isdigit():
            if isNumber == False: 
                result+=RULES_TO_BRAILLE['number']+NUMBERS_TO_BRAILLE[char] #Adding the number rule before the number
                isNumber = True
            else:
                result+=NUMBERS_TO_BRAILLE[char]
        elif (char=='.'):
            if isNumber==True:
                result+=RULES_TO_BRAILLE['decimal']
            result+=LETTERS_TO_BRAILLE[char]
        elif (char == " "):
            result+='......' #If there is a space, then stop the number rule
            isNumber = False
        elif char in SYMBOLS_TO_BRAILLE:
            result+=SYMBOLS_TO_BRAILLE[char]    
    return result

#Converting from Braille to English
def braille_to_english(text): 
    phrase = [text[i:i+6] for i in range(0, len(text), 6)]
    isNumber = False
    isCaps = False
    result = ''

    for word in phrase: 
        if word in BRAILLE_TO_RULES:
            rule = BRAILLE_TO_RULES[word]
            if rule == 'capital': #Checking if the character is uppercase
                isCaps = True
            elif rule == 'number': #Checking if the character is a number
                isNumber = True
            elif rule == 'decimal': #Checking if the character is a decimal
                result += '.'
        elif isNumber:
            if word == '......':  # If there is a space, then stop the number rule
                isNumber = False
                result += ' '
            else:
                result += BRAILLE_TO_NUMBERS.get(word, '')  
        elif isCaps:
            result += BRAILLE_TO_LETTERS.get(word, '').upper()
            isCaps = False
        else:
            result += BRAILLE_TO_SYMBOLS.get(word, BRAILLE_TO_LETTERS.get(word, '')) 

    return result

def main():
    if len(sys.argv) < 2:
        return
    text = ' '.join(sys.argv[1:])
    result = check_input(text)
    print(result)

if __name__ == "__main__":
    main()
    