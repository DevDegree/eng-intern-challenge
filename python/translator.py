combo = [
    (".....0", "CAPITAL"),
    (".0.000", "NUMBER"),
    ("......", " "),
    ("0.....", "a", "A", "1"), 
    ("0.0...", "b", "B", "2"),
    ("00....", "c", "C", "3"),
    ("00.0..", "d", "D", "4"),
    ("0..0..", "e", "E", "5"), 
    ("000...", "f", "F", "6"),
    ("0000..", "g", "G", "7"),
    ("0.00..", "h", "H", "8"),
    (".00...", "i", "I", "9"),
    (".000..", "j", "J", "0"),
    ("0...0.", "k", "K"),
    ("0.0.0.", "l", "L"),
    ("00..0.", "m", "M"),
    ("00.00.", "n", "N"),
    ("0..00.", "o", "O"),
    ("000.0.", "p", "P"),
    ("00000.", "q", "Q"),
    ("0.000.", "r", "R"),
    (".00.0.", "s", "S"),
    (".0000.", "t", "T"),
    ("0...00", "u", "U"),
    ("0.0.00", "v", "V"),
    (".000.0", "w", "W"),
    ("00..00", "x", "X"),
    ("00.000", "y", "Y"),
    ("0..000", "z", "Z"),
]

def braille_to_english(inpt):

    output = ""

    #inpt is in braille, convert to english
    sets = len(inpt)/6 #sets of 6 dots in input
    i = 0 #set counter

    capital = False
    number = False

    while i < sets:
        dot = i*6
        temp = inpt[dot:dot+6]

        find = 0 #finder
        while find < 29:
            if combo[find][0] == temp:
                break
            find += 1
        
        #at this point, find is the index of the braille set in combo list
        if combo[find][1] == "CAPITAL":
            capital = True
        elif combo[find][1] == "NUMBER":
            number = True
        elif capital == True:
            output = output + combo[find][2]
            capital = False
        elif number == True:
            output = output + combo[find][3]
        else:
            output = output + combo[find][1]

        i += 1

    print(output)


def english_to_braille(inpt):
    #inpt is in english, convert to braille

    output = ""

    number = False
    
    i = 0 #parse input string
    while i < len(inpt):

        if inpt[i] == " ":
            number = False

        found = False

        if found == False and number == False :

            #first check lowercase letters
            j = 2 #entries in combo searched
            while j < 29:
                if combo[j][1] == inpt[i]: #found letter (lowercase)
                    output = output + combo[j][0] #appended braille
                    found = True
                    break
                j += 1

        if found == False and number == False:

            #now check uppercase letters
            j = 3
            while j < 29:
                if combo[j][2] == inpt[i]: #found letter (uppercase)
                    output = output + combo[0][0] + combo[j][0]
                    found = True
                    break
                j += 1

        if found == False:

            #finally check numbers
            j = 3
            while j < 13:
                if combo[j][3] == inpt[i]: #found number
                    if number == True:
                        output = output + combo[j][0]
                    else:
                        output = output + combo[1][0] + combo[j][0]
                        number = True
                    found = True
                    break
                j += 1

        i += 1

    print(output)

def main():
    inpt = input()
    braille = False
    max = 0
    
    if len(inpt) < 6:
        max = len(inpt)
    else:
        max = 6
    
    i = 0 #character counter
    while i < max:
        if inpt[i] == ".":
            braille = True
            break
        i += 1

    if braille == True:
        braille_to_english(inpt)
    else:
        english_to_braille(inpt)

if __name__ == "__main__":
    main()