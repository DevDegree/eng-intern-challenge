import sys

eng_to_braille = {
    'a': "O.....",
    'b': "O.O...",
    'c': "OO....",
    'd': "OO.O..",
    'e': "O..O..",
    'f': "OOO...",
    'g': "OOOO..",
    'h': "O.OO..",
    'i': ".OO...",
    'j': ".OOO..",
    'k': "O...O.",
    'l': "O.O.O.",
    'm': "OO..O.",
    'n': "OO.OO.",
    'o': "O..OO.",
    'p': "OOO.O.",
    'q': "OOOOO.",
    'r': "O.OOO.",
    's': ".OO.O.",
    't': ".OOOO.",
    'u': "O...OO",
    'v': "O.O.OO",
    'w': ".OOO.O",
    'x': "OO..OO",
    'y': "OO.OOO",
    'z': "O..OOO",
    '.': "..OO.O",
    ',': "..O...",
    '?': "..OO..",
    '!': "..OOO.",
    ';': "..O.O.",
    ':': "..O.O.",
    '-': "..O..O",
    '/': ".O..O.",
    '<': ".O...O",
    '>': ".OO..O",
    '(': ".OOO..",
    ')': ".O.OO.",
    ' ': "......",
    "capital_follows": ".....O",
    "number_follows": ".O.OOO",
    "decimal_follows": ".O...O"
}

eng_to_braille_numeric = {
    '1': "O.....",
    '2': "O.O...",
    '3': "OO....",
    '4': "OO.O..",
    '5': "O..O..",
    '6': "OOO...",
    '7': "OOOO..",
    '8': "O.OO..",
    '9': ".OO...",
    '0': ".OOO..",
}

braille_to_eng = {}
braille_to_eng_numeric = {}

for key, val in eng_to_braille.items():
    braille_to_eng[val] = key

for key, val in eng_to_braille_numeric.items():
    braille_to_eng_numeric[val] = key

def encode_english(string):
    out_string = ""
    encode_mode = "normal"

    for char in string:
        if char.isupper():
            out_string += eng_to_braille["capital_follows"]

        if char.isnumeric() and encode_mode == "normal":
            out_string += eng_to_braille["number_follows"]
            encode_mode = "number_follows"

        if char == " ":
            encode_mode = "normal"

        if encode_mode == "number_follows":
            if char == ".":
                out_string += eng_to_braille["decimal_follows"]
            else:
                out_string += eng_to_braille_numeric[char]
        else:
            out_string += eng_to_braille[char.lower()]

    return out_string


def decode_braille(string):
    out_str = ""

    decode_mode = "lowercase"
    for subStr in [string[i:i + 6] for i in range(0, len(string), 6)]:
        if braille_to_eng[subStr] == "capital_follows":
            decode_mode = "capital"
            continue
        elif braille_to_eng[subStr] == "number_follows":
            decode_mode = "number_follows"
            continue
        elif braille_to_eng[subStr] == "decimal_follows":
            out_str += "."
            continue

        if braille_to_eng[subStr] == " ":
            out_str += " "
            decode_mode = "lowercase"
        elif decode_mode == "capital":
            out_str += braille_to_eng[subStr].upper()
            decode_mode = "lowercase"
        elif decode_mode == "lowercase":
            out_str += braille_to_eng[subStr]
        elif decode_mode == "number_follows":
            out_str += braille_to_eng_numeric[subStr]

    return out_str

in_string = " ".join(sys.argv[1::])
# in_string = "Hello a 123.456"
# print(in_string)
# in_string = "Hello a 123.456"
# in_string = "Hello world"
# in_string = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
# print(in_string)

valid_braille_count = 0
for char in in_string:
    if char in ["O", "."]:
        valid_braille_count += 1

res = None
if valid_braille_count != len(in_string):
    res = encode_english(in_string)
else:
    res = decode_braille(in_string)

print(res)
# print(decode_braille(res))