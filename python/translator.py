import sys
import re
from enum import Enum

class CharacterType(Enum):
    NORMAL = 1
    CAPITAL_FOLLOWS = 2
    DECIMAL_FOLLOWS = 3
    NUMBER_FOLLOWS = 4

class Character:
    type = CharacterType
    asciiz = str
    braille = str
    
    def __init__(self, braille, type=CharacterType.NORMAL, asciiz=None):
        self.type = type
        self.asciiz = asciiz
        self.braille = braille
        
CHARACTER_CAPITAL = Character(".....O", type=CharacterType.CAPITAL_FOLLOWS)
CHARACTER_DECIMAL = Character(".O...O", type=CharacterType.DECIMAL_FOLLOWS)
CHARACTER_NUMBER = Character(".O.OOO", type=CharacterType.NUMBER_FOLLOWS)

characters = [
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
    Character("......", asciiz=" "),
    Character("..OO.O", asciiz="."),
    Character("..O...", asciiz=","),
    Character("..O.OO", asciiz="?"),
    Character("..OOO.", asciiz="!"),
    Character("..OO..", asciiz=":"),
    Character("..O.O.", asciiz=";"),
    Character("....OO", asciiz="-"),
    Character(".O..O.", asciiz="/"),
    Character(".OO..O", asciiz="<"),
    Character("O..OO.", asciiz=">"),
    Character("O.O..O", asciiz="("),
    Character(".O.OO.", asciiz=")"),
]

numbers = [
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
