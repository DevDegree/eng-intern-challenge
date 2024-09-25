import sys

english_To_Braille_Map = {
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
    "W": ".OO.OO",
    "X": "OO..OO",
    "Y": "OO.OOO",
    "Z": "O..OOO",
    "capital follows": ".....O",
    "number follows": ".O.OOO",
    " ": "......",
}

num_To_Braille_Map = {
    "0": ".OOO..",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
}

def translateToBraille():
    toTranslate = sys.argv[1:]
    translated = []
    is_number = False
    
    for word in toTranslate:
        for char in word:
            if char.isalpha():
                if char.isupper():
                    translated.append(english_To_Braille_Map["capital follows"])
                translated.append(english_To_Braille_Map[char.upper()])
                is_number = False
            elif char.isdigit():
                if not is_number:
                    translated.append(english_To_Braille_Map["number follows"])
                    is_number = True
                translated.append(num_To_Braille_Map[char])
            else:
                translated.append(english_To_Braille_Map.get(char, "......"))
                is_number = False
        translated.append(english_To_Braille_Map[" "])
    
    print("".join(translated).rstrip(english_To_Braille_Map[" "]))

def translateToEnglish():
    toTranslate = sys.argv[1:]
    translated = []
    
    for word in toTranslate:
        i = 0
        while i < len(word):
            group = word[i:i+6]
            if group == english_To_Braille_Map["capital follows"]:
                translated.append("\\")
            elif group == english_To_Braille_Map["number follows"]:
                translated.append("#")
            else:
                if translated and translated[-1] == "\\":
                    translated.pop()
                    translated.append(next(key for key, value in english_To_Braille_Map.items() if value == group).upper())
                elif translated and translated[-1] == "#":
                    translated.pop()
                    translated.append(next(key for key, value in num_To_Braille_Map.items() if value == group))
                    translated.append("#")
                else:
                    translated.append(next(key for key, value in english_To_Braille_Map.items() if value == group).lower())
            i += 6
    
    print("".join(translated).replace("#", "").replace("\\", ""))

def main():
    if all(char in ['O', '.'] for char in sys.argv[1]):
        translateToEnglish()
    else:
        translateToBraille()

if __name__ == "__main__":
    main()