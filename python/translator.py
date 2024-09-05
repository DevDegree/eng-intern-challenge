
import sys

def main():
    dictionary = {
        "O....." : "a",
        "O.O..." : "b",
        "OO...." : "c",
        "OO.O.." : "d",
        "O..O.." : "e",
        "OOO..." : "f",
        "OOOO.." : "g",
        "O.OO.." : "h",
        ".OO..." : "i",
        ".OOO.." : "j",
        "O...O." : "k",
        "O.O.O." : "l",
        "OO..O." : "m",
        "OO.OO." : "n",
        "O..OO." : "o",
        "OOO.O." : "p",
        "OOOOO." : "q",
        "O.OOO." : "r",
        ".OO.O." : "s",
        ".OOOO." : "t",
        "O...OO" : "u",
        "O.O.OO" : "v",
        ".OOO.O" : "w",
        "OO..OO" : "x",
        "OO.OOO" : "y",
        "O..OOO" : "z",
        "......" : " "
    }
        # ".O...O" : ".",
        # "..OO.O" : ".",
        # "..O..." : ",",
        # "..O.OO" : "?",
        # "..OOO." : "!",
        # "..OO.." : ":",
        # "..O.O." : ";",
        # "....OO" : "-",
        # ".O..O." : "/",
        # ".OO..O" : "<",
        #"O..OO." : ">",
        # "O.O..O" : "(",
        # ".O.OO." : ")",
    
    # make the dictionary bidirectional
    temp = {v: k for k, v in dictionary.items()}
    dictionary.update(temp)

    # check for capital
    # set to true when "capital follows" is seen - capitalize following character
    capitalFollows = False

    numberFollows = False

    # get text
    arg = ' '.join(sys.argv[1:])

    # check if it is braille (divisible by 6 and only contains O and .)
    if(len(arg)%6 == 0 and all(char in {'O', '.'} for char in arg)):
        output = ""
        for i in range(0, len(arg), 6):
            braille = arg[i:i+6]
            if braille == ".....O":
                capitalFollows = True
                continue
            
            if braille == ".O.OOO":
                numberFollows = True
                continue

            text = dictionary[braille]
            if text == " ":
                numberFollows = False

            if numberFollows:
                # convert to number
                if 'a' <= text <= 'j':  # Ensure it's a valid character to convert
                    number = ord(text) - ord('a') + 1
                    number = number % 10  # 'j' should convert to 0
                    text = str(number)
                
            elif capitalFollows:
                # capitalize
                text = text.capitalize()
                capitalFollows = False
            
            output += text

        print(output)

    else:
        # else it's English Text
        isNumber = False
        braille = ""
        for c in arg:
            if c.isupper():
                braille += ".....O"
                c = c.lower()

            if c.isdigit() and isNumber is False:
                braille += ".O.OOO"
                isNumber = True
            
            if c == " ":
                isNumber = False

            if isNumber and c.isnumeric():
                if(c == '0'):
                    c = 'j'
                else:
                    c = chr(ord('a') + (ord(c) - ord('0')) - 1)
             
            # print("char: " + c + " braille: " + dictionary[c])
            braille += dictionary[c]
        
        print(braille)

    



if __name__ == "__main__":
    main()