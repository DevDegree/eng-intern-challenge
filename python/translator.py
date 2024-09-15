import sys

english_map = {
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
    "z": "O..OOO",
    "capitalfollows": ".....O",
    "decimalfollows": "..O...",
    "numberfollows": ".O.OOO",
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
braille_map = {v: k for k, v in english_map.items()}

arguments = " ".join(sys.argv[1:])
english = False

for c in arguments:
    if c != '.' and c != 'O':
        english=True
        break
    
new_string = ""
offsetNumberToLetter = ord('a') - ord('0') -1

if english:
    i = 0
    number = False
    while i < len(arguments):
        if not number and arguments[i].isnumeric():
            number = True
            new_string += english_map["numberfollows"]
            i-=1
            next
        elif not arguments[i].isnumeric():
            number = False
            if arguments[i].isupper():
                new_string += english_map["capitalfollows"]
                new_string += english_map[arguments[i].lower()]
            elif arguments[i] == "." and i+1 < len(arguments) and arguments[i+1].isnumeric():
                new_string += english_map["decimalfollows"]
            else:
                new_string += english_map[arguments[i]]
        elif number:
            new_string += english_map[chr(ord(arguments[i]) + offsetNumberToLetter + (10 if arguments[i] == '0' else 0))]
        i+=1 
else:
    splitArgs = [arguments[i:i+6] for i in range(0, len(arguments), 6)]
    i = 0
    number = False
    while i < len(splitArgs):
        if splitArgs[i] == english_map["capitalfollows"]:
            new_string += braille_map[splitArgs[i+1]].upper()
            i +=1
        elif splitArgs[i] == english_map["decimalfollows"]:
            new_string += "."
        elif splitArgs[i] == english_map["numberfollows"]:
            number = True
        elif splitArgs[i] == english_map[" "]:
            new_string += " "
            number = False
        else:
            if number:
                new_string += chr(ord(braille_map[splitArgs[i]]) - offsetNumberToLetter - (10 if braille_map[splitArgs[i]] == 'j' else 0))
            else:
                number = False
                new_string += braille_map[splitArgs[i]]
        i+=1

print(new_string)