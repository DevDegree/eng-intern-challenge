import sys #Need this to read system input 

# Braille to English Dictionary
braille_to_english = {
"O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
"OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
"O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
"OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
"O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
"O..OOO": "z", ".O.OOO": "num", ".....O": "cap", "......": " "
}

# English to Braille Dictionary
# Reversed it cause I'm too lazy to retype everything
english_to_braille = {v: k for k, v in braille_to_english.items()}

def main():
    print("Hey, this is printing to the command line!") #Test

if __name__ == "__main__":
    main()