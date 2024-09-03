#Chris Beaucage
#Shopify Intern Challenge - Braille Translator
#2024/09/02

import sys
#import dictionaries to key alphatbetical characters to braille characters
import AlphabetToBraille
#import dictionaries to key braille characters to alphabetical characters
import BrailleToAlphabet
#import regex expressions, used to split braille into 6 character segments
import re

CAPITAL = '.....O'
DECIMAL = '.O...O'
NUMBER = '.O.OOO'
SPACER = '......'

#set list of args to variable
argList = sys.argv[1:]

#function to convert from alphabetical characters to braille
def alphabet_to_braille(input):
    
    result = ""
    for i in range(len(input)):

        #If a number is the first character, will print number delimiter without spacer
        if input[i] in AlphabetToBraille.numbers and i == 0:
            result += NUMBER + AlphabetToBraille.numbers.get(input[i])

        #If character is a number and previous character was not, will print number delimiter and include spacer
        if input[i] in AlphabetToBraille.numbers and not input[i-1] in AlphabetToBraille.numbers:
            result += SPACER + NUMBER + AlphabetToBraille.numbers.get(input[i])

        #If character is a number and previous character was, will print number without delimiter
        elif input[i] in AlphabetToBraille.numbers and input[i-1] in AlphabetToBraille.numbers:
            result += AlphabetToBraille.numbers.get(input[i])

        #If character is a capital letter and previous character was a number, will print capital delimiter and include spacer
        elif input[i].lower() in AlphabetToBraille.letters and input[i].isupper() and input[i-1] in AlphabetToBraille.numbers:
            result += SPACER + CAPITAL + AlphabetToBraille.letters.get(input[i].lower())

        #If character is a capital letter, will print capital delimiter
        elif input[i].lower() in AlphabetToBraille.letters and input[i].isupper():
            result += CAPITAL + AlphabetToBraille.letters.get(input[i].lower())

        #If character is a letter and previous character was a number, will include spacer
        elif input[i] in AlphabetToBraille.letters and input[i-1] in AlphabetToBraille.numbers:
            result += SPACER + AlphabetToBraille.letters.get(input[i])

        #If character is a letter, prints letter
        elif input[i] in AlphabetToBraille.letters:
            result += AlphabetToBraille.letters.get(input[i])

        #If character is punctuation, prints punctuation
        elif input[i] in AlphabetToBraille.punctuation:

            #Assumption made of decimal case, potentially does not account for edge cases
            #If punctuation is a period and is flanked by numbers on both sides, assume it is a decimal point and print decimal delimiter
            if input[i] == '.' and input[i-1] in AlphabetToBraille.numbers and input[i+1] in AlphabetToBraille.numbers:
                result += DECIMAL + AlphabetToBraille.punctuation.get(input[i])

            #If not assumed decimal, print punctuation
            else:
                result += AlphabetToBraille.punctuation.get(input[i])

        #This exists to cover any unexpected symbols that are not in the existing dictionary files, not ideal
        else:
            continue

    return result
    
#Define function to convert braille characters to alphabetical characters
def braille_to_alphabet(input):

    #remove any unwanted space characters
    nospace = input.replace(" ", "")
    #trim any whitespace on either end
    trim = nospace.strip()
    #use regex to segment the string into 6 characters to be interpreted as braille
    braille = re.findall('......',trim)

    result = ""

    #This section is not finished, many cases are not accounted for
    for i in range(len(braille)):

        #Bypass capital delimiters
        if braille[i] == CAPITAL:
            continue

        #Bypass numerical delimiters
        elif braille[i] == NUMBER:
            continue

        #Bypass decimal delimiters
        elif braille[i] == DECIMAL:
            continue

        #This seems inefficient
        #If segment is a letter and previous segment was capital delimiter, print letter as uppercase
        elif braille[i] in BrailleToAlphabet.letters and braille[i-1] == CAPITAL:
            result += BrailleToAlphabet.letters.get(braille[i]).upper() 

        #This does not account for sections where multiple segments are numbers
        #If segment is a number and previous segment was numerical delimiter, print as number
        elif braille[i] in BrailleToAlphabet.numbers and braille[i-1] == NUMBER:
            result += BrailleToAlphabet.numbers.get(braille[i])

        #If segment is a letter, print that alphabetical letter
        elif braille[i] in BrailleToAlphabet.letters:
            result += BrailleToAlphabet.letters.get(braille[i])
        
        #If segment is punctuation, print that symbol
        elif braille[i] in BrailleToAlphabet.punctuation:
            result += BrailleToAlphabet.punctuation.get(braille[i])

        #This exists to cover any unexpected combinations that are not in the existing dictionary files, not ideal
        else:
            continue

    return result

#define function to determine if string passed is alphabetical or braille
def braille_or_alphabet(input):

    #remove whitespace on front and end
    trim = input.strip()
    #slice first 6 characters
    check = trim[:6]

    #If first 6 characters exist in braille dictionaries, assume string is braille. Does not account for strings with mixed braille and alphabetical characters
    if check in BrailleToAlphabet.letters or check in BrailleToAlphabet.numbers or check in BrailleToAlphabet.punctuation or check == CAPITAL or check == NUMBER or check == DECIMAL:
        return braille_to_alphabet(input)
    
    #If not in braille dictionaires, assume string is alphabetical
    else:
        return alphabet_to_braille(input)
        

def run(input):

    braille_or_alphabet(input)


if __name__ == '__main__':
    
    #Join any args into single string to be passed
    input = ''.join(argList)

    print(run(input))







