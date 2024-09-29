from textwrap import wrap
import sys


if __name__ == '__main__':
    braille = False
    if len(sys.argv) > 1:
        inp = " ".join(sys.argv[1:])  # Join all arguments into a single string
    else:
        inp = input()  # Fall back to interactive input if no command-line arguments
    num = False
    cap = False
    output = ""

    #Create a hashmap for the english to braille translations
    translation = {
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
        "q" : "OOOOO.",
        "r" : "O.OOO.",
        "s" : ".OO.O.",
        "t" : ".OOOO.",
        "u" : "O...OO",
        "v" : "O.O.OO",
        "w" : ".OOO.O",
        "x" : "OO..OO",
        "y" : "OO.OOO",
        "z" : "O..OOO",
        " " : "......"
    }

    numbers = {
        "1" : "O.....",
        "2" : "O.O...",
        "3" : "OO....",
        "4" : "OO.O..",
        "5" : "O..O..",
        "6" : "OOO...",
        "7" : "OOOO..",
        "8" : "O.OO..",
        "9" : ".OO...",
        "0" : ".OOO.."
    }

    special = {
        "cap" : ".....O",
        "num" : ".O.OOO",
        " " : "......"
    }

    #check if input contains only braille characters
    brchars = ['.','O']
    if all([i in brchars for i in inp]):
        braille = True

    #perform translation from braille to english
    if braille:
        str = wrap(inp, 6)
        #reverse key value pairs for braille to english
        special = dict((i,j) for j,i in special.items())
        numbers = dict((i,j) for j,i in numbers.items())
        translation = dict((i,j) for j,i in translation.items())
        for i in str:
            #check special cases first
            if i in special:
                val = special[i]
                if val == "cap":
                    cap = True
                elif val == "num":
                    num = True
                elif val == " ":
                    output += " "
                    num = False
            elif num:
                output += numbers[i]
            else:
                if cap:
                    output += translation[i].upper()
                    cap = False
                else:
                    output += translation[i]
    #perform translation for english to braille
    else:
        for i in inp:
            if i in numbers:
                if not num:
                    num = True
                    output += special["num"]
                output += numbers[i]
            else:
                num = False
                if i.isupper():
                    output += special["cap"]
                output += translation[i.lower()]

                

    print(output)
