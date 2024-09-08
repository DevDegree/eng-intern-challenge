braille = {"a":"O.....", "b":"O.O...", "c":"OO....", "d":"OO.O..", "e":"O..O..", "f":"OOO...", "g":"OOOO..", "h":"O.OO..", "i":".OO...", "j":".OOO..", "k":"O...O.",
            "l":"O.O.O.", "m":"OO..O.", "n":"OO.OO.", "o":"O..OO.", "p":"OOO.O.", "q":"OOOOO.", "r":"O.OOO.", "s":".OO.O.", "t":".OOOO.", "u":"O...OO","v":"O.O.OO",
            "w":".OOO.O", "x":"OO..OO", "y":"OO.OOO", "z":"O..OOO", ".":"..OO.O", ",":"..O...", "?":"..O.OO", "!": "..OOO.", ":":"..OO..", ";":"..O.O.",
            "-":"...OO","/":".O..O.", "<":".OO..O", ">":"O..OO.", "(":"O.O..O", ")":".O.OO.", " ":"......"} # dictionary for Braille letters, punctuation marks and spaces


braille_numbers = {"1":"O.....", "2":"O.O...", "3":"OO....", "4":"OO.O..", "5":"O..O..", "6":"OOO...", "7":"OOOO..", "8":"O.OO..", "9":".OO...", "0":".OOO.."} # dictionary for Braille numbers
capital_follows = ".....O"
number_follows = ".O.OOO"

import sys
num_of_args = len(sys.argv)
input = ""
for j in range(1, num_of_args):
    input += sys.argv[j] + " "
input = input.strip()

def englishtobraille(input): # this function will be called if the string is English
    firstnumber = True # boolean to keep track of whether a symbol is the first of some consecutive number symbols
    brailestring = "" # stores converted Braille string
    for char in input: # loops through characters
        if (not char.isdigit()): # checks if the character is a letter or symbol
            if (char.isupper()): # the character is upper case so an uppercase follows symbol needs to be inserted
                brailestring += capital_follows
            brailestring+=braille[char.lower()] # gets the corresponding Braille symbol
            if (char == " "): # a space has been encountered, so any numbers that follow will need to be preceded by a number follows symbol
                firstnumber = True
        else: # the character is a number
            if(firstnumber): # this is the first number in a consecutive group so a number follows symbol needs to be inserted
                brailestring+=number_follows
                firstnumber=False # indicates that any following consecutive numbers are not the first in their group so no number follows symbol will be inserted

            brailestring+=braille_numbers[char] # gets the corresponding Braille symbol

    return(brailestring)


def brailletoenglish(input): # this function will be called if the string is Braille
    englishstring = "" # stores converted English string
    next_is_num = False # boolean to keep track of whether the following consecutive symbols should be interpreted as numbers
    next_is_cap = False # boolean to keep track of whether the next symbol should be interpreted as a capital letter

    list_of_braillealphasandsymbolsvalues = list(braille.values()) # list of Braille symbols for letters, punctuation marks and spaces
    list_of_braillenumbersvalues = list(braille_numbers.values()) # list of Braille symbols for numbers
    list_of_braillealphasandsymbolskeys = list(braille.keys()) # list of English letters, punctuation marks and spaces
    list_of_braillenumberskeys = list(braille_numbers.keys()) # list of numbers

    num_of_symbols = len(input) // 6 # gets the number of symbols in the input string

    start_index = 0 # will keep track of the start index of the current symbol in the input string
    end_index = 6 # will keep track of the (end + 1) index of the current symbol in the input string

    for i in range(num_of_symbols): # loops through the input string
        symbol = input[start_index:end_index] # gets each 6 character braille symbol

        if (symbol == "......"): # checks if the current symbol is a space 
            next_is_num = False
            englishstring += " "
        elif (symbol == number_follows): # checks if the current symbol is a number follows symbol
            next_is_num = True
        elif (symbol == capital_follows): # checks if the current symbol is a capital follows symbol
            next_is_cap = True
        else:
            if (next_is_num): # checks if the current symbol is supposed to be interpreted as a number
                index_of_num = list_of_braillenumbersvalues.index(symbol) # gets the index of the Braille symbol in the list
                englishstring += list_of_braillenumberskeys[index_of_num] # uses the index to find the corresponding number in the list of numbers
            elif (next_is_cap): # checks if the current symbol is supposed to be interpreted as a capital letter
                index_of_letterorsymbol = list_of_braillealphasandsymbolsvalues.index(symbol) # gets the index of the Braille symbol in the list
                englishstring += list_of_braillealphasandsymbolskeys[index_of_letterorsymbol].upper() # uses the index to find the corresponding English letter/punctuation mark and makes it upper case
                next_is_cap = False
            else:
                index_of_letterorsymbol = list_of_braillealphasandsymbolsvalues.index(symbol) # gets the index of the Braille symbol in the list
                englishstring += list_of_braillealphasandsymbolskeys[index_of_letterorsymbol] # uses the index to find the corresponding English letter/punctuation mark
        
        start_index+=6 # updates the indexes so the next 6 character braille symbol can be accessed
        end_index+=6

    return(englishstring)

def main():
    for character in input: # loops through the characters in the input string
        english = False
        if character in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ1234567890,?!:;-/<>() ": # checks if any of the characters are letters, numbers or punctuation marks (excluding 0 and .) which means the input is English
            english = True
            break

    if (english): 
        return(englishtobraille(input))
    elif (not english):
        return(brailletoenglish(input))

    
print(main())
