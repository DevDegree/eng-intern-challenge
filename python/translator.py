import sys

braile_mappings = {
    "A": "O.....",
    "B": "O.O...",
    "C": "OO....",
    "D": "OO.O..",
    "E": "O..O..",
    "F": "OOO...",
    "G": "OOOO..",
    "H": "O.OO..",
    "I": ".OO...",
    "J": ".OOO..",
    "K": "O...O.",
    "L": "O.O.O.",
    "M": "OO..O.",
    "N": "OO.OO.",
    "O": "O..OO.",
    "P": "OOO.O.",
    "Q": "OOOOO.",
    "R": "O.OOO.",
    "S": ".OO.O.",
    "T": ".OOOO.",
    "U": "O...OO",
    "V": "O.O.OO",
    "W": ".OOO.O",
    "X": "OO..OO",
    "Y": "OO.OOO",
    "Z": "O..OOO",
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
    "capital": ".....O",
    "number": ".O.OOO",
    "space": "......"
}

braille_to_english = {a: b for b, a in braile_mappings.items() if not b.isdigit()}
braille_to_numbers = {a: b for b, a in braile_mappings.items() if b.isdigit()}

# converts braile to english        
def bra_to_eng(s: str) -> str:
    
    number_mode = False
    captial_mode = False

    result = []

    braile_words = [s[i:i+6] for i in range(0, len(s), 6)]

    for word in braile_words:

        if number_mode:

            if braille_to_english[word] != "space":
                result.append(braille_to_numbers[word])
            else:
                result.append(" ")
                number_mode = False

        else:
            if braille_to_english[word] == "number":
                number_mode = True
            elif braille_to_english[word] == "capital":
                captial_mode = True
            elif braille_to_english[word] == "space":
                result.append(" ")
            else:
                result.append(braille_to_english[word] if captial_mode else braille_to_english[word].lower())
                captial_mode = False
    
    return "".join(result)

def eng_to_bra(s: str) -> str:

    number_mode = False
    result = []

    for c in s:
        if number_mode:
            if c != " ":
                result.append(braile_mappings[c])
            else:
                number_mode = False
                result.append(braile_mappings["space"])
        else:
            if c == " ":
                result.append(braile_mappings["space"])
            elif c.isdigit():
                result.append(braile_mappings["number"])
                result.append(braile_mappings[c])
                number_mode = True
            else:
                if c.isupper():
                    result.append(braile_mappings["capital"])
                
                result.append(braile_mappings[c.upper()])

    return "".join(result)


def is_english(s):
    return s.count(".") == 0

def main():
    if len(sys.argv) in [0, 1]:
        sys.exit(1)
    
    elif len(sys.argv) == 2:
        test = sys.argv[1]
        out = eng_to_bra(test) if is_english(test) else bra_to_eng(test)
        print(out)
    
    else:
        ch = " " if is_english(sys.argv[1]) else braile_mappings["space"]
        test = ch.join([sys.argv[i] for i in range(1, len(sys.argv))])
        out = eng_to_bra(test) if is_english(test) else bra_to_eng(test)
        print(out)

if __name__ == "__main__":
    main()
    
    