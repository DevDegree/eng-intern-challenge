
'''
In this coding challenge you will create a terminal / command-line application that can translate Braille to English and vice versa.

The string to translate will be passed into your application as an argument at runtime. Your application must be smart enough to determine if the string given to it is either Braille or English and automatically convert it to the appropriate opposite.

For the purposes of this challenge Braille must be displayed as O and . where O represents a raised dot. You must include the entire English alphabet, the ability to capitalize letters, add spaces, and the numbers 0 through 9 as well.

After conversion, output the translated string--and nothing else--to the terminal.
'''
import sys

alphabets = {
    "a": "O.....",
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
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO"
}
numbers = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO.."
}

follows = {
    "capi": ".....O",
    "deci": ".O...O",
    "numb": ".O.OOO",
    " ": "......"
}


def bra_to_eng(message):
    braille = []
    strr = ""
    for i in range(len(message)):
        strr += message[i]
        if (i + 1) % 6 == 0:
            braille.append(strr)
            strr = ""
    
    capital = False
    number = False
    english = []

    for char in braille:
        if char == follows["capi"]:
            capital = True
        elif char == follows["numb"]:
            number = True
        elif char == follows[" "]:
            english.append(" ")
        else:
            if number:
                for key, value in numbers.items():
                    if value == char:
                        english.append(key)
                        break
                number = False
            else:
                for key, value in alphabets.items():
                    if value == char:
                        if capital:
                            english.append(key.upper())
                            capital = False
                        else:
                            english.append(key)
                        break
    return "".join(english)


def eng_to_bra(message):
    english = []
    strr = ""
    for i in range(len(message)):
        if message[i].isupper():
            if strr:
                english.append(strr)
                strr = ""
            english.append("*")  # symbol for capital letters
            english.append(message[i].lower())
        elif message[i].isnumeric():
            if strr:
                english.append(strr)
                strr = ""
            english.append("~")  # symbol for numbers
            english.append(message[i])
        elif message[i] == " ":
            if strr:
                english.append(strr)
                strr = ""
            english.append(" ")
        else:
            strr += message[i]

    if strr:
        english.append(strr)
    
    capital = False
    number = False
    braille = []

    for i in range(len(english)):
        for j in range(len(english[i])):
            if english[i][j] == "*":
                braille.append(follows["capi"])
                capital = True
            elif english[i][j] == "~":
                braille.append(follows["numb"])
                number = True
            elif english[i][j] == " ":
                braille.append(follows[" "])
            else:
                if number:
                    for key, value in numbers.items():
                        if key == english[i][j]:
                            braille.append(value)
                            break
                    number = False
                elif capital:
                    for key, value in alphabets.items():
                        if key == english[i][j].lower():
                            braille.append(value)
                            break
                    capital = False
                else:
                    for key, value in alphabets.items():
                        if key == english[i][j]:
                            braille.append(value)
                            break

    return "".join(braille)






if __name__ == "__main__":
    input = " ".join(sys.argv[1:])
    if "." in input:
        print(bra_to_eng(input))
    else:
        print(eng_to_bra(input))