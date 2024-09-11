import sys

toBraille = {
    "a":"O.....",
    "b":"O.O...",
    "c":"OO....",
    "d":"OO.O..",
    "e":"O..O..",
    "f":"OOO...",
    "g":"OOOO..",
    "h":"O.OO..",
    "i":".OO...",
    "j":".OOO..",
    "k":"O...O.",
    "l":"O.O.O.",
    "m":"OO..O.",
    "n":"OO.OO.",
    "o":"O..OO.",
    "p":"OO).O.",
    "q":"OOOOO.",
    "r":"O.OOO.",
    "s":".OO.O.",
    "t":".OOOO.",
    "u":"O...OO",
    "v":"O.O.OO",
    "w":".OOO.O",
    "x":"OO..OO",
    "y":"OO.OOO",
    "z":"O..OOO",
}
toEnglish = {
    "O.....":"a",
    "O.O...":"b",
    "OO....":"c",
    "OO.O..":"d",
    "O..O..":"e",
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
    "OO).O.":"p",
    "OOOOO.":"q",
    "O.OOO.":"r",
    ".OO.O.":"s",
    ".OOOO.":"t",
    "O...OO":"u",
    "O.O.OO":"v",
    ".OOO.O":"w",
    "OO..OO":"x",
    "OO.OOO":"y",
    "O..OOO":"z",
    "......":" "
}
toBrailleNums = {
    "1":"O.....",
    "2":"O.O...",
    "3":"OO....",
    "4":"OO.O..",
    "5":"O..O..",
    "6":"OOO...",
    "7":"OOOO..",
    "8":"O.OO..",
    "9":".OO...",
    "0":".OOO.."
}
toEnglishNums = {
    "O.....":"1",
    "O.O...":"2",
    "OO....":"3",
    "OO.O..":"4",
    "O..O..":"5",
    "OOO...":"6",
    "OOOO..":"7",
    "O.OO..":"8",
    ".OO...":"9",
    ".OOO..":"0"
}

userInput = sys.argv[1:]

translatedOutput=""
useNums = False
capitalize = False

if not userInput:
    print("Please provide an input")
else:
    #userInput is english
    if "." not in userInput[0]:
        for i, word in enumerate(userInput):
            for letter in word:
                if letter.isupper():
                    translatedOutput += ".....O"
                elif letter.isdigit() and not useNums:
                    useNums = True
                    translatedOutput += ".O.OOO"

                if letter.isalpha():
                    translatedOutput += toBraille[letter.lower()]
                else:
                   translatedOutput += toBrailleNums[letter] 
            if i < len(userInput) - 1:
                translatedOutput += "......"
                useNums = False
    else: 
        for i in range(0,len(userInput[0]), 6):
            character = userInput[0][i:i+6]
            if character == ".O.OOO":
                useNums = True
                continue
            elif character == ".....O":
                capitalize = True
                continue
            if useNums and character != "......":
                translatedOutput += toEnglishNums[character]
            else:
                useNums = False
                if capitalize:
                    capitalize = False
                    translatedOutput += toEnglish[character].capitalize()
                else:
                    translatedOutput += toEnglish[character]


print(translatedOutput)


# .O.OOOOO.O..O.O...
# .O.OOOOO.O..O.O...
