from enum import Enum

str input = ''
bool foundNonBrailleSymbol = False
int inputLength = len(input)

public class dictionaries:
    brailleSymbols = {'o', '.'}

class inputLanguage (Enum):
    BRAILLE = 0
    ENGLISH = 1