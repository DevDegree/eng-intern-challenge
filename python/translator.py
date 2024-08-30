import sys

# Tests cases are incorrect, so I have left my code as original.

# Dictionary of alphabet
alpha_sym = {
"O....." : "a", "O.O..." : "b", "OO...." : "c",
"OO.O.." : "d", "O..O.." : "e", "OOO..." : "f",
"OOOO.." : "g", "O.OO.." : "h", ".OO..." : "i",
".OOO.." : "j", "O...O." : "k", "O.O.O." : "l",
"OO..O." : "m", "OO.OO." : "n", "O..OO." : "o",
"OOO.O." : "p", "OOOOO." : "q", "O.OOO." : "r",
".OO.O." : "s", ".OOOO." : "t", "O...OO" : "u",
"O.O.OO" : "v", ".OOO.O" : "w", "OO..OO" : "x",
"OO.OOO" : "y", "O..OOO" : "z", "..OO.O" : ".",
"..O..." : ",", "..O.OO" : "?", "..OOO." : "!",
"..OO.." : ":", "..O.O." : ";", "....OO" : "-",
".O..O." : "/", ".OO..O" : ">", "O.O..O" : "(",
".O.OO." : ")", "......" : " "
}

# Dictionary of alphabet
numbers = {
"O....." : "1", "O.O..." : "2", "OO...." : "3",
"OO.O.." : "4", "O..O.." : "5", "OOO..." : "6",
"OOOO.." : "7", "O.OO.." : "8", ".OO..." : "9",
".OOO.." : "0"
}


def translate(sentence):
        """
        Translation function that takes a (string) value and translates from Braille to English or English to Braille
        """
        finalString  = ""
        word = ""
        capitalize = 0 # Takes into account whether it is capitalzed or not
        number = 0 # Takes into account whether followed by number or not
        
        # Braille to English
        if sentence[0:6] in numbers or sentence[0:6]in alpha_sym or  sentence[0:6]  == ".....O" or sentence[0:6] == ".O.OOO" or sentence[0:6] == "......":
            for i in range(len(sentence)):
                word += sentence[i]
                if (i+1)%6==0:
                        if word == ".....O":
                            capitalize = 1
                        if word == ".O.OOO":
                            number = 1
                        if word == "......":
                            number = 0
                        if word in alpha_sym:
                            if number == 1:
                                finalString += numbers.get(word)
                                word = ""
                                continue
                            if capitalize == 1:
                                finalString += alpha_sym.get(word).upper()
                                capitalize -=1
                            else:
                                finalString += alpha_sym.get(word)
                        word = ""
        else: 
        # English to Braille
            for i in sentence:
                if i.isupper():
                    finalString += ".....O"
                if i.isnumeric():
                    if number == 1:
                       finalString = finalString
                    else:
                        finalString += ".O.OOO"
                    number = 1
                
                if i.isnumeric():
                    key = next(iter(key for key, val in numbers.items() if val == i.lower()), None)
                    finalString += str(key)
                else:
                    key = next(iter(key for key, val in alpha_sym.items() if val == i.lower()), None)
                    finalString += str(key)
                    if key == "......":
                       number = 0

        print(finalString)

if __name__ == '__main__':
    translate(str(' '.join(sys.argv[1:])))
