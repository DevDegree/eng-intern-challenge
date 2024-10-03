import sys

# user input
inpStr = sys.argv[1:]
inpStr = " ".join(inpStr)

# output string
output = ""

# letters
convert = {
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
    "p":"OOO.O.",
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

# numbers
nums = {
    "0":".OOO..",
    "1":"O.....",
    "2":"O.O...",
    "3":"OO....",
    "4":"OO.O..",
    "5":"O..O..",
    "6":"OOO...",
    "7":"OOOO..",
    "8":"O.OO..",
    "9":".OO...",
}

# special cases
actions = {
    "space":"......",
    "cap":".....O",
    "num":".O.OOO",
}

# function to get key from value
def brailleToChar(string, num):
    # if not number
    if num == 0:
        retVal = [letter for letter, braille in convert.items() if braille == string]
    # if number
    else:
        retVal = [letter for letter, braille in nums.items() if braille == string]
    return retVal[0]

# if input is braille
if set(inpStr) == {"O", "."}:
    i = 0
    while i < len(inpStr):
        # read 6 chars at a time
        string = inpStr[i:i+6]
        # if letter is capitalized, read letter and add to output
        if string == actions["cap"]:
            i += 6
            string = inpStr[i:i+6]
            output += brailleToChar(string, 0).capitalize()
        # if space, add space to output string
        elif string == actions["space"]:
            output += " "
        # if number, read next set of values and add to output until end of input or next space
        elif string == actions["num"]:
            while string != actions["space"] and i < len(inpStr) - 6:
                i += 6
                string = inpStr[i:i+6]
                output += brailleToChar(string, 1)
        # lowercase letters
        else:
            output += brailleToChar(string, 0)
        i += 6

# input is english
else:
    i = 0
    while i < len(inpStr):
        # if space, insert into output
        if inpStr[i] == " ":
            output += actions["space"]
        # if number, add number identifier and keep going until space/end of string
        elif inpStr[i] in nums.keys():
            output += actions["num"]
            while i < len(inpStr) and inpStr[i] != " ":
                output += nums[inpStr[i]]
                i += 1
            i -= 1
        # if lowercase letter
        elif inpStr[i] in convert.keys():
            output += convert[inpStr[i]]
        # uppercase letter
        else:
            output += actions["cap"]
            output += convert[inpStr[i].lower()]
        i += 1

print(output)
