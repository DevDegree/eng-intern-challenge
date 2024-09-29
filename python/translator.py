import sys

def translate(stringo):
    mode = 0
    
    if all(char in ".O" for char in stringo):
        mode = 1

    braillePart1 = {
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
    }

    braillePart2 = {
    }

    for letter in "klmnopqrst":
        braillePart2.update({letter:braillePart1[chr(ord(letter)-10)][:4]+"O."})

    braillePart3 = {
    }

    for letter in "uv":
        braillePart3.update({letter:braillePart2[chr(ord(letter)-10)][:5]+"O"})

    braillePart3.update({"w":".OOO.O"})

    for letter in "xyz":
        braillePart3.update({letter:braillePart2[chr(ord(letter)-11)][:5]+"O"})     

    braillePart4 = {    
        "." : "..OO.O",
        "," : "..O...O",
        "?" : "..O..OO",
        "!" : "..OOOO",
        ":" : "..OO..",
        ";" : "..O.OO",
        "-" : "....OO",
        "/" : "O..OO.O",
        #"<" : "O..OO.",
        #">" : ".OO..O",
        "(" : ".O.OO.",
        ")" : "O.O..O",
        " " : "......"
    }

    brailleNumbers = {
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
    }

    braille = {} 
    braille.update(braillePart1)
    braille.update(braillePart2)
    braille.update(braillePart3)
    braille.update(braillePart4)

    final = ""

    if mode == 0:
        isNumber = False

        for i in stringo:
            if i.isdigit() == True:
                if isNumber == False:
                    final = final + ".O.OOO"
                    isNumber = True

                final = final + brailleNumbers[i]
                
            else:
                isNumber = False
                if i.isupper() == True:
                    final = final + ".....O"
                final = final + braille[i.lower()]

        return(final)

    else:
        letters = {i:x for x,i in braille.items()}
        numbers = {i:x for x,i in brailleNumbers.items()}

        brailleGrouping = []

        for i in range(0, len(stringo), 6):
            brailleGrouping.append(stringo[i:i+6])

        isNumber = False
        isCapital = False

        for i in brailleGrouping:
            if i == ".O.OOO":
                isNumber = True
            
            elif isNumber == True:
                if i not in numbers:
                    isNumber = False
                    final = final + letters[i]

                else:
                    final = final + numbers[i]
            
            elif i == ".....O":
                isCapital = True
                isNumber = False

            elif isCapital == True:
                final = final + letters[i].upper()
                isCapital = False

            else:
                final = final + letters[i]
                
        return(final)
        
if __name__ == "__main__":
    text = " ".join(sys.argv[1:])
    result = translate(text)
    print(result)