braille_to_eng = {
    # Letters
    'a': "0.....", 'b': "0.0...", 'c': "00....", 'd': "00.0..", 'e': "0..0..",
    'f': "000...", 'g': "0000..", 'h': "0.00..", 'i': ".00...", 'j': ".000..",
    'k': "0...0.", 'l': "0.0.0.", 'm': "00..0.", 'n': "00.00.", 'o': "0..00.",
    'p': "000.0.", 'q': "00000.", 'r': "0.000.", 's': ".00.0.", 't': ".0000.",
    'u': "0...00", 'v': "0.0.00", 'w': ".000.0", 'x': "00..00", 'y': "00.000",
    'z': "0..000",
    
    # Numbers
    '1': "0.....", '2': "0.0...", '3': "00....", '4': "00.0..", '5': "0..0..",
    '6': "000...", '7': "0000..", '8': "0.00..", '9': ".00...", '0': ".000..",

    # Characters
    '.': "..00.0", ',':"..0...", '?':"..0.00", '!':"..000.", ':':"..00..", 
    ';':"..0.0.", '-':"....00", '/':".0..0.", '<':".00..0", '>':"0..00.",
    '(':"0.0..0", ')':".0.00.", ' ':"......",

    # Other
    'cap': ".....0", 'dec': ".0...0", 'num':".0.000"
}

eng_to_braille = {
    v:k for k, v in braille_to_eng.items()
}
eng_to_braille.update({
    'cap': ".....0", 'dec': ".0...0", 'num':".0.000"
})


def detect_lang(text):
    return all(c in "o." for c in text)

def transl_to_braille(text):
    braille_text = []
    for char in text:
        if char.isupper():
            braille_text.append(eng_to_braille["cap"])
            char = char.lower()
        braille_text.append(eng_to_braille[char])
    return ''.join(braille_text)

def transl_to_eng(text):
    english_text = []
    i = 0
    while i < len(text):
        char = text[i:i+6] # interpret each chunk of 6 characters (o and .) as a distinct character
        if char == braille_to_eng["cap"]:
            i = i+6
            char = text[i:i+6]
            english_text.append(braille_to_eng[char]).upper()
            # make if statements for decimals and numbers
        else:
            english_text.append(braille_to_eng[char])