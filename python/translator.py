import sys
"""
-- Info & Assumptions --
Braille Translator,
- Hash maps we used to map from braille to english and english to braille.
- 1 main assumption was made for the 'o' and '>': There was a numbers mode, if the program was in
a sequence of numbers a '>' would be inserted. If we see a 'space'(......) that means numbers mode is off, and if we
encounter a 'O..OO.' that means we insert a 'o' when we are not in numbers mode while read our code.

"""

#dict mapping braille to eng for a to z and the space
braille_English = {
    'O.....':'a', "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z",
    "......": ' '
}

#dict mapping Braille codes to punctuation and special signs
signs_brailleToEng = {
    "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":",
    "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<", "O..OO.": ">",
    "O.O..O": "(", ".O.OO.": ")",
}

#dict mapping Braille codes to numbers (with "NUMBER" mode prefix)
numbers_brailletoNumbers = {
    ".O.OOOO.....": "1", ".O.OOOO.O...": "2", ".O.OOOOO....": "3", ".O.OOOOO.O..": "4", ".O.OOOO..O..": "5",
    ".O.OOOOOO...": "6", ".O.OOOOOOO..": "7", ".O.OOOO.OO..": "8", ".O.OOO.OO...": "9", ".O.OOO.OOO..": "0"
}

#reverse dict mapping for English to Braille conversion
english_Braille = {v: k for k, v in braille_English.items()}

#rictionary for converting English numbers to Braille
numbers_EngToBraille = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "OO..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

#reverse dictionary mapping for English signs to Braille
signs_EngToBraille = {v: k for k, v in signs_brailleToEng.items()}



#test3 h1>2
#O.OO...O.OOOO.....O..OO.O.O...
#O.OO...O.OOOO.....O..OO.O.O...

#test4 1>2
#.O.OOOO.....O..OO.O.O...

#FROM 1>2
#.O.OOOO.....O..OO.O.O...

#test Hello world 
#supp .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..
#mine .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..


#test Abc 123 xYz
#supp .....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO
#mine .....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO
#mine 

#test 42
#supp .O.OOOOO.O..O.O...
#mine .O.OOOOO.O..O.O...

#test Abc 123
#supp .....OO.....O.O...OO...........O.OOOO.....O.O...OO....
#mine .....OO.....O.O...OO...........O.OOOO.....O.O...OO....

#check if the string is in eng or braille
def translate(word):
    brailleToEngB = True
    for c in word:
        if c == 'O' or c == '.':
            continue
        else:
            brailleToEngB = False
    #we checked every single char, if one of them was not '.' or 'O' that means we have to go from eng to braille
    if brailleToEngB:
        # braille to Eng code
        return brailleToEng(word)
    else:
        # eng to braille code
        return engToBraille(word)


#function to translate Braille to English
def brailleToEng(word):
    res = []
    left = 0
    #this bool will put the program into numbers mode until we touch the end or we have a space somewhere
    in_numbers_mode = False

    while left < len(word):
        #our current code
        currString = word[left:left+6]
        #code right after currString
        nextChar = word[left+6:left+12] if left + 12 <= len(word) else ""

        # case where the code tells us that it will be a capital letter
        if currString == ".....O":  
            left += 6
            currString = word[left:left+6]
            res.append(braille_English.get(currString, '').upper())
            in_numbers_mode = False

        # Handle number sequences
        elif currString == '.O.OOO':
            in_numbers_mode = True
            left += 6
            #this while loop will go and append numbers until we break because we have seen a space
            while left < len(word):
                currString = word[left:left + 6]
                if ".O.OOO" + currString in numbers_brailletoNumbers.keys():
                    res.append(numbers_brailletoNumbers.get(".O.OOO" + currString, ''))
                #added a case here that if we have to put either a 'o' or '>' we check if the next char is a space. If we have a space we will append an 'o'.
                elif currString == "O..OO.":
                    if nextChar != "......":
                        res.append(">")
                    else:
                        res.append("o")
                #break case, we have seen a space
                elif currString == "......":
                    res.append(" ")
                    in_numbers_mode = False
                    break
                elif currString in signs_brailleToEng:
                    res.append(signs_brailleToEng.get(currString, ''))
                left += 6

        else:
            res.append(braille_English.get(currString, ''))
            in_numbers_mode = False
        
        left += 6

    return ''.join(res)


#function to translate English to Braille
def engToBraille(word):
    res = []
    in_numbers_mode = False

    for char in word:
        
        #case capital letters
        if char.isalpha():
            if char.isupper():
                res.append('.....O' + english_Braille.get(char.lower(), ''))
            else:
                res.append(english_Braille.get(char, ''))
            in_numbers_mode = False
        
        #handle digits
        elif char.isdigit() or in_numbers_mode:
            if not in_numbers_mode:
                res.append('.O.OOO')
                in_numbers_mode = True
            if char == ' ':
                res.append('......')
            if char.isdigit():
                res.append(numbers_EngToBraille.get(char, ''))
            else:
                res.append(signs_EngToBraille.get(char, ''))

        #handle signs in digit mode
        elif char in signs_EngToBraille and in_numbers_mode:
            res.append(signs_EngToBraille.get(char, ''))

        #handle signs outside digit mode
        elif char in english_Braille and not in_numbers_mode:
            res.append(english_Braille.get(char, ''))
        
        #handle spaces
        elif char == ' ':
            res.append('......')
            in_numbers_mode = False

    return "".join(res)



if __name__ == "__main__":
    input_string = ' '.join(sys.argv[1:])
    output_string = translate(input_string)
    print(output_string)