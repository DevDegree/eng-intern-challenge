import sys

def isBraille(line):
    for n in range(len(line)):
        if line[n] != "0" and line[n] != ".":
            return False
    return True


translation = {"CAPITAL": ".....O",
               "DECIMAL": ".0...0",
               "SPACE": "......",
               "a": "aa"
}

translationNumbers = {}

# braile is in segments of 6, so any braille code would be in segments of 6
# unsure if the sys.argv = 2 is just bc of how im testing my logic here
if (len(sys.argv[1]) % 6) == 0 and isBraille(sys.argv[1]):


    # print(".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO")