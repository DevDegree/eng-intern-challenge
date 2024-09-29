# Python function to translate Braille to English

'''
Problem Statement: Build a command line application that translates a given string from Braille to English and vice versa.

Solution Design:

1) Define Braille and English mappings
    a) Mappings for English alphabet, numbers, spaces, and punctuation to Braille using 0s and '.'s

2) Handle Capitalization and Numbers
    a) Special Braille characters denote that the following characters should be either capitalized or treated as numbers

3) Detect Input Type
    a) Detect whether Braille, English or wrong input

4) Translate
    a) Convert to the other language

5) Command-line Argument
    a) Accept a string as a command-line argument and output only the translated string
'''

import sys
import string

# Dictionary for mapping characters to Braille and vice-versa
braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....",
    "d": "OO.O..", "e": "O..O..", "f": "OOO...",
    "g": "OOOO..", "h": "O.OO..", "i": ".OO...",
    "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.",
    "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO",
    "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO", 
    "1": "O.....", "2": "O.O...", "3": "OO....",
    "4": "OO.O..", "5": "O..O..", "6": "OOO...",
    "7": "OOOO..", "8": "O.OO..", "9": ".OO...",
    "0": ".OOO..",
    "upper": ".....O", "number": ".O.OOO"
}

alphabet ={
    "O.....": "a", "O.O...": "b", "OO....": "c",
    "OO.O..": "d", "O..O..": "e", "OOO...": "f",
    "OOOO..": "g", "O.OO..": "h", ".OO...": "i",
    ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
    "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r",
    ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u",
    "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
    "OO.OOO": "y", "O..OOO": "z",
    "......": " "
}

numbers ={
    "O.....": "1", "O.O...": "2", "OO....": "3",
    "OO.O..": "4", "O..O..": "5", "OOO...": "6",
    "OOOO..": "7", "O.OO..": "8", ".OO...":"9",
    ".OOO..":"0",
}

def main():

    if((sys.argv[1].isalpha()== True) or (sys.argv[1].isdigit() == True) ):
        toBraille() # Convert to Braille if input is English or numbers
    else: 
        toEnglish() # Convert Braille to English

    return


def toBraille():
    result: string = ""
    index: int = 1

    while(index < len(sys.argv)):
        if(index>1):
            result += "......" # Add space between words in Braille

        if (sys.argv[index].isalpha() == True):
            result += alpha(sys.argv[index])
        else:
            result += digit(sys.argv[index])

        index+=1


    print(result)
    return


def alpha(letters: string):
    sequence: string =""
    for letter in letters:
        if(letter.isupper() == True):
            sequence += braille["upper"]
        sequence += braille[letter.lower()]

    return sequence

def digit(numbers: string):
    sequence: string = braille["number"]
    for number in numbers:
        sequence += braille[number]

    return sequence

def toEnglish():
    result: string = seq(sys.argv[1])

    print(result)
    return

def seq(sequence: string):
    result: string = ""
    firstIndex: int = 0

    while (firstIndex < len(sequence) -1):
        # Check for the capital flag
        if(sequence[firstIndex:(firstIndex+6)] == ".....O"): 
            firstIndex +=6
            result += alphabet[sequence[firstIndex:(firstIndex+6)]].capitalize()
        elif(sequence[firstIndex:(firstIndex+6)] == ".O.OOO"): # Check for the number flag
            firstIndex +=6
            while( (sequence[firstIndex:(firstIndex+6)] != "......") and (firstIndex < len(sequence) -1)):
                result += numbers[sequence[firstIndex:(firstIndex+6)]]
                firstIndex +=6

        else:
            result += alphabet[sequence[firstIndex:(firstIndex+6)]].lower()

        firstIndex +=6 # Move to the next 6-character Braille cell

    return result

if __name__ == "__main__":
    main()



