
def Main():
    trans = {}
    brailToString = {}
    alphabet = ["a","b","c","d", "e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    alphabetToString = {"a": "1", "b": "2", "c": "3", "d": "4", "e": "5", "f": "6", "g": "7", "h": "8", "i": "9", "j": "0"}

    trans[" "] = "......"
    trans["a"] = "O....."
    trans["b"] = "O.O..."
    trans["c"] = "OO...."
    trans["d"] = "OO.O.."
    trans["e"] = "O..O.."
    trans["f"] = "OOO..."
    trans["g"] = "OOOO.."
    trans["h"] = "O.OO.."
    trans["i"] = ".OO..."
    trans["j"] = ".OOO.."

    brailToString["O....."] = "a"
    brailToString["O.O..."] = "b"
    brailToString["OO...."] = "c"
    brailToString["OO.O.."] = "d"
    brailToString["O..O.."] = "e"
    brailToString["OOO..."] = "f"
    brailToString["OOOO.."] = "g"
    brailToString["O.OO.."] = "h"
    brailToString[".OO..."] = "i"
    brailToString[".OOO.."] = "j"
    brailToString["......"] = " "

    wOffest = 0

    for i in range(10):
        
        trans[alphabet[i+10]] = trans[alphabet[i]][0:4] + "O" + trans[alphabet[i]][5]
        trans[str((i + 1) % 10)] = trans[alphabet[i]]

        brailToString[trans[alphabet[i]][0:4] + "O" + trans[alphabet[i]][5]] = alphabet[i + 10]
        if (i < 5):
            
            
            if alphabet[i+20] == "w":
                wOffest = 1
                trans["w"] = ".OOO.O"
                brailToString[".OOO.O"] = "w"
            trans[alphabet[i+wOffest+20]] = trans[alphabet[i]][0:4] + "OO"
            brailToString[trans[alphabet[i]][0:4] + "OO"] = alphabet[i+wOffest+20]

    inp = input()
    soln = ""


    def stringToBrailleTranslation(inp):
        soln = ""
        number = False
        for i in range(len(inp)):
            currentIndex = inp[i]        
            if (currentIndex.isupper()):
                soln+= ".....O"
                soln += trans[currentIndex.lower()].upper()
                
            else:                
                if (currentIndex.isdigit() and number == False):
                    soln += ".O.OOO"
                    number = True
                if (currentIndex == " "):
                    number = False
                soln += trans[currentIndex]
        return soln

    def brailleToStringTranslation(inp):
        soln = ""
        nextCap = False
        decimal = False
        number = False
        for i in range(0, len(inp), 6):
            currentIndex = inp[i:i+6]            
            if (currentIndex == ".....O"):
                nextCap = True
                
                continue
            if (currentIndex == ".O...O"):
                decimal = True
                continue
            if (currentIndex == ".O.OOO"):
                number = True
                
                continue

            if (nextCap):
                soln += brailToString[currentIndex].upper()
                
            elif (decimal) :
                soln += "." + brailToString[currentIndex]  
            elif (currentIndex == "......"):
                
                number = False
                soln+= " "
            elif (number):
                soln += alphabetToString[brailToString[currentIndex]]
                
            else:
                soln += brailToString[currentIndex]
            
            nextCap = False
            decimal = False

        return soln

    if (len(inp) == 0):
        print("")
    else:
        if ("." in inp):
            soln = brailleToStringTranslation(inp)
        else:
            soln = stringToBrailleTranslation(inp)


    print(soln)

if __name__ == "__main__":
    Main()