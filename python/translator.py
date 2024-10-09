import sys

# Map from braille to English, numerals are separated due to duplicated key
bteMap = {"O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
          "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
          "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
          "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
          "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
          "O..OOO": "z", "......": " ", "..OO.O": ".", "..O...": ",", "..O.OO": "?",
          "..OOO.": "!", "..OO..": ":", "..O.O.": ";", "....OO": "-", ".O..O.": "/",
          ".OO..O": "<", "O.O..O": "(", ".O.OO.": ")", ".....O": "Capital follows",
          ".O.OOO": "Number follows"}
numMap = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
}
# Map from English to braille
etbMap = {**{v: k for k, v in bteMap.items()},**{v: k for k, v in numMap.items()}}


def brailleToEng(string):
    output = ""
    i = 0
    while i < len(string):  # Iterate over the input
        char = string[i:i + 6]  # Extract a symbol
        if char == ".....O":  # Next character is capital
            i += 6
            char = string[i:i + 6]
            output += bteMap[char].upper()  # Concatenate the corresponding English letter to our output string
        elif char == ".O.OOO":  # All characters following are numbers until space found
            i += 6
            while i < len(string) and string[i:i + 6] != "......": # Keep going until reaches the end or a space
                output += numMap[string[i:i + 6]]   # Append
                i += 6
            if string[i:i + 6] == "......":
                output += " "
        else:
            output += bteMap[char]
        i += 6  # Move to next group of characters
    return output

def engToBraille(string):
    output = ""
    number = False
    for i in string:    # Iterative over input
        if i.isalpha():     # If character is a letter
            if i.isupper():     # Add "capital follows" symbol if needed
                output += ".....O"
            output += etbMap[i.lower()]
        elif i.isdigit():   # If character is a number
            if not number:  # If previously not in number mode, enter first
                output += ".O.OOO"
                number = True
            output += etbMap[i]
        else:   # All other symbols
            number = False
            output += etbMap[i]
    return output


if __name__ == "__main__":
    args = ' '.join(sys.argv[1:])  # Convert input to string
    # Determine function to run
    if all(c in '.O' for c in args):
        print(brailleToEng(args))  # If input consists of only '.' and 'O'
    else:
        print(engToBraille(args))
