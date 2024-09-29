import sys

# For simplicity, we will consider each braille character to be a 6-dimensional row vector
# We start by building an English - Braille lookup table.

# We note that the letter A to J form the "base set"
def buildLookupTable():
    table = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......",
    }

    # In the range of letters ["k", ..., "t"], the ith letter can be related to the ith letter in the range ["a", ..., "j"]:
    rangeTenTwenty = [chr(i) for i in range(ord('k'), ord('t') + 1)] # the ten next letters after j (after the base set)
    for letter in rangeTenTwenty:
        base_braille = list(table[chr(ord(letter) - 10)]) # get the braille rep of the corresponding letter in the base set
        base_braille[4] = 'O' # the rule relating the letters in the base set to those in rangeTenTwenty is that the '.' at index 4 is replaced by a 'O'
        table[letter] = "".join(base_braille)

    # Same concept for the letters ["u", ..., "v"] 
    rangeTwentyTwentySix = [chr(i) for i in range(ord('u'), ord('z') + 1)] # the two next letters after t 
    offset = 10

    for letter in rangeTwentyTwentySix:
        if letter == 'w':
            table[letter] = ".OOO.O" # w is an exception to the rule we came up with
            offset = 11 # the bases of the letters after w are then offset by 1 more 
            continue

        base_braille = list(table[chr(ord(letter) - offset)]) # get the braille rep of the corresponding letter in the base set
        base_braille[5] = 'O' # '.' at index 5 is replaced by a 'O'
        table[letter] = "".join(base_braille)


    # add the digits
    numberFlag = ".O.OOO" # when met, everything that follows is a number UNTIL space pattern
    decimalFlag = ".O...O" # signifies a fractional part coming up; continues until space is met. 
    for digit in range(10):
        if digit == 0:
            table[str(digit)] = "n" + table["j"]
            continue

        table[str(digit)] = "n" + table[chr(ord('a') + digit - 1)] 

    # add capital letters
    capitalFlag = ".....O"
    # when met, only next letter is capital
    for ascii in range(ord('a'), ord('z') + 1):
        table[chr(ascii).upper()] = capitalFlag + table[chr(ascii)]

    # Reverse table into a Braille to English table
    braille_table = {}
    for key, braille in table.items():
        braille_table[braille] = key

    return table, braille_table


# a function to translate English input to Braille
def englishToBraille(table:dict, inputString:str):
    capitalFlag = ".....O"
    numberFlag = ".O.OOO"
    decimalFlag = ".O...O"
    # parse input char by char 
    # for each char, translate i
    translation = ""
    inputArray = list(inputString)
    index = 0

    while index < len(inputArray):
        character = inputArray[index]
        # check if number
        if '0' <= character <= '9':
            # we have a digit
            translation += numberFlag + table[str(character)][1:] # gotta remove the 'n' prefix
            # we keep going until we see a space 
            for j in range(index+1, len(inputArray)):
                if inputArray[j] == " ":
                    translation += table[" "]
                    index = j + 1 # we will translate the char right after the space
                    break
                else:
                    if (inputArray[j] == ","):
                        translation += decimalFlag # + table[inputArray[j]] # do we add the regular decimal even after the flag, or only the flag
                    else:
                        translation += table[inputArray[j]][1:]
                    index = j # index has got to keep up

        elif 'A' <= character <= 'Z':
            # we have an uppercase letter
            translation += capitalFlag + table[str(character).lower()]

        else:
            # we have a special character or a lowercase letter 
            translation += table[str(character)]

        index += 1

    return translation


def brailleToEnglish(braille_table:dict, inputString:str):
    pass
    # parse 6 characters at a time
    inputArray = list(inputString)
    if len(inputArray) % 6 != 0:
        return "Invalid Braille"
    
    groups = ["".join(inputArray[i: i + 6]) for i in range(0, len(inputArray), 6)] # split into groups, 6 charss at a time
    
    capitalFlag = ".....O"
    numberFlag = ".O.OOO"
    decimalFlag = ".O...O"

    translation = ""
    index = 0

    print(groups)

    while index < len(groups):
        if groups[index] == capitalFlag:
            translation += braille_table[groups[index] + groups[index+1]]
            index += 1  # skip the letter after the flag

        elif groups[index] == numberFlag:
            # If number flag is found
            index += 1
            while index < len(groups):
                translation += braille_table["n" + groups[index]]  # Use "?" for unrecognized Braille
                index += 1
                if index < len(groups) and groups[index - 1] == " ":
                    break  # Stop if we hit a space

        elif groups[index] == decimalFlag:
            # If decimal flag is found, treat next group as a decimal
            index += 1
            if index < len(groups):
                translation += braille_table[groups[index]]
                index += 1  # Move past the number after the flag

        else:
            # Normal character translation
            translation += braille_table[groups[index]]

        index += 1  # Move to the next group


    return translation

def detectLang(str):
    for char in str:
        if char != "O" and char != ".":
            return "English"
        
    return "Braille"

def main():
    englishBrailleTable, brailleEnglishTable = buildLookupTable()

    toTranslate = sys.argv[0]
    res = ""
    if detectLang(toTranslate) == "English":
        res = englishToBraille(englishBrailleTable, toTranslate) 
    else:
        res = brailleToEnglish(brailleEnglishTable, toTranslate)

    return res 


if __name__ == "__main__":
    main()
         