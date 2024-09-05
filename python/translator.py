import sys

def translate(text: str) -> str:
    # English to Braille mapping hash map (constant space)
    englishToBraille = {"a": "O.....", "b": "O.O...", "c": "OO....", 
                        "d": "OO.O..", "e": "O..O..", "f": "OOO...",
                        "g": "OOOO..", "h": "O.OO..", "i": ".OO...",
                        "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
                        "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
                        "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.",
                        "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO",
                        "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
                        "y": "OO.OOO", "z": "O..OOO",
                        
                        "NUMBER": ".O.OOO", "CAPITAL": ".....O",
                        "DECIMAL": ".O...O",
                        ".": "..OO.O", ",": "..O...", "?": "..O.OO",
                        "!": "..OOO.", ":": "..OO..", ";": "..O.O.",
                        "-":"....OO", "/": ".O..O.", "<": ".OO..O",
                        ">": "O..OO.", "(": "O.O..O", ")": ".O.OO.",
                        " ": "......"}
    
    # constructing the number to Braille mapping using the first dictionary (constant space)
    numberToBraille = {}
    for i in range(1, 11):
        if i == 10:
            numberToBraille["0"] = englishToBraille[chr(ord("a") + (i-1))]
        else:
            numberToBraille[str(i)] = englishToBraille[chr(ord("a") + (i-1))]
    
    # storing the Braille to English mapping (constant space)
    brailleToEnglish = {"O.....": "a", "O.O...": "b", "OO....": "c",
                        "OO.O..": "d", "O..O..": "e", "OOO...": "f",
                        "OOOO..": "g", "O.OO..": "h", ".OO...": "i",
                        ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
                        "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
                        "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r",
                        ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u",
                        "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
                        "OO.OOO": "y", "O..OOO": "z",
                        ".O.OOO": "NUMBER", ".....O": "CAPITAL",
                        ".O...O": "DECIMAL",
                        "..OO.O": ".", "..O...": ",", "..O.OO": "?",
                        "..OOO.": "!", "..OO..": ":", "..O.O.": ";",
                        "....OO": "-", ".O..O.": "/", ".OO..O": "<",
                        "O.O..O": "(", ".O.OO.": ")",
                        "......": " "}
    
    # constructign the Braille to number mapping (constant space)
    brailleToNumber = {}
    i = 1
    for key in brailleToEnglish:
        if i == 10:
            brailleToNumber[key] = "0"
            break
        brailleToNumber[key] = str(i)
        i += 1
    
    # checking if the given input is English or Braille                
    isBraille = False
    if len(text) >= 6:
        for ch in text:
            if ch == "." or ch == "O":
                isBraille = True
            else:
                isBraille = False
                break
    res = ""
    # handling English text
    if not isBraille:
        isCapital = False # capital flag
        isNumber = True # number flag
        isDecimal = True #decimal flag

        for ch in text:
            if ch.isupper(): #checking for upper case
                isCapital = True
                
            elif ch == "." and isDecimal: #checking for decimal points and handling them
                res += englishToBraille["DECIMAL"] 
                res += englishToBraille[ch]
                isDecimal = False
                continue
            elif ch == " ":
                res += englishToBraille[ch]
                isNumber = True # assigning the number flag to be True right after a space
                continue
            # handling a digit in the string
            if ch in numberToBraille:
                if isNumber:
                    res += englishToBraille["NUMBER"]
                    isNumber = False
                braille = numberToBraille[ch]
                res += braille
            # handling an alphabet in the string
            else:
                if isCapital:
                    res += englishToBraille["CAPITAL"]
                    isCapital = False
                
                braille = englishToBraille[ch.lower()]
                res += braille

    # handling Braille text
    else:
        isCapital = False
        isNumber = False
        isDecimal = False
        # going through the Braille string 6 characters at a time
        for i in range(0, len(text), 6):
            s = text[i: i+6]
            if s == ".....O":
                isCapital = True #handling "capital follows"
                continue
            elif s == ".O.OOO":
                isNumber = True # handling "number follows"
                continue
            elif s == ".O...O":
                isDecimal = True
                continue
            elif s == "......":
                res += " "
                isNumber = False # handling space
                continue
            
            if isNumber: # handling digits in Braille translation
                if isDecimal: # handling decimal points for digits
                    res += "."
                    isDecimal = False
                    continue
                number = brailleToNumber[s]
                res += number

            # handling alphabets in Braille translation
            else:
                english = brailleToEnglish[s]
                if isCapital: # handling capital letters
                    res += english.upper()
                    isCapital = False
                else:
                    res += english

    return res

def main():
    input_text = input_text = " ".join(sys.argv[1:]) # handling multple command line arguments based on the expected output.
    result = translate(input_text)
    print(result)
if __name__ == "__main__":
    main()


                    



