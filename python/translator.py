import sys

braille_dict_letter = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f", "OOOO..": "g", "O.OO..": "h",
    ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p",
    "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
    "OO.OOO": "y", "O..OOO": "z", "......": " "
}

braille_dict_num = {
    "O....." : "1",  "O.O..." : "2",  "OO...." : "3", "OO.O.." : "4",
    "O..O.." : "5", "OOO..." : "6", "OOOO.." : "7",  "O.OO.." : "8",
    ".OO..." : "9", ".OOO.." : "0",
}

def get_key(dict, value):
    for k, v in dict.items():
        if value == v:
            return k

def braille_to_english(input):
    output = ""

    #break string every 6 character 
    list_char = []
    for i in range(0, len(input), 6):
        list_char.append(input[i:i+6])


    #change every character to its english equivalent
    i = 0
    letters = 1
    while i < len(list_char):
        #capital follows
        if list_char[i] == ".....O" and letters == 1:
            output += braille_dict_letter[list_char[i+1]].upper()
            i += 2
        
        #number follows turn on and offf
        elif list_char[i] == ".O.OOO":
            letters = 0
            i += 1
        elif list_char[i] == "......" and letters == 0:
            output += " "
            letters = 1
            i += 1

        #all other cases
        elif letters == 0:
            output += braille_dict_num[list_char[i]]
            i += 1
        else:
            output += braille_dict_letter[list_char[i]]
            i += 1
    
    return output

def english_to_braille(input):
    output = ""

    i = 0
    letters = 1
    while i < len(input):
        #adding a capital follows
        if input[i].isupper() == True:
            output += ".....O"
            output += get_key(braille_dict_letter, input[i].lower())
            i += 1
        
        #adding a number follows only when the first number in a series comes
        elif input[i] in braille_dict_num.values() and letters == 1:
            output += ".O.OOO"
            letters = 0
            output += get_key(braille_dict_num, input[i])
            i += 1 

        # space ends series of numbers
        elif input[i] == " " and letters == 0:
            letters = 1
            output += "......"
            i += 1

        #number but not first one
        elif input[i] in braille_dict_num.values() and letters == 0:   
            output += get_key(braille_dict_num, input[i]) 
            i += 1 

        #all other cases
        else:
            output += get_key(braille_dict_letter, input[i])
            i += 1
        
    return output

def main():
    #keep input spaces
    input = ""
    for i in range(1,len(sys.argv)):
        input += sys.argv[i]
        if len(sys.argv) != 1 and i != len(sys.argv) - 1:
            input += " "
    
    #determine whether english or braille
    count = 0
    for i in input:
        if i == 'O' or i == '.':
            count += 1

    if count == len(input):
       print(braille_to_english(input))
    else:
        print(english_to_braille(input))

if __name__ == "__main__":
    main()
