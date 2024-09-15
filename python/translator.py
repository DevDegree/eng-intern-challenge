from brailleTranslator import brailleTranslator
from englishTranslator import englishTranslator
import sys

def translate(input_string:str) -> str:
    if (len(input_string) % 6 == 0 and all(char in ('.', 'O') for char in input_string)):
        translated = brailleTranslator(input_string)
    else:
        translated = englishTranslator(input_string)
    return(translated)

print(translate(" ".join(sys.argv[1:])))

