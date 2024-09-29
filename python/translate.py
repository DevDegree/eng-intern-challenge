"""

Translate Application that translates between English and Braille.

The criteria used for determining whether a string is Braille representation
    1. can only use `O`(letter O) and `.`
    2. the length should be multiples of 6.

"""

import itertools

import constants


def translate(message: list[str]) -> str:
    """Entrypoint."""
    s = " ".join(message)
    if _is_braille(s):
        return translate_braille(s)
    else:
        return translate_english(s)


def translate_braille(braille_str: str) -> str:
    """Braille to English."""
    res = []
    idx = 0
    braille_words = [
        "".join(w)
        for w in itertools.batched(list(braille_str), constants.BRAILLE_WORD_SIZE)
    ]
    while idx < len(braille_words):
        braille_word = braille_words[idx]
        if braille_word == constants.BrailleModifier.capital.to_braille():
            idx += 1
            next_word = braille_words[idx]
            res.append(constants.BRAILLE_TO_ENG[next_word].upper())
            idx += 1
        elif braille_word == constants.BrailleModifier.number.to_braille():
            idx += 1
            while idx < len(braille_words) and braille_words[idx] != constants.ENG_TO_BRAILLE[" "]:
                res.append(constants.BRAILLE_TO_NUM[braille_words[idx]])
                idx += 1
        else:
            res.append(constants.BRAILLE_TO_ENG[braille_word])
            idx += 1
            
    return "".join(res)


def translate_english(english_str: str) -> str:
    """English to Braille."""
    res = []
    idx = 0
    while idx < len(english_str):
        if english_str[idx].isupper():
            # prepend "capital follows" modifer for uppercase letters.
            res.append(constants.BrailleModifier.capital.to_braille())
            res.append(constants.ENG_TO_BRAILLE[english_str[idx].lower()])
            idx += 1
        elif english_str[idx].isnumeric():
            res.append(constants.BrailleModifier.number.to_braille())
            # find all consecutive numeric chars until next space
            while idx < len(english_str) and english_str[idx] != " ":
                res.append(constants.ENG_TO_BRAILLE[english_str[idx]])
                idx += 1
        else:
            res.append(constants.ENG_TO_BRAILLE[english_str[idx]])
            idx += 1
    return "".join(res)


def _is_braille(s: str) -> bool:
    """Whether given string is Braille representation.
    
    The criteria used:
    1. can only use `O`(letter O) and `.`
    2. the length should be multiples of 6.

    """
    chars = set(list(s))
    return (
        len(chars) == 2 and
        "O" in chars and
        "." in chars and
        len(s) % constants.BRAILLE_WORD_SIZE == 0
    )

