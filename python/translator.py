def translator(input_text):
    alpha_translator ={
        "a": "O.....",
        "b": "O.O...",
        "c": "OO....",
        "d": "OO.O..",
        "e": "O..O..",
        "f": "OOO...",
        "g": "OOOO..",
        "h": "O.OO..",
        "i": ".OO...",
        "j": ".OOO...",
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
    }
    capital_follow = ".....O"
    decimal_follow = ".O...O"
    number_follow = ".O.OOO"
    space = "......"
    numeric_translator ={
        ".OOO..": 0,
        "O.....": 1,
        "O.O...": 2,
        "OO....": 3,
        "OO.O..": 4,
        "O..O..": 5,
        "OOO...": 6,
        "OOOO..": 7,
        "O.OO..": 8,
        ".OO...": 9,
    }
    