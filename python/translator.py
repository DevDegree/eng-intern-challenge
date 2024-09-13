import sys

asciiToBinary = ["O.....","O.O...","OO....","OO.O..","O..O..","OOO...",
                "OOOO..","O.OO..",".OO...",".OOO..","O...O.","O.O.O.",
                "OO..O.","OO.OO.","O..OO.","OOO.O.","OOOOO.","O.OOO.",
                ".OO.O.",".OOOO.","O...OO","O.O.OO",".OOO.O","OO..OO",
                "OO.OOO","O..OOO", ".OOO.."]

def main():
    Message = ""

    if not len(sys.argv) == 1:
        braille = True
        count = 0
        for word in sys.argv[1]:
            for char in word:
                count += 1
                if char not in ['.', 'O']:
                    braille = False
                    break
            else:
                continue
            break

        if not count%6 == 0:
            braille = False

        for index in range(1, len(sys.argv)):
            space = ""
            capital = False
            number = False
            if not braille:
                space = "......"
                for char in sys.argv[index]: 
                    if char.isalpha():
                        if char.isupper():
                            Message += ".....O"
                            Message += asciiToBinary[ord(char) - ord('A')]
                        else:
                            Message += asciiToBinary[ord(char) - ord('a')]
                    elif char.isnumeric():
                        if not number:
                            Message += ".O.OOO"
                            
                        # Access 0 at index -1 due to mismatch in binary and ASCII
                        Message += asciiToBinary[ord(char) - ord('1')]
                        number = True;
                    elif char == '.':
                        Message += ".O.OOO" + "..OO.O"
                    elif char == ' ':
                        Message += "......"
                        number = False
            else:
                space = ""
                for jndex in range(0, len(sys.argv[index]), 6):
                    char = sys.argv[index][jndex:jndex+6]
                    if char == "..OO.O":
                        Message += '.'
                    elif char == "......":
                        Message += " "
                    elif char == ".OOO..":
                        Message += '0'
                    elif char == ".....O":
                        capital = True
                    elif char == ".O.OOO":
                        number = True
                    else:
                        asciiOffset = 97
                        if number:
                            asciiOffset = 49
                        elif capital:
                            asciiOffset = 65
                            capital = False

                        Message += chr(asciiToBinary.index(char) + asciiOffset)
                    
            if index < len(sys.argv) - 1:
                Message += space
   
    print(Message)
    return Message

if __name__ == '__main__':
    main()
