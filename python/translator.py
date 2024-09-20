import string
import sys

phrase = sys.argv[1]

def translator(phrase):
    mode = ""
    alphabet = list(string.ascii_letters)
    # Determine if string is Braille or English
    for i in range(len(phrase)):
        for j in range(len(alphabet)):
            if phrase[i] in alphabet or phrase[i].isdigit():
                mode = "English"
            else:
                mode = "Braille"
    if mode == "English":
        output = englishtToBraille(phrase)
    else:
        output = brailleToEnglish(phrase)
    return output

def brailleToEnglish(phrase):
    # Braille to English mappings
    alphabetAToJ = {
        "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
        "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j"
    }
    alphabetKToT = {
        "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
        "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t"
    }
    alphabetUToZ = {
        "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", "O..OOO": "z"
    }
    alphabet = {**alphabetAToJ, **alphabetKToT, **alphabetUToZ}
    numbersOneToNine = {
        "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
        "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
    }
    symbolsAndSpace = {
        "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":",
        "..O.O.": ";", "....OO": "-", "./../.": "/", ".OO..O": "<", "O..OO.": ">",
        "O.O..O": "(", ".O.OO.": ")", "......": " "
    }
    capitalFollows = ".....O"
    numberFollows = ".O.OOO"
    # Split the string into 6 character chunks
    braille = [phrase[i:i+6] for i in range(0, len(phrase), 6)] #This takes 
    translated_braille = ""

    i = 0
    while i < len(braille):
        # Check if letter or number
        if braille[i] in alphabet:
            # Capitalize if letter
            if i > 0 and braille[i-1] == capitalFollows:
                translated_braille += alphabet.get(braille[i], "").capitalize()
            else:
                translated_braille += alphabet.get(braille[i], "")
            i += 1
            # If numberFollows signal then run until space
        elif braille[i] == numberFollows:
            i += 1
            #Concatenate numbers until you find a space
            while i < len(braille) and braille[i] != "......":
                translated_braille += numbersOneToNine.get(braille[i], "")
                i += 1
            continue
        else:
            translated_braille += symbolsAndSpace.get(braille[i], "")  
            i += 1
    return translated_braille

def englishtToBraille(phrase): 

    capitalizedAlphabet = list(string.ascii_letters.capitalize())
    
    #Dictionary
    alphabetAToJ = {
        "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
        "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j"
    }
    alphabetKToT = {
        "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
        "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t"
    }
    alphabetUToZ = {
        "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", "O..OOO": "z"
    }
    alphabet = {**alphabetAToJ, **alphabetKToT, **alphabetUToZ}

    numbersOneToNine = {
        "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
        "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
    }
    symbolsAndSpace = {
        "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":",
        "..O.O.": ";", "....OO": "-", "./../.": "/", ".OO..O": "<", "O..OO.": ">",
        "O.O..O": "(", ".O.OO.": ")", "......": " "
    }
    capitalFollows = ".....O"
    numberFollows = ".O.OOO"
    # Reverse dictionaries
    reversedAlphabet = {v: k for k, v in alphabet.items()}
    reversedNumbers = {v: k for k, v in numbersOneToNine.items()}
    reversedSymbols = {v: k for k, v in symbolsAndSpace.items()}

    translated_english = ""
    i = 0
    while i < len(phrase):
        # Letter to Braille Logic
        if phrase[i].isalpha():
            if phrase[i].isupper():
                translated_english += capitalFollows + reversedAlphabet.get(phrase[i].lower(), "")
            else:
                translated_english += reversedAlphabet.get(phrase[i], "")
            i += 1
        elif phrase[i].isdigit():
            translated_english += numberFollows
            while i < len(phrase) and phrase[i].isdigit():
                translated_english += reversedNumbers.get(phrase[i], "")
                i += 1
        else:
            translated_english += reversedSymbols.get(phrase[i], " ")
            i += 1
    return translated_english