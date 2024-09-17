from brailles_constants import LATIN_ENGLISH_ALPHABET, ENG_TO_BRAILLE, NUMERALS, NUMBER_TO_BRAILLE, PUNCTUATED, SPECIALLY

def isit_braille(s: str) -> bool:
    return all(c in 'O.' for c in s) and len(s) % 6 == 0

def poof_braille (input_string: str) -> str:
    res_transl = ""
    num_mode = False
    
    for word in input_string.split():
        if res_transl:  
            res_transl += ENG_TO_BRAILLE[' ']
        
        for c in word:
            if c.isnumeric():
                if not num_mode:
                    res_transl += ENG_TO_BRAILLE['digit']
                    num_mode = True
                res_transl += NUMBER_TO_BRAILLE[c]
            elif c in PUNCTUATED:
                res_transl += SPECIALLY.get(c, ENG_TO_BRAILLE.get(c, ''))
            elif c.isalpha():
                if num_mode:
                    num_mode = False
                if c.isupper():
                    res_transl += ENG_TO_BRAILLE['caps']
                res_transl += ENG_TO_BRAILLE[c.upper()]
            elif c == '.':
                res_transl += ENG_TO_BRAILLE['deci']
            else:
                raise ValueError(f"Invalid character in input: {c}")
        
        num_mode = False  # Reset num_mode at the end of each word
    
    return res_transl

def poof_english(braille_string: str) -> str:
    res_transl = ""
    isit_number = False
    capital_next = False

    for i in range(0, len(braille_string), 6):
        braille_char = braille_string[i:i+6]
        
        if braille_char == ENG_TO_BRAILLE['caps']:
            capital_next = True
        elif braille_char == ENG_TO_BRAILLE['digit']:
            isit_number = True
        elif braille_char == ENG_TO_BRAILLE[' ']:
            res_transl += ' '
            isit_number = False
        elif braille_char == ENG_TO_BRAILLE['deci']:
            res_transl += '.'
        elif isit_number:
            res_transl += NUMERALS[braille_char]
        else:
            char = LATIN_ENGLISH_ALPHABET.get(braille_char)
            if not char:
                raise ValueError(f"Invalid Braille pattern: {braille_char}")
            if capital_next:
                res_transl += char.upper()
                capital_next = False
            else:
                res_transl += char.lower()
    
    return res_transl
