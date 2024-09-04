userInput = input()

symbolHash = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..",
    "e": "O..O..", "f": "OOO...", "g": "OOOO..", "h": "O.OO..",
    "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.",
    "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO", " ": "......"
},

def checkEnglish(input):
    english = False
    if (
        len(set(input)) > 2 
        or len(input) < 6
        or ("O" not in input and "." not in input)
        ):
        english = True
    
    return english

def checkCapitalNxt():
    pass

def checkNumNxt():
    pass


print(str(checkEnglish(userInput)))