import sys

# Dict containing all the braille codes to alphabet, and the num and capital signal codes
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

# dict containing all the numbers
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
}



def braille_or_eng(input: str ) -> str:
    """determines whether the input is braille or english, used to decode input string

        Parameters:
        - input (str): the input coded string (either braille or eng)

        Returns:
        - str: string containing either braille or eng, what the input text must BE TRANSLATED TO
    """

    # if input is braille, return eng
    # if input is eng, return braille
    if len(set(input)) == 2 and (''.join(set(input)) == ".O" or ''.join(set(input)) == "O." ):
        return "eng" 

    return "braille"

def parse_input(input: str) -> str:
    """Parses the input string, determines if braille or eng, then looks up coresponding values in the two dictionarys
        braille_alpha and braille_num_special to convert between the two languages.

        Parameters: 
        - input (str): the input coded string (either braille or eng)
                
        Returns:
        - str: The decoded string of text
    """
    
    ans = ""

    # used for tracking if number follows or capital letter follows
    num_flag = -1
    capital_flag = -1

    if braille_or_eng(input) == "eng": 
        # input is in braille, must convert to eng

        for i in range(6, len(input)+1, 6):
            # use string slicing to get the 6 char braille substring  
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
                # if the next char is a capital, use .upper(), the capital flag is turned off, so immediately lowercased 
                ans += braille_alpha[substr].upper()
                capital_flag = -1
            else:
                # if the substring is " " (space), we know that the sequence of numbers has stopped, set it to -1
                if braille_alpha[substr] == " ":
                    num_flag = -1
                # regardless, add the correct letter to the ans string
                ans += braille_alpha[substr]

    else:
        # otherwise, input is in eng, must convert to braille

        # loop through each character, convert that into braille code
        for i in range (len(input)):
            if input[i].isupper():
                # if the input is an uppercase letter, add the uppercase braille sqn, then the lowercase letter
                ans += ".....O" 
                ans += list(braille_alpha.keys())[list(braille_alpha.values()).index(input[i].lower())]

            elif input[i].isnumeric():
                # only if this is the first number, add the "number follows" braille code
                if num_flag == -1:
                    ans += ".O.OOO"
                    num_flag = 1 

                # adds the number from the dict of braille to numbers 0-9
                ans += list(braille_num_special.keys())[list(braille_num_special.values()).index(input[i])]
            else:

                # sets the num flag to -1, indicating sequence of numbers has stopped
                if input[i] == " ":
                    num_flag = -1

                ans += list(braille_alpha.keys())[list(braille_alpha.values()).index(input[i])]
            
    return ans


if __name__ == "__main__":
    
    # take all inputs after the python translator.py execution command
    input_args = sys.argv[1:]
    
    # join the arguments into a single string
    input_string = ' '.join(input_args)

    # output the decoded text
    print(parse_input(input_string))