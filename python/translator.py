import sys

def isBraille(line):
    print(line)
    for n in range(len(line)):
        if line[n] != "O" and line[n] != ".":
            return False
    return True


translation = {"CAPITAL": ".....O",
               "DECIMAL": ".O...O",
               "SPACE": "......",
               "NUMBERS": ".0.000",
               "a": "0.....",
               "b": "00....",
               "c": "00....",
               "d": "00.0..",
               "e": "0..0..",
               "f": "000...",
               "g": "0000..",
               "h": "0.00..",
               "i": ".00...",
               "j": ".000..",
               "k": "0...0.",
               "l": "0...0.",
               "m": "00..0.",
               "n": "00.00.",
               "o": "0..00.",
               "p": "000.0.",
               "q": "00000.",
               "r": "0.000.",
               "s": ".00.0.",
               "t": ".0000.",
               "u": "0...00",
               "v": "0.0.00",
               "w": ".000.0",
               "x": "00..00",
               "y": "00.000",
               "z": "0..000",

}

translationNumbers = {"1": "0.....",
                      "2": "00....",
                      "3": "00....",
                      "4": "00.0..",
                      "5": "0..0..",
                      "6": "000...",
                      "7": "0000..",
                      "8": "0.00..",
                      "9": ".00...",
                      "0": ".000..",}

# braile is in segments of 6, so any braille code would be in segments of 6
# unsure if the sys.argv = 2 is just bc of how im testing my logic here

if (len(sys.argv[1]) % 6) == 0 and isBraille(sys.argv[1]):
    ans = ""
    braille = list(translation.values())
    alphanum = list(translation.keys())
    numbers = list(translationNumbers.values())
    caps = False
    nums = False
    # take segments 6 at a time
    while len(sys.argv) != 0:
        char = sys.argv[1][:6]
        print(char)
        if braille.index(char) == 2: # index of space key
            nums = False
        elif braille.index(char) == 0:
            caps = True
             # do caps lock here
            ans += alphanum[braille.index(char)].upper()
            continue
        elif braille.index(char) == 3:
            nums = True

        if nums:
            # search in nums list
            ans += nums[braille.index(char)-4]

        ans += alphanum[braille.index(char)]
        sys.argv = sys.argv[6:]

    print(ans)
    # print(".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO")