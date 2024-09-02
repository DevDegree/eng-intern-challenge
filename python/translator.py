import argparse

import mapping

BRAILLE_ALPHABET = ['.', 'O']
TOKEN_LEN = 6

def isTextBraille(text):
    return all(x in BRAILLE_ALPHABET for x in text)

def convertEnglishToBraille(text):
    res = ""

    numberFollows = False
    for c in text:
        if c.isupper():
            res += mapping.CAPITAL_FOLLOWS_TOKEN
            c = c.lower() # mapping's dictionary contains lowercase keys
        elif not numberFollows and c.isnumeric():
            res += mapping.NUMBER_FOLLOWS_TOKEN
            numberFollows = True
        elif c == ' ':
            numberFollows = False
            
        res += mapping.DIGIT_TO_BRAILLE[c] if numberFollows else mapping.CHAR_TO_BRAILLE[c]
    return res

def isBrailleTextValid(text, tokens):
    return all(token in mapping.VALID_BRAILLE_TOKENS for token in tokens) and len(text) % TOKEN_LEN == 0 

def convertBrailleToEnglish(text):
    tokens = [ text[i:i+TOKEN_LEN] for i in range(0, len(text), TOKEN_LEN) ]
    if not isBrailleTextValid(text, tokens): return ""

    res = ""
    capitalFollows = False
    numberFollows = False
    for token in tokens:
        if token == mapping.CAPITAL_FOLLOWS_TOKEN:
            capitalFollows = True
        elif token == mapping.NUMBER_FOLLOWS_TOKEN:
            numberFollows = True
        else:
            translatedToken = mapping.BRAILLE_TO_CHAR[token]

            if capitalFollows:
                translatedToken = translatedToken.upper()
                capitalFollows = False
            elif translatedToken == ' ':
                numberFollows = False
            elif numberFollows:
                translatedToken = mapping.BRAILLE_TO_DIGIT[token]

            res += translatedToken
    
    return res

def formatInput(args):
    text = ' '.join(args.text) # different words are given to us in a list
    text = text.replace('../', '.') # gets around the way inputting "..." actually inserts "../.." in terminal
    text = text.strip()

    return text

def main(args):
    text = formatInput(args)
    res = ''

    if isTextBraille(text):
        res = convertBrailleToEnglish(text)
    else:
        res = convertEnglishToBraille(text)
    if not res: return

    print(res)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Eng Intern Challenge Fall - Winter 2025 by Patrick Deniso")
    
    parser.add_argument("text", nargs="+", help="Braille or English text to translate. The program will automatically detect alphabet.")
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version="1.0.0")
    )

    args = parser.parse_args()
    main(args)