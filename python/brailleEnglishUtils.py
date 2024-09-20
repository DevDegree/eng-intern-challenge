from enum import Enum

class ModeChange(Enum):
    SPACE = 0
    CAPITAL = 1
    NUMBER = 2
    NONE = 3

__brailleToModeTable = {'......': ModeChange.SPACE,
                        '.....O': ModeChange.CAPITAL,
                        '.O.OOO': ModeChange.NUMBER}
__modeToBrailleTable = {change: braille for braille, change in __brailleToModeTable.items()}
__brailleToEngTable = {'O.....':'a',
                       'O.O...':'b',
                       'OO....':'c',
                       'OO.O..':'d',
                       'O..O..':'e',
                       'OOO...':'f',
                       'OOOO..':'g',
                       'O.OO..':'h',
                       '.OO...':'i',
                       '.OOO..':'j',
                       'O...O.':'k',
                       'O.O.O.':'l',
                       'OO..O.':'m',
                       'OO.OO.':'n',
                       'O..OO.':'o',
                       'OOO.O.':'p',
                       'OOOOO.':'q',
                       'O.OOO.':'r',
                       '.OO.O.':'s',
                       '.OOOO.':'t',
                       'O...OO':'u',
                       'O.O.OO':'v',
                       '.OOO.O':'w',
                       'OO..OO':'x',
                       'OO.OOO':'y',
                       'O..OOO':'z'}  
__engToBrailleTable = {char: braille for braille, char in __brailleToEngTable.items()}

def mode_change(char):
    if char in __brailleToModeTable:
        return __brailleToModeTable[char]
    return ModeChange.NONE

def mode_to_braille(mode):
    return __modeToBrailleTable[mode]

def eng_to_braille(char):
    return __engToBrailleTable[char]

def braille_to_eng(braille):
    return __brailleToEngTable[braille]

#Converts the english character to its corresponding braille number
def to_number(char):
    num = ord(char) - ord('a') + 1
    if(num < 10):
        return str(num)
    if(num == 10):
        return "0"
    #If the braille character does not have a corresponding number
    return None

def num_to_braille(char):
    num = int(char)
    if num > 9 or num < 0:
        return None
    #Transcribes using keys of the table, which is in braille
    return list(__brailleToEngTable)[(num-1)%10]

