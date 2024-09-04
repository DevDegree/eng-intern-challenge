import sys

def translate(to_trans):
    
    char_map = {
        "a": "O......",
        "b":"O.O...",
        "c":"OO....",
        "d":"OO.O..",
        "e":"O..O..",
        "f":"OOO...",
        "g":"OOOO..",
        "h":"O.OO..",
        "i":".OO...",
        "j":".OOO..",
        "k":"O...O.",
        "l":"O.O.O.",
        "m":"OO..O.",
        "n":"OO.OO.",
        "o":"O..OO.",
        "p":"OOO.O.",
        "q":"OOOOO.",
        "r":"O.OOO.",
        "s":".OO.O.",
        "t":".OOOO.",
        "u":"O...OO",
        "v":"O.O.OO",
        "w":".OOO.O",
        "x":"OO..OO",
        "y":"OO.OOO",
        "z":"O..OOO",
        ".":"..OO.O",
        ",":"..O...",
        "?":"..O.OO",
        "!":"..OOO.",
        ":":"..OO..",
        ";":"..O.O.",
        "-":"....OO",
        "/":".O..O.",
        "<":".OO..O",
        ">":"O..OO.",
        "(":"O.O..O",
        ")":".O.OO.",
        " ":"......"
    }

    num_map = {
        "1": "O......",
        "2":"O.O...",
        "3":"OO....",
        "4":"OO.O..",
        "5":"O..O..",
        "6":"OOO...",
        "7":"OOOO..",
        "8":"O.OO..",
        "9":".OO...",
        "0":".OOO.."
    }

    capf = ".....O"
    decf = ".O...O"
    numf = ".O.OOO"

    #Determine if englsh or braile
    #Split english into list of characters and braile into list of strings each 6 chars
    #Use dictionary to map opposite word
    #print completed word








def main():
    
    args = sys.argv[1:]

    to_trans = ''.join(args) 

    out = translate(to_trans)

    print(out)


if __name__ == "__main__":
    main()