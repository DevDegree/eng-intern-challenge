import sys
from enum import Enum

class CharacterType(Enum):
    NORMAL = 1
    CAPITAL_FOLLOWS = 2
    NUMBER_FOLLOWS = 3

class Character:
    type = CharacterType
    asciiz = str
    braille = str
    
    def __init__(self, braille, type=CharacterType.NORMAL, asciiz=None):
        self.type = type
        self.asciiz = asciiz
        self.braille = braille
        
class Translator:
    CHARACTER_CAPITAL = Character(".....O", type=CharacterType.CAPITAL_FOLLOWS)
    CHARACTER_NUMBER = Character(".O.OOO", type=CharacterType.NUMBER_FOLLOWS)

    CHARACTERS = [
        Character("O.....", asciiz="a"),
        Character("O.O...", asciiz="b"),
        Character("OO....", asciiz="c"),
        Character("OO.O..", asciiz="d"),
        Character("O..O..", asciiz="e"),
        Character("OOO...", asciiz="f"),
        Character("OOOO..", asciiz="g"),
        Character("O.OO..", asciiz="h"),
        Character(".OO...", asciiz="i"),
        Character(".OOO..", asciiz="j"),
        Character("O...O.", asciiz="k"),
        Character("O.O.O.", asciiz="l"),
        Character("OO..O.", asciiz="m"),
        Character("OO.OO.", asciiz="n"),
        Character("O..OO.", asciiz="o"),
        Character("OOO.O.", asciiz="p"),
        Character("OOOOO.", asciiz="q"),
        Character("O.OOO.", asciiz="r"),
        Character(".OO.O.", asciiz="s"),
        Character(".OOOO.", asciiz="t"),
        Character("O...OO", asciiz="u"),
        Character("O.O.OO", asciiz="v"),
        Character(".OOO.O", asciiz="w"),
        Character("OO..OO", asciiz="x"),
        Character("OO.OOO", asciiz="y"),
        Character("O..OOO", asciiz="z"),
        CHARACTER_CAPITAL,
        CHARACTER_NUMBER,
        Character("......", asciiz=" ")
    ]

    NUMBERS = [
        Character("O.....", asciiz="1"),
        Character("O.O...", asciiz="2"),
        Character("OO....", asciiz="3"),
        Character("OO.O..", asciiz="4"),
        Character("O..O..", asciiz="5"),
        Character("OOO...", asciiz="6"),
        Character("OOOO..", asciiz="7"),
        Character("O.OO..", asciiz="8"),
        Character(".OO...", asciiz="9"),
        Character(".OOO..", asciiz="0"),
    ]
    
    ASCII_TO_CHARACTER_MAP = {character.asciiz: character for character in (CHARACTERS + NUMBERS)}
    BRAILLE_TO_CHARACTER_MAP = {character.braille: character for character in CHARACTERS}
    BRAILLE_TO_NUMBER_CHARACTER_MAP = {character.braille: character for character in NUMBERS}

    def brailleToASCII(self, braille: str):
        """Translates a braille string to ASCII. Prints the output to stdout.
        
        Returns: 
                True, if the translation was successful.
        """

        if len(braille) % 6 != 0:
            return False
        capital = False
        number = False
        asciiz = ""
        for i in range(0, len(braille), 6):
            characterString = braille[i:i+6]
            # find ascii character corresponding to braille
            if characterString in self.BRAILLE_TO_CHARACTER_MAP:
                character = self.BRAILLE_TO_CHARACTER_MAP[characterString]
                # precondition: if in number mode, this symbol must be a number
                if number:
                    # unless if it's a space, which ends number mode
                    if character.asciiz == " ":
                        number = False
                    else:
                        if characterString not in self.BRAILLE_TO_NUMBER_CHARACTER_MAP:
                            return False
                        character = self.BRAILLE_TO_NUMBER_CHARACTER_MAP[characterString]
                
                if character == self.CHARACTER_CAPITAL:
                    capital = True
                elif character == self.CHARACTER_NUMBER:
                    number = True
                else:
                    if capital:
                        # precondition: this symbol must be capitalizable (a-z)
                        if ord(character.asciiz) < ord("a") or ord(character.asciiz) > ord("z"):
                            return False
                        asciiz += character.asciiz.upper()
                        capital = False
                    else:
                        asciiz += character.asciiz
            else:
                return False
        print(asciiz, end='')
        return True

    def asciiToBraille(self, asciiz: str):
        """Translates an ASCII string to braille. Prints the output to stdout."""
        number = False
        for character in asciiz:
            if character.isupper():
                # precondition: this character must be capitalizable (a-z)
                if character.lower() in self.ASCII_TO_CHARACTER_MAP:
                    print(self.CHARACTER_CAPITAL.braille, end='')
                    character = character.lower()
            # precondition: alphabet is from (a-z, 0-9, space)
            if character in self.ASCII_TO_CHARACTER_MAP:
                if not number and ord(character) >= ord("0") and ord(character) <= ord("9"):
                    print(self.CHARACTER_NUMBER.braille, end='')
                    number = True
                elif character == " ":
                    number = False
                print(self.ASCII_TO_CHARACTER_MAP[character].braille, end='')

arguments = sys.argv[1:]
argumentString = " ".join(arguments)
translator = Translator()
# Try translating to ASCII.
success = translator.brailleToASCII(argumentString)
# If it fails, try translating to Braille.
if not success:
    translator.asciiToBraille(argumentString)
sys.stdout.flush()
