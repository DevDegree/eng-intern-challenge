import sys
import re
from collections import defaultdict

class BrailleTranslator:

    mapAlphabetBraille = defaultdict(str, 
        {
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
        }
    )

    mapSymbolBraille = defaultdict(str, 
        {
            "capital": ".....O",
            "number": ".O.OOO",
            " ": "......"
        }
    )

    mapNumberBraille = defaultdict(str, 
        {
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
        }
    )

    mapBrailleAlphabet = defaultdict(str)
    mapBrailleNumber = defaultdict(str)
    mapBrailleSymbol = defaultdict(str)

    def __init__(self):
        # Create the reverse maps
        for key, value in self.mapAlphabetBraille.items():
            self.mapBrailleAlphabet[value] = key
        for key, value in self.mapNumberBraille.items():
            self.mapBrailleNumber[value] = key
        for key, value in self.mapSymbolBraille.items():
            self.mapBrailleSymbol[value] = key

    def translate(self, text):        
        if self.__isBraille(text):
            return self.__translateToAlphabet(text)
        if self.__isAlphabet(text):
            return self.__translateToBraille(text)
        raise Exception("Invalid input. It should be either braille or alphabet.")

    def __translateToBraille(self, text):
        chars = list(text)[::-1] # Reverse the text to be able to pop
        brailles = []
        while chars:
            char = chars.pop()
            # Handle space
            if char == " ":
                brailles.append(self.mapSymbolBraille[char])
                continue

            # Handle capital
            if char.isupper():
                brailles.append(self.mapSymbolBraille["capital"])
                brailles.append(self.mapAlphabetBraille[char.lower()])
                continue
            
            # Handle number
            if char.isnumeric():
                brailles.append(self.mapSymbolBraille["number"])
                brailles.append(self.mapNumberBraille[char])
                # Iterate until  next space
                while chars and chars[-1] != " ":
                    nextChar = chars.pop()
                    if nextChar in self.mapNumberBraille:
                        brailles.append(self.mapNumberBraille[nextChar])
                    else:
                        raise Exception("Invalid text. It should be a number.")
                continue

            # Handle alphabet
            if char in self.mapAlphabetBraille:
                brailles.append(self.mapAlphabetBraille[char])
            else:
                raise Exception("Invalid text. It should be an lowercase alphabet.")
  
        return "".join(brailles)

    
    def __translateToAlphabet(self, text):
        if len(text) % 6 != 0:
            raise Exception("Invalid braille length. The input text should be multiples of 6.")
        # Separate text in groups of 6 to create brailles
        # Reverse to be able to pop
        brailles = [text[i:i+6] for i in range(0, len(text), 6)][::-1]

        alphabets = []
        while brailles:
            braille = brailles.pop()
            # Handle space
            if self.mapBrailleSymbol[braille] == " ":
                alphabets.append(" ")
                continue

            # Handle capital
            if self.mapBrailleSymbol[braille] == "capital":
                nextBraille = brailles.pop()
                if nextBraille in self.mapBrailleAlphabet:
                    alphabets.append(self.mapBrailleAlphabet[nextBraille].upper())
                else:
                    raise Exception("Invalid text after capital")
                continue
                
            # Handle number
            if self.mapBrailleSymbol[braille] == "number":
                # Iterate until next space
                while brailles and brailles[-1] != self.mapSymbolBraille[" "]:
                    braille = brailles.pop()
                    if braille in self.mapBrailleNumber:
                        alphabets.append(self.mapBrailleNumber[braille])
                    else:
                        raise Exception("Invalid text. It should be a number.")
                continue

            # Handle alphabet
            if braille in self.mapBrailleAlphabet:
                alphabets.append(self.mapBrailleAlphabet[braille])
            else:
                raise Exception("Invalid text. Couldn't find the alphabet.")
        return "".join(alphabets)
    
    def __isBraille(self, text):
        return bool(re.match(r"^[O.]+$", text))
       
    def __isAlphabet(self, text):        
        for char in text:
            if char.lower() in self.mapAlphabetBraille: continue
            if char in self.mapNumberBraille: continue
            if char in self.mapSymbolBraille: continue
            return False
        return True

def main():
    if len(sys.argv) < 2:
        print("Invalid arguments. Ignore the program.")
        sys.exit(1)
    
    source = " ".join(sys.argv[1:])
    translator = BrailleTranslator()
    print(translator.translate(source))
    
if __name__ == "__main__":
    main()