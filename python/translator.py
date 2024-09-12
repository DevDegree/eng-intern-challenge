

braille_alpha = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
    "......": " ",

    ".....O": "capital follows",
    ".O.OOO": "number follows",
}

braille_num_special = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9", 
    ".OOO..": "0",
    "..OO.O": ".",

}

def braille_or_eng(input: str ) -> str:
    # if input is braille, return eng
    # if input is eng, return braille
    if len(set(input)) == 2 and (''.join(set(input)) == ".O" or ''.join(set(input)) == "O." ):
        return "eng" 

    return "braille"

def parse_input(input: str) -> str:

    ans = ""

    num_flag = -1
    capital_flag = -1

    if braille_or_eng(input) == "eng": 
        # input is in braille, must convert to eng
        for i in range(6, len(input)+1, 6):
            # use string slicing to get a the 6 char braille substring  
            substr = input[i-6: i]

            # check if number follows
            if braille_alpha[substr] == "number follows":
                num_flag = 1
                continue

            # check if capital follows
            if braille_alpha[substr] == "capital follows":
                capital_flag = 1
                continue

            # check for the various flags
            if num_flag == 1:
                # if the next is a num, then read the substr from number dict, assumes all future chars are nums, except until a space
                ans += braille_num_special[substr]
            elif capital_flag == 1:
                ans += braille_alpha[substr].upper()
                capital_flag = -1
            else:
                if braille_alpha[substr] == " ":
                    num_flag = -1
                ans += braille_alpha[substr]

    else:
        # otherwise, input is in eng, must convert to braille

        # loop through each character, convert that into 
        for i in range (len(input)):
            if input[i].isupper():
                ans += ".....O"
                ans += list(braille_alpha.keys())[list(braille_alpha.values()).index(input[i].lower())]
            elif input[i].isnumeric():

                # only if this is the first number, add the "number follows" braille code
                if num_flag == -1:
                    ans += ".O.OOO"
                    num_flag = 1

                ans += list(braille_num_special.keys())[list(braille_num_special.values()).index(input[i])]
            else:

                # sets the num flag to -1, indicating sequence of numbers has stopped
                if input[i] == " ":
                    num_flag = -1

                ans += list(braille_alpha.keys())[list(braille_alpha.values()).index(input[i])]
            
            
    return ans



if __name__ == "__main__":
    
    # read the input from python
    text = input()


    print(parse_input(text))


