import sys

SPACE = "......"
NUMBER_FOLLOWS = ".O.OOO"
CAPITAL_FOLLOWS = ".....O"

english_to_braille = {
    "A" : "O.....",
    "B" : "O.O...",
    "C" : "OO....",
    "D" : "OO.O..",
    "E" : "O..O..",
    "F" : "OOO...",
    "G" : "OOOO..",
    "H" : "O.OO..",
    "I" : ".OO...",
    "J" : ".OOO..",
    "K" : "O...O.",
    "L" : "O.O.O.",
    "M" : "OO..O.",
    "N" : "OO.OO.",
    "O" : "O..OO.",
    "P" : "OOO.O.",
    "Q" : "OOOOO.",
    "R" : "O.OOO.",
    "S" : ".OO.O.",
    "T" : ".OOOO.",
    "U" : "O...OO",
    "V" : "O.O.OO",
    "W" : ".OOO.O",
    "X" : "OO..OO",
    "Y" : "OO.OOO",
    "Z" : "O..OOO",
    "1" : "O.....",
    "2" : "O.O...",
    "3" : "OO....",
    "4" : "OO.O..",
    "5" : "O..O..",
    "6" : "OOO...",   
    "7" : "OOOO..",
    "8" : "O.OO..",
    "9" : ".OO...",
    "0" : ".OOO.."
}

braille_letters = {
    "O.....": "A",
    "O.O...": "B",
    "OO....": "C",
    "OO.O..": "D",
    "O..O..": "E",
    "OOO...": "F",
    "OOOO..": "G",
    "O.OO..": "H",
    ".OO...": "I",
    ".OOO..": "J",
    "O...O.": "K",
    "O.O.O.": "L",
    "OO..O.": "M",
    "OO.OO.": "N",
    "O..OO.": "O",
    "OOO.O.": "P",
    "OOOOO.": "Q",
    "O.OOO.": "R",
    ".OO.O.": "S",
    ".OOOO.": "T",
    "O...OO": "U",
    "O.O.OO": "V",
    ".OOO.O": "W",
    "OO..OO": "X",
    "OO.OOO": "Y",
    "O..OOO": "Z",
    ".....O": "capital follows",
    ".O.OOO": "number follows",
    "......": "space"
}

braille_nums = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0"
}

# we check if it is english or braille
# false = english
# true = braille
def writingsystem_check(text):
    if len(text) % 6 != 0:
        return False

    # loop through input by steps of 6
    for i in range(0, len(text), 6):
        # take only 6 characters to compare
        txt = text[i:i+6]
        if(txt not in braille_letters and txt not in braille_nums):
            return False
    return True

def translate(text):
    if(writingsystem_check(text) == False):
        # it is an english sentence so we translate to braille
        result = ""
        is_number = False
        for i in range(0,len(text)):
            # if capital we add the capital braille equivalent and then the letter
            if(text[i].isupper()):
                result+=CAPITAL_FOLLOWS
                result+=english_to_braille[text[i]]
            # if it is a number we add the number follows equivalent and then the number (only if it is the first number so we check if there isnt already a num_follow)
            elif(text[i].isdigit() and is_number == False):
                result+=NUMBER_FOLLOWS
                result+=english_to_braille[text[i]]
                # we put is_number true in case next character is also a number
                is_number = True
            # check if there is space
            elif(text[i].isspace()):
                result+=SPACE
                is_number = False
            else:
                result+=english_to_braille[text[i].upper()]
        return result
    else:
        #if it is braille we translate to english
        result = ""
        is_number = False
        is_capital = False
        # like in writingsystem_check we go by steps of 6 and then take only 6 characters to compare
        for i in range(0,len(text), 6):
            txt = text[i:i+6]
            # if it is a number follow then we set to true so we can use the braille_num dictionnary
            if txt == NUMBER_FOLLOWS:
                is_number = True
            elif txt == CAPITAL_FOLLOWS:
                is_capital = True
            elif txt == SPACE:
                result+=" "
                is_number = False
            elif is_capital:
                result += braille_letters[txt]
                is_capital = False
            elif is_number:
                result+=braille_nums[txt]
            else:
                result+=braille_letters[txt].lower()
        return result

def main():
    input_text = " ".join(sys.argv[1:])
    print(translate(input_text))

if __name__ == "__main__":
    main()
