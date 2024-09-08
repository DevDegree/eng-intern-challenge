braille_to_eng = {
    # Letters
    'a': "o.....", 'b': "o.o...", 'c': "oo....", 'd': "oo.o..", 'e': "o..o..",
    'f': "ooo...", 'g': "oooo..", 'h': "o.oo..", 'i': ".oo...", 'j': ".ooo..",
    'k': "o...o.", 'l': "o.o.o.", 'm': "oo..o.", 'n': "oo.oo.", 'o': "o..oo.",
    'p': "ooo.o.", 'q': "ooooo.", 'r': "o.ooo.", 's': ".oo.o.", 't': ".oooo.",
    'u': "o...oo", 'v': "o.o.oo", 'w': ".ooo.o", 'x': "oo..oo", 'y': "oo.ooo",
    'z': "o..ooo",
    
    # Numbers
    '1': "o.....", '2': "o.o...", '3': "oo....", '4': "oo.o..", '5': "o..o..",
    '6': "ooo...", '7': "oooo..", '8': "o.oo..", '9': ".oo...", '0': ".ooo..",

    # Characters
    '.': "..oo.o", ',':"..o...", '?':"..o.oo", '!':"..ooo.", ':':"..oo..", 
    ';':"..o.o.", '-':"....oo", '/':".o..o.", '<':".oo..o", '>':"o..oo.",
    '(':"o.o..o", ')':".o.oo.", ' ':"......",

    # Other
    'cap': ".....o", 'dec': ".o...o", 'num':".o.ooo"
}

eng_to_braille = {
        # Letters
    'a': "o.....", 'b': "o.o...", 'c': "oo....", 'd': "oo.o..", 'e': "o..o..",
    'f': "ooo...", 'g': "oooo..", 'h': "o.oo..", 'i': ".oo...", 'j': ".ooo..",
    'k': "o...o.", 'l': "o.o.o.", 'm': "oo..o.", 'n': "oo.oo.", 'o': "o..oo.",
    'p': "ooo.o.", 'q': "ooooo.", 'r': "o.ooo.", 's': ".oo.o.", 't': ".oooo.",
    'u': "o...oo", 'v': "o.o.oo", 'w': ".ooo.o", 'x': "oo..oo", 'y': "oo.ooo",
    'z': "o..ooo",
    
    # Numbers
    '1': "o.....", '2': "o.o...", '3': "oo....", '4': "oo.o..", '5': "o..o..",
    '6': "ooo...", '7': "oooo..", '8': "o.oo..", '9': ".oo...", '0': ".ooo..",

    # Characters
    '.': "..oo.o", ',':"..o...", '?':"..o.oo", '!':"..ooo.", ':':"..oo..", 
    ';':"..o.o.", '-':"....oo", '/':".o..o.", '<':".oo..o", '>':"o..oo.",
    '(':"o.o..o", ')':".o.oo.", ' ':"......",

    # Other
    'cap': ".....o", 'dec': ".o...o", 'num':".o.ooo"

}

def is_braille(text):
    return all(char in "o." for char in text)


def transl_to_braille(text):
    braille_text = []
    words = text.split()  # separate words/numbers/decimals in the input
    for i,word in enumerate(words):
        if word.isdigit() or word.replace('.', '', 1).isdigit():  # check if it's a number or decimal
            if word == word.replace('.', '', 1):
                braille_text.append(eng_to_braille["num"])  
            else:
                braille_text.append(eng_to_braille["dec"])
            for char in word:
                braille_text.append(eng_to_braille[char])
        else:  # process letters and other characters
            for char in word:
                if char.isupper():
                    braille_text.append(eng_to_braille["cap"])  # indicate following letter is upper case
                    char = char.lower()
                braille_text.append(eng_to_braille[char])
        if i< len(words) -1 :
            braille_text.append("......")  # add space between words
    return ''.join(braille_text) # remove trailing space


def transl_to_eng(text):
    english_text = []
    i = 0
    while i < len(text):
        char = text[i:i+6] # interpret each chunk of 6 characters (o and .) as a distinct character

        
        if char == braille_to_eng.get('cap'):
            i = i+6
            char = text[i:i+6]
            english_text.append(braille_to_eng.get(char, '?').upper())
            i+=6
            continue
        # make if statements for decimals and numbers
        if char == braille_to_eng.get('num'):
            i = i+6
            # keep reading numbers until space is encountered
            while i<len(text) and text[i:i+6] !="......":
                char = text[i:i+6]
                english_text.append(braille_to_eng.get(char, '?'))
                i+=6
            continue
        if char == braille_to_eng.get('dec'):
            english_text.append(".")
            i+=6
            continue

        if char in braille_to_eng:
            english_text.append(braille_to_eng[char])
        else:
            english_text.append('?')  # Handle unknown Braille characters
        
        i += 6  # Move to the next Braille character        
    return ''.join(english_text)


def translator(input):
    if is_braille(input):
        return transl_to_eng(input)
    else:
        return transl_to_braille(input)

import sys
def main(): 
    input = sys.argv[1]
    translated_input = translator(input)
    print(translated_input)

if __name__ == "__main__":
    main()