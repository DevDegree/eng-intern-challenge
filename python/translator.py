import argparse

braille_length = 6
# Braille letters sequentially in array
e2b_letter = [
    "O.....",
    "O.O...",
    "OO....",
    "OO.O..",
    "O..O..",
    "OOO...",
    "OOOO..",
    "O.OO..",
    ".OO...",
    ".OOO..",
    "O...O.",
    "O.O.O.",
    "OO..O.",
    "OO.OO.",
    "O..OO.",
    "OOO.O.",
    "OOOOO.",
    "O.OOO.",
    ".OO.O.",
    ".OOOO.",
    "O...OO",
    "O.O.OO",
    ".OOO.O",
    "OO..OO",
    "OO.OOO",
    "O..OOO",
]

# All braille translations according to the ascii table of the english language in an array for quick access using ord
e2b_ascii = ["......", "..OOO.", None, None, None, None, None, None, "O.O..O", ".O.OO.", None, None, "..O...", "....OO", "..OO.O", ".O..O.", ".OOO.."] + \
            e2b_letter[0:9] + ["..OO..", "..O.O.", ".OO..O", None, "O..OO.", "..O.OO", None] + [".....O" + s for s in e2b_letter] + \
            6*[None] + e2b_letter + 4*[None]

braille_capital = ".....O"
braille_number = ".O.OOO" 

# Hashmap from braille sequence to english character for quick access
b2e_map = {}
for i in range(len(e2b_ascii)):
    if not (48 <= i <= 57):
        b2e_map[e2b_ascii[i]] = chr(i+32)

parser = argparse.ArgumentParser(description="Please pass a Braille/English text to be translated to the opposite option.")
parser.add_argument('text', metavar='T', type=str, nargs="+",
                    help='Text to be translated to Braille/English')

text = " ".join(parser.parse_args().text)

text_type = 0
for c in text:
    if c != "." and c != "O":
        text_type = 1

if text_type == 1:
    # English text to translate to braille
    translated = ""
    number = False
    for i in range(len(text)):
        c = text[i]
        ascii = ord(c)
        # This character is a number or a period with the next one being a number
        in_number = 48 <= ascii <= 57 or (ascii == 46 and i < len(text) - 1 and 48 <= ord(text[i+1]) <= 57)
        
        if in_number and number == False:
            translated += braille_number
            number = True
        elif not in_number and number == True:
            number = False
        if 32 <= ascii <= 126:
            translated += e2b_ascii[ascii - 32]
        else:
            print(f"Error, no translation found for character {c}")
else:
    # Braille text to english
    translated = ""
    capital = False
    number = False
    for i in range(0, len(text), braille_length):
        symbol = text[i:i+braille_length]
        
        char = ""
        if symbol == braille_capital:
            capital = True
            continue
        if symbol == braille_number:
            number = True
            continue
        
        if capital:
            char = b2e_map.get(braille_capital+symbol)
            capital = False
        elif number:
            # Math fix for the fact that numbers start at 1 and end at 0 in braille
            char = chr(((ord(b2e_map[symbol]) - 97 + 1) % 9)+48) if b2e_map.get(symbol) else ""
        else:
            if symbol == e2b_ascii[0]:
                number = False
            char = b2e_map.get(symbol) 

        if char:
            translated += char
        else:
            print(f"Error, no translation found for sequence {symbol}.")
        
print(translated)