import sys

engToBr = {"a": "O.....",
         "b": "O.O...",
         "c": "OO....",
         "d": "OO.O..",
         "e": "O..O..",
         "f": "OOO...",
         "g": "OOOO..",
         "h": "O.OO..",
         "i": ".OO...",
         "j": ".OOO..",
         "k": "O...O.",
           "l": "O.O.O.",
           "m": "OO..O.",
           "n": "OO.OO.",
           "o": "O..OO.",
           "p": "OOO.O.",
           "q": "O0000.",
           "r": "O.OOO.",
           "s": ".OO.O.",
           "t": ".OOOO.",
           "u": "O...OO",
           "v": "O.O.OO",
           "w": ".OOO.O",
           "x": "OO..OO",
           "y": "OO.0OO",
           "z": "O..OOO",
           ".": "..OO.O",
           ",": "..O...",
           "?": "..O.OO",
           "!": "..OOO.",
           ":": "..OO..",
           ";": "..O.O.",
           "-": "....OO",
           "/": ".O..O.",
           "<": ".OO..O",
           ">": "O..OO.",
           "(": "O.O..O",
           ")": ".O.OO.",
           " ": "......"
           }
engToBrDigits= {"1": "O.....",
           "2": "O.O...",
           "3": "OO....",
           "4": "OO.O..",
           "5": "O..O..",
           "6": "OOO...",
           "7": "OOOO..",
           "8": "O.OO..",
           "9": ".OO...",
           "0": ".OOO.."}
brToEng = {"O.....":"a",
         "O.O...":"b",
         "OO....":"c",
        "OO.O..":"d",
        "O..O..": "e",
         "OOO...":"f",
          "OOOO..":"g",
         "O.OO..":"h",
         ".OO...":"i",
         ".OOO..":"j",
         "O...O.":"k",
           "O.O.O.":"l",
           "OO..O.":"m",
           "OO.OO.":"n",
           "O..OO.":"o",
           "OOO.O.":"p",
           "O0000.":"q",
           "O.OOO.":"r",
           ".OO.O.":"s",
           ".OOOO.":"t",
           "O...OO":"u",
           "O.O.OO":"v",
           ".OOO.O":"w",
           "OO..OO":"x",
            "OO.OOO":"y",
           "O..OOO":"z",
           "..OO.O":".",
           "..O...": ",",
           "..O.OO":"?",
           "..OOO.":"!",
            "..OO..":":",
            "..O.O.":";",
           "....OO":"-",
           ".O..O.":"/",
           ".OO..O":"<" ,
            "O.O..O":"(",
           ".O.OO.":")",
            "......":" "
           }

brToEngDigits ={"O.....":"1",
           "O.O...":"2",
           "OO....":"3",
           "OO.O..":"4",
           "O..O..":"5",
           "OOO...":"6",
            "OOOO..":"7",
           "O.OO..":"8",
           ".OO...":"9",
           ".OOO..":"0"}


def englishtoBraille(english):
    argument = " ".join(english)
    toBraille = ""
    i = 0
    while (i < len(argument)):
        if (argument[i].isdigit()):
            trackdigit = True
            toBraille += ".O.OOO"
            while (trackdigit):
                toBraille += engToBrDigits[argument[i]]
                if (i + 1 >= len(argument)):
                    trackdigit = False
                else:
                    if (argument[i + 1].isdigit()):
                        i += 1
                    else:
                        trackdigit = False

        elif (argument[i].isupper()):
            toBraille += ".....O" + engToBr[argument[i].lower()]
        else:
            toBraille += engToBr[argument[i]]

        i += 1
    print(toBraille)


def brailletoEnglish(braille):
    argument = "......".join(braille)   #in between items puts space in braille
    toEnglish = ""
    i=0
    while(i<len(argument)):
        if(argument[i:i+6]==".O.OOO"):  # checks if num
            while(argument[i+6:i+12] in brToEngDigits):
                toEnglish+=brToEngDigits[argument[i+6:i+12]]
                i+=6
            i+=6
        elif(argument[i:i+6]==".....O"):
            toEnglish = toEnglish + brToEng[argument[i+6:i+12]].upper()
            i+=12
        else:
            toEnglish+=brToEng[argument[i:i+6]]
            i+=6
    print(toEnglish)


def main(): #main


    if(len(sys.argv)<2):
        print("")
    else:
        argument = sys.argv[1:]
        braille = True
        curr = sys.argv[1]
        if(len(curr)%6!=0):
           braille=False
        else:
           if(curr[0] == "O"):
                  if(curr[1]!= "." or curr[1]!= "0"):
                         braille = False
        if(braille):
               brailletoEnglish(argument)
        else:
               englishtoBraille(argument)
main()

