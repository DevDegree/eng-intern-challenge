from braille import *
from functions import *
from sys import argv

phrase = ' '.join(argv[1:])
detected = detect(phrase)

if detected == 'braille':
    parsedBraille = parseBraille(phrase)
    translatedList = translateBraille2English(parsedBraille)

else: # detected == 'english'

    parsedEnglish = parseEnglish(phrase)
    translatedList = translateEnglish2Braille(parsedEnglish)

print(''.join(translatedList))