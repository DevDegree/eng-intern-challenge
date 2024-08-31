import sys
from textwrap import wrap

def isbraille(str):
    input = set(str)
    brailechars = set("0.")
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
                if x == ".....0":
                    capital = True
                elif x == ".0.000":
                    number = True
                else:
                    if capital:
                        charindex = brailechars.index(x)
                        output += caps[charindex]
                        capital = False
                    elif number:
                        charindex = brailenumbers.index(x)
                        output += numbers[charindex]
                        number = False
                    else:
                        charindex = brailechars.index(x)
                        output += englishchars[charindex]
                        
            except:
                return 0
        return output
    else:
        sttarr = list(str)
        for x in sttarr:
            try:
                charindex = 0
                if x in caps:
                    output += ".....0"
                    charindex = caps.index(x)
                    output += brailechars[charindex]
                elif x in numbers:
                    output += ".0.000"
                    charindex = numbers.index(x)
                    output += brailenumbers[charindex]
                else:
                    charindex = englishchars.index(x)
                    output += brailechars[charindex]
            except:
                return 0
        return output

englishchars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r","s","t","u", "v","w","x","y","z"," ",".",",","?","!",":",";","-","/","<",">","(",")"]

brailechars = ["0.....", "0.0...","00....","00.0..","0..0..","000...","0000..","0.00..",".00...",".000..","0...0.", "0.0.0.","00..0.","00.00.","0..00.","000.0.","00000.","0.000.",".00.0.",".0000.","0...00","0.0.00",".000.0","00..00","00.000","0..000","......","..00.0","..0...","..0.00","..000.","..00..","..0.0.","....00",".0..0.",".00..0","0..00.","0.0..0",".0.00."]

numbers = ["1","2","3","4","5","6","7","8","9","0"]
brailenumbers = ["0.....", "0.0...","00....","00.0..","0..0..","000...","0000..","0.00..",".00...",".000.."]

caps = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

strtotranslate = sys.argv[1]

print(dotranslate(strtotranslate))
