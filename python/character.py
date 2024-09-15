from bidict import bidict

braille_capital_symbol = ".....O"
braille_number_follows = ".O.OOO"
braille_blank_space = "......"

braille_numbers = bidict({
   "O.....": "1","O.O...": "2","OO....": "3","OO.O..": "4","O..O..": "5",
   "OOO...": "6","OOOO..": "7","O.OO..": "8",".OO...": "9",".OOO..": "O",
})

braille_symbols = bidict({
   "..OO.O": ".", "..O...": ",","..O.OO": "?", "..OOO.": "!", "..OO..":":",
   "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<", "O..OO.": ">",
   "O.O..O":"(",".O.OO.": ")", "......": " "
})

braille_letters = bidict({
   "O.....": "a","O.O...": "b","OO....": "c","OO.O..": "d","O..O..": "e",
   "OOO...": "f","OOOO..": "g","O.OO..": "h",".OO...": "i",".OOO..": "j",
   "O...O.": "k","O.O.O.": "l","OO..O.": "m","OO.OO.": "n","O..OO.": "o",
   "OOO.O.": "p","OOOOO.": "q","O.OOO.": "r",".OO.O.": "s",".OOOO.": "t",
   "O...OO": "u","O.O.OO": "v",".OOO.O": "w","OO..OO": "x","OO.OOO": "y",
   "O..OOO": "z",
   
   ".....OO.....": "A",".....OO.O...": "B",".....OOO....": "C",".....OOO.O..": "D",".....OO..O..": "E",
   ".....OOOO...": "F",".....OOOOO..": "G",".....OO.OO..": "H",".....O.OO...": "I",".....O.OOO..": "J",
   ".....OO...O.": "K",".....OO.O.O.": "L",".....OOO..O.": "M",".....OOO.OO.": "N",".....OO..OO.": "O",
   ".....OOOO.O.": "P",".....OOOOOO.": "Q",".....OO.OOO.": "R",".....O.OO.O.": "S",".....O.OOOO.": "T",
   ".....OO...OO": "U",".....OO.O.OO": "V",".....O.OOO.O": "W",".....OOO..OO": "X",".....OOO.OOO": "Y",
   ".....OO..OOO": "Z",
   
   # "..OO.O": ".", "..O...": ",","..O.OO": "?", "..OOO.": "!", "..OO..":":",
   # "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<", "O..OO.": ">",
   # "O.O..O":"(",".O.OO.": ")", "......": " "
})