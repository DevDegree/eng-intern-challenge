

#define dictionaries
b_t_e = { # handles braille to english letters
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
    "......": " ",
    ".O.OOO": "number",   # number indicator
    ".....O": "capital",  # capital indicator
    ".O...O": "decimal"  # decimal indicator
}

b_t_n = { # braille to #
    ".OOO..": "0",
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9"
}

b_t_p = { # braille to punc.
    "..O.OO": ".",
    "..O...": ",",
    "..OO.O": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "..O..O": "-",
    "..O.O.": "/",
    ".O..OO": "(",
    ".O.OO.": ")",
    ".OO..O": "<",
    "O..OO." : ">",
    " ": "......"
}

e_t_b = { # eng to braille
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
    "z": "O..OOO",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
    ".": "..O.OO",
    ",": "..O...",
    "?": "..OO.O",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "..O..O",
    "/": "..O.O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": ".O..OO",
    ")": ".O.OO.",
    " ": "......",
    "number": ".O.OOO",  # number indicator
    "capital": ".....O",  # capital indicator
    "decimal": ".O...O"  # decimal indicator

}

def br_to_en(inp):
    out = ""
    i = 0
    cap = False
    num = False
    decimal = False
    curr_c = ""

    curr_str = ""

    while i < len(inp):
        curr_str = inp[i:i+6]

        curr_c = b_t_e[curr_str]

        if(curr_c == "capital"):
            cap = True
        elif(curr_c == "number"):
            num = True
        elif(curr_c == "decimal"):
            decimal = True
        else:
            if(cap): #indicators for changing the input
                out += curr_c.upper()
                cap = False
            elif(curr_c == ""):
                out += curr_c
                num = False

            elif(num): #dont reset num bool until space
                out += b_t_n[curr_str]

            elif(decimal):
                out += b_t_p[curr_str]
                decimal = False

            else:
                out += curr_c
        i=i+6

    return out

def en_to_br(inp):
    out = ""
    num = False
    curr_c = ""

    i = 0
    while(i < len(inp)):
        curr_c = inp[i]

        if curr_c.isupper():
            out += e_t_b["capital"]
            out += e_t_b[curr_c.lower()]

        elif curr_c.isnumeric():
            if not num:
                out += e_t_b["number"]
                num = True
            out += e_t_b[curr_c]

        elif curr_c == " ":
            num = False
            out += e_t_b[" "]

        elif not curr_c.isalpha():
            out += e_t_b["decimal"]
            out += e_t_b[curr_c]

        else:
            out += e_t_b[curr_c]


        i+=1

    return out

user_inp = input()

if len(user_inp) == user_inp.count("O") + user_inp.count(".") and len(user_inp) % 6 == 0:
    print(br_to_en(user_inp))
else:
    print(en_to_br(user_inp))


