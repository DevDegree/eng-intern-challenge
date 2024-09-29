import re

user_input = input(" ")

output_string = ""
numbers = False
uppercase = False

characters_to_braille_dict = {
    "a" : "O.....",
    "b" : "O.O...",
    "c" : "OO....",
    "d" : "OO.O..",
    "e" : "O..O..",
    "f" : "OOO...",
    "g" : "OOOO..",
    "h" : "O.OO..",
    "i" : ".OO...",
    "j" : ".OOO..",
    "k" : "O...O.",
    "l" : "O.O.O.",
    "m" : "OO..O.",
    "n" : "OO.OO.",
    "o" : "O..OO.",
    "p" : "OOO.O.",
    "r" : "O.OOO.",
    "s" : ".OO.O.",
    "t" : ".OOOO.",
    "u" : "O...OO",
    "v" : "O.O.OO",
    "w" : ".OOO.O",
    "x" : "OO..OO",
    "y" : "OO.OOO",
    "z" : "O..OOO",
    "." : "..OO.O",
    "," : "..O...",
    "?" : "..O.OO",
    "!" : "..OOO.",
    ":" : "..OO..",
    ";" : "..O.O.",
    "-" : "....OO",
    "/" : ".O..O.",

    "(" : "O.O..O",
    ")" : ".O.OO.",
    " ": "......",
}

numbers_to_braille_dict = {
    "1" : "O.....",
    "2" : "O.O...",
    "3" : "OO....",
    "4" : "OO.O..",
    "5" : "O..O..",
    "6" : "OOO...",
    "7" : "OOOO..",
    "8" : "O.OO..",
    "9" : ".OO...",
    "0" : ".OOO..",
    "<" : ".OO..O",
    ">" : "O..OO.",
}


barille_to_characters_dict = {
    "O....." :"a" ,
    "O.O..." : "b",
    "OO...." : "c",
    "OO.O.." : "d",
    "O..O.." : "e",
    "OOO..." : "f",
    "OOOO.." : "g",
    "O.OO.." : "h",
    ".OO..." : "i",
    ".OOO.." : "j",
    "O...O." : "k",
    "O.O.O." : "l",
    "OO..O." : "m",
    "OO.OO." : "n",
    "O..OO." : "o",
    "OOO.O." : "p",
    "O.OOO." : "r",
    ".OO.O." : "s",
    ".OOOO." : "t",
    "O...OO" : "u",
    "O.O.OO" : "v",
    ".OOO.O" : "w",
    "OO..OO" : "x" ,
    "OO.OOO" : "y",
    "O..OOO" : "z",
    "..OO.O" : ".",
    "..O..." : ",",
    "..O.OO" : "?",
    "..OOO." : "!",
    "..OO.." : ":",
    "..O.O." : ";",
    "....OO" : "-",
    ".O..O." : "/",
    "O.O..O" : "(",
    ".O.OO." : ")",
    "......": " ",
}

braille_to_number_dict = {
    "O....." : "1",
    "O.O..." : "2",
    "OO...." : "3",
    "OO.O.." : "4",
    "O..O.." : "5",
    "OOO..." : "6",
    "OOOO.." : "7",
    "O.OO.." : "8",
    ".OO..." : "9",
    ".OOO.." : "0",
    ".OO..O" : "<",
    "O..OO." : ">",
}

# Find out if English or Braille
# if true the input is braille and the output will be english
if bool(re.match(r'^[O.]*$', user_input)):
    # split string into characters
    braille_characters = []
    for i in range(0, len(user_input), 6):
        braille_characters.append(user_input[i:i+6])
        
    print(braille_characters)