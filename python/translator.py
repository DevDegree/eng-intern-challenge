import sys
from textwrap import wrap

def isbraille(str):
    input = set(str)
    brailechars = set("O.")
    if input.issubset(brailechars):
        return True
    else:
        return False

def dotranslate(str):
    output = ""
    capital = False
    number = False
    if isbraille(str):
        sttarr = wrap(str, 6)
        for x in sttarr:
            try:
                if x == "......" and number == True:
                    number = False
                if x == ".....O":
                    capital = True
                elif x == ".O.OOO":
                    number = True
                else:
                    if capital:
                        charindex = brailechars.index(x)
                        output += caps[charindex]
                        capital = False
                    elif number:
                        charindex = brailenumbers.index(x)
                        output += numbers[charindex]
                    else:
                        charindex = brailechars.index(x)
                        output += englishchars[charindex]
                        
            except Exception as e:
                return e
        return output
    else:
        sttarr = list(str)
        isnumber = False
        for x in sttarr:
            try:
                charindex = 0
                if x in caps:
                    output += ".....O"
                    charindex = caps.index(x)
                    output += brailechars[charindex]
                elif x in numbers and isnumber == False:
                    output += ".O.OOO"
                    charindex = numbers.index(x)
                    output += brailenumbers[charindex]
                    isnumber = True
                elif x in numbers and isnumber == True:
                    charindex = numbers.index(x)
                    output += brailenumbers[charindex]
                else:
                    charindex = englishchars.index(x)
                    output += brailechars[charindex]
                if x == " ":
                    isnumber = False
            except Exception as e:
                return e
        return output

englishchars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r","s","t","u", "v","w","x","y","z"," ",".",",","?","!",":",";","-","/","<",">","(",")"]

brailechars = ["O.....", "O.O...","OO....","OO.O..","O..O..","OOO...","OOOO..","O.OO..",".OO...",".OOO..","O...O.", "O.O.O.","OO..O.","OO.OO.","O..OO.","OOO.O.","OOOOO.","O.OOO.",".OO.O.",".OOOO.","O...OO","O.O.OO",".OOO.O","OO..OO","OO.OOO","O..OOO","......","..OO.O","..O...","..O.OO","..OOO.","..OO..","..O.O.","....OO",".O..O.",".OO..O","O..OO.","O.O..O",".O.OO."]

numbers = ["1","2","3","4","5","6","7","8","9","0"]
brailenumbers = ["O.....", "O.O...","OO....","OO.O..","O..O..","OOO...","OOOO..","O.OO..",".OO...",".OOO.."]

caps = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

strtotranslate = ""
xnum = 0
for x in sys.argv:
    if xnum == 1:
        strtotranslate += x
    elif xnum > 1:
        strtotranslate += " " + x
    xnum += 1

print(dotranslate(strtotranslate))
